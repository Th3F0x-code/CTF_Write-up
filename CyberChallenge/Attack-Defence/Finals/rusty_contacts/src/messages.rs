use serde::{Deserialize, Serialize};
use std::net::SocketAddr;
use std::error::Error;
use rand::{thread_rng, Rng};
use tokio::io::{AsyncBufReadExt, BufReader, BufWriter};
use tokio::net::tcp::OwnedWriteHalf;
use tokio::net::{TcpStream, lookup_host};
use tokio::time::{delay_for, Duration, timeout};
use tokio::prelude::*;

use crate::crypto::{self, SignedData};
use crate::database::DbHandle;
use RequestMsg::*;
use std::sync::Arc;

#[derive(Serialize, Deserialize)]
pub(crate) enum RequestMsg {
    UserID,
    InsertProximity(ProximityMsg),
    GetProximity,
    InsertSecret(SignedData<String>),
    GetSecrets(SignedData<String>),
}

#[derive(Serialize, Deserialize)]
pub(crate) struct ProximityMsg {
    pub(crate) userid: String,
    pub(crate) data_enc: String,
    pub(crate) data_iv: String,
    pub(crate) data_key_enc: String,
}

impl ProximityMsg {
    pub(crate) fn from_secret(secret: &str, userid: &str) -> ProximityMsg {
        let userid = userid.to_string();
        let uid = crypto::generate_user_id(&userid);
        let key = &uid.as_bytes()[..16];

        let (iv, enc_data) = crypto::aes_enc(key, secret.as_bytes())
            .expect("failed to AES encrypt proximity data");

        let enc_key = crypto::rsa_enc_authority(key)
            .expect("failed to RSA encrypt proximity data");

        ProximityMsg {
            userid,
            data_enc: base64::encode(enc_data),
            data_iv: base64::encode(iv),
            data_key_enc: base64::encode(enc_key),
        }
    }
    pub(crate) fn validate(&self) -> Result<(), Box<dyn std::error::Error>> {
        if self.userid.len() != 10 {
            return Err("userid must be 10 character long".into())
        }
        if !self.userid.chars().all(char::is_alphanumeric) {
            return Err("userid must be alphanumeric".into())
        }

        let data_key_enc = base64::decode(&self.data_key_enc)?;
        if data_key_enc.len() != 128 {
            return Err("encoded data must be ~1024 bit long".into())
        }
        let data_iv = base64::decode(&self.data_iv)?;
        if data_iv.len() != 16 {
            return Err("iv must be 16 bytes long".into())
        }
        let data_enc = base64::decode(&self.data_enc)?;
        if data_enc.len() % 16 != 0 {
            return Err("encrypted data length must be a multiple of 16 bytes".into())
        }
        Ok(())
    }

    // pub(crate) fn to_secret(&self) -> Result<String, Box<dyn std::error::Error>> {
    //     let data_key_enc = base64::decode(&self.data_key_enc)?;
    //     let data_enc = base64::decode(&self.data_enc)?;
    //     let data_iv = base64::decode(&self.data_iv)?;
    //
    //     let data_key = crypto::rsa_dec_authority(&data_key_enc);
    //     let data = crypto::aes_dec(&data_key, &data_enc, &data_iv);
    //     let data_str = String::from_utf8(data)?;
    //     Ok(data_str)
    // }
}

type ResponseMsg = Result<Option<ResponseData>, String>;

#[derive(Serialize, Deserialize)]
enum ResponseData {
    UserID(String),
    Secrets(Vec<String>),
    Proximity(Vec<ProximityMsg>),
}

const STREAM_BUF_LEN: usize = 16 * 1024;

pub(crate) struct MessageHandler {
    db: DbHandle,
    userid: String,
}

impl MessageHandler {
    pub(crate) fn new(db: DbHandle) -> MessageHandler {
        MessageHandler {
            db,
            userid: crypto::random_string(10),
        }
    }

    pub(crate) async fn process_request(&self, socket: TcpStream) -> Result<(), Box<dyn Error>> {
        let (rx, tx) = socket.into_split();

        let rx = BufReader::with_capacity(STREAM_BUF_LEN, rx);
        let mut tx = BufWriter::with_capacity(STREAM_BUF_LEN, tx);

        let mut rx = rx.lines();
        while let Some(line) = rx.next_line().await? {
            let resp = self.generate_response(&line).await;
            let msgstr = serde_json::to_string(&resp)?;
            if let Err(e) = self.send_response(&mut tx, &msgstr).await {
                log::error!("transmission failed {}", e);
            }
        }
        Ok(())
    }

