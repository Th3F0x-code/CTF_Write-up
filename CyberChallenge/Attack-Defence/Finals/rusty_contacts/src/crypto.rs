use lazy_static::lazy_static;
use rand::distributions::Alphanumeric;
use rand::rngs::OsRng;
use rand::{thread_rng, Rng};
use rsa::{PaddingScheme, PublicKey as RsaPublicKey, RSAPublicKey};
use serde::{Deserialize, Serialize};
use std::error::Error;

lazy_static! {
    pub(crate) static ref AUTHORITY_RSA_PUBKEY: RSAPublicKey = {
        let der_bytes = b"0\x81\x9f0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x81\x8d\x000\x81\x89\x02\x81\x81\x00\xca\xc9\x16r\xc9\x83\xc6\xb25\x83p\xc1\x0f\xa8\xeb\xdeZ\xe2\xdc\x90\xa5~\xcd\x08\xf7\x14D\x8dZ\x038\xbe\xeeB]2x*-Lr\x93(s\xdf[\xb6\xd3\xaf~\x8f\xa9\xb3\xd4\x00\x9a\xab]\\\x02\x9e\x81\xe5\x95\x0cCypq\xf6\xe1\x08M\x01\x82\xe3\xc3\x0fes\x04F\xe8^\xd0v}\x95\xf1\xc6C\xa3[\xee\xd7/\xb5\xb5:\x90\x8ae\x1b\x8b\xed\xe6\xf6\xaf\x06\xdf\x1eHinj\x1d\xd8\xd9N\x8a\xcd\x12K\xd6u\xb9_\xa3\x02\x03\x01\x00\x01";
        RSAPublicKey::from_pkcs8(&der_bytes[..]).expect("failed to parse rsa pubkey")
    };
}
pub(crate) static AUTHORITY_ECC_PUBKEY: &[u8] = b"\x04F\x06\\\xd6\xdc\xee8\xb8]N\xe3\xc8\x18\x13\x11\x83Z\x042\x82_w\xd2>%\xb8\xdd\x89\xddl\xf1\xfd\xb2g\xb7u\x11>\xd2\xed\xa2e\x1d1\xb7~.\xc3|\xea@6\x16\xec\xc1\xa6\x87\xe3J\x82z\x0e\xaf\xb4";

pub(crate) fn random_string(length: usize) -> String {
    let rand_string: String = thread_rng()
        .sample_iter(&Alphanumeric)
        .take(length)
        .collect();
    rand_string
}

pub(crate) fn rsa_enc_authority(pt: &[u8]) -> Result<Vec<u8>, Box<dyn Error>> {
    let mut rng = OsRng;
    let padding = PaddingScheme::new_oaep::<sha2::Sha256>();
    let ct = AUTHORITY_RSA_PUBKEY.encrypt(&mut rng, padding, &pt[..])?;
    Ok(ct)
}

pub(crate) fn aes_enc(key: &[u8], plaintext: &[u8]) -> Result<(Vec<u8>, Vec<u8>), Box<dyn Error>> {
    use aes::Aes128;
    use block_modes::block_padding::Pkcs7;
    use block_modes::{BlockMode, Cbc};

    type Aes128Cbc = Cbc<Aes128, Pkcs7>;

    let mut rng = OsRng;
    let iv: [u8; 16] = rng.gen();
    let iv = Vec::from(iv);
    let cipher = Aes128Cbc::new_var(key, &iv)?;

    let ciphertext = cipher.encrypt_vec(plaintext);
    Ok((iv, ciphertext))
}

pub(crate) fn ecdsa_verify(pubkey: &[u8], message: &[u8], signature: &[u8]) -> Result<(), Box<dyn Error>> {
    use ring::signature::{self, ECDSA_P256_SHA256_ASN1};
    // SECP256R1 curve
    let verif_algo = &ECDSA_P256_SHA256_ASN1;
    let peer_public_key = signature::UnparsedPublicKey::new(verif_algo, pubkey);

    peer_public_key.verify(message, signature)
        .map_err(|_| "Invalid signature and/or pubkey".into())
}

pub(crate) fn generate_user_id(user_name: &str) -> String {
    let mut rng = thread_rng();
    let uid = format!("{}_{:010}", &user_name, rng.gen::<u32>());
    uid
}

#[derive(Serialize, Deserialize)]
pub(crate) struct SignedData<T: Serialize> {
    pub(crate) data: T,
    signature: String,
    pub(crate) identity: Option<Box<SignedData<String>>>,
}

impl<T: Serialize> SignedData<T> {
    pub(crate) fn verify_signature(&self) -> Result<(), Box<dyn Error>> {
        let message = serde_json::to_vec(&self.data)?;
        let signature = base64::decode(&self.signature)?;
        let pubkey = match &self.identity {
            Some(v) => base64::decode(&v.data)?,
            None => AUTHORITY_ECC_PUBKEY.into(),
        };
        ecdsa_verify(&pubkey, &message, &signature)
    }
}