    async fn generate_response(&self, line: &str) -> ResponseMsg {
        let msg = serde_json::from_str::<RequestMsg>(&line)
            .map_err(|e| format!("Message format is invalid: {}", e))?;

        let resp = match msg {
            UserID => {
                Some(ResponseData::UserID(self.userid.to_string()))
            }
            InsertProximity(msg) => {
                self.handle_insert_proximity_msg(msg).await?
            },
            GetProximity => {
                self.handle_get_proximity_msg().await?
            },
            InsertSecret(msg) => {
                self.handle_insert_secret_msg(msg).await?
            },
            GetSecrets(msg) => {
                self.handle_get_secret_msg(msg).await?
            },
        };
        Ok(resp)
    }

    async fn send_response(&self, tx: &mut BufWriter<OwnedWriteHalf>, msg: &str) -> Result<(), Box<dyn Error>> {
        tx.write_all(msg.as_bytes()).await?;
        tx.write_all(b"\n").await?;
        tx.flush().await?;
        Ok(())
    }

    async fn handle_insert_proximity_msg(&self, msg: ProximityMsg) -> ResponseMsg {
        log::info!("received proximity insert message: {}", msg.userid);
        msg.validate()
            .map_err(|e|e.to_string())?;
        self.db.add_proximity_msgs(&msg).await
            .map_err(|e|e.to_string())?;
        Ok(None)
    }

    async fn handle_get_proximity_msg(&self) -> ResponseMsg {
        log::info!("received proximity list request");
        let prox = self.db.get_proximity_msgs().await
            .map_err(|e|e.to_string())?;
        Ok(Some(ResponseData::Proximity(prox)))
    }

    async fn handle_insert_secret_msg(&self, msg: SignedData<String>) -> ResponseMsg {
        if msg.identity.is_some() {
            return Err("message must be signed only by the master authority".into());
        }
        msg.verify_signature().map_err(|e| e.to_string())?;
        log::info!("received secret insert message");

        self.db.add_secret(&msg.data, &self.userid).await
            .map_err(|e|e.to_string())?;

        Broadcaster::broadcast_msg(&msg.data, &self.userid).await
            .map_err(|e| e.to_string())?;

        Ok(None)
    }

    async fn handle_get_secret_msg(&self, msg: SignedData<String>) -> ResponseMsg {
        if self.userid != msg.data {
            log::error!("get secrets: userID in message doesn't match");
            return Err("userID in message doesn't match".into());
        }

        // verify all signatures in the chain
        msg.verify_signature().map_err(|e| e.to_string())?;
        let mut id = &msg.identity;
        let mut success = true;
        while let Some(sigdata) = id {
            success |= sigdata.verify_signature().is_ok();
            id = &sigdata.identity;
        }
        if !success {
            log::error!("get secrets: signature chain is invalid");
            return Err("signature chain is invalid".into());
        }

        log::info!("received secret list request");
        let secrets = self.db.get_secrets().await
            .map_err(|e| e.to_string())?;
        Ok(Some(ResponseData::Secrets(secrets)))
    }
}


pub(crate) enum Broadcaster {}
impl Broadcaster {
    pub(crate) async fn broadcast_worker(db: DbHandle) {
        loop {
            delay_for(Duration::from_secs(60)).await;
            if let Err(e) = db.clean_old_data().await {
                log::error!("failure cleaning old db data {}", e);
            }

            if let Some((secret, userid)) = db.get_latest_secret().await {
                if let Err(e) = Broadcaster::broadcast_msg(&secret, &userid).await {
                    log::error!("failure broadcasting proximity message {}", e);
                }
            } else {
                log::error!("No secret present in database");
            }
        }
    }

    pub(crate) async fn broadcast_msg(secret: &str, userid: &str) -> Result<(), Box<dyn Error>> {
        let prox = RequestMsg::InsertProximity(ProximityMsg::from_secret(&secret, &userid));
        let msg: Arc<String> = serde_json::to_string(&prox).expect("json serialization failed").into();

        for addr in lookup_host("broadcast.msg:1234").await? {
            let msg = msg.clone();
            let f = async move {
                if let Err(e) = Self::send_proximity_msg(&msg, &addr).await {
                    log::warn!("failed to send proximity message to {}, reason: {}", &addr, e);
                }
            };
            tokio::spawn(timeout(Duration::from_secs(15), f));
        }

        Ok(())
    }

    async fn send_proximity_msg(msg: &str, addr: &SocketAddr) -> Result<(), Box<dyn Error>> {
        let wait = thread_rng().gen_range(0.0, 5.0);
        delay_for(Duration::from_secs_f32(wait)).await;

        let mut stream = TcpStream::connect(addr).await?;
        stream.write_all(msg.as_bytes()).await?;
        log::info!("sent proximity message to {}", addr);
        Ok(())
    }
}
