use crate::messages::ProximityMsg;
use std::sync::Arc;
use tokio::task::JoinHandle;
use tokio_postgres::{Client, Error, NoTls};

#[derive(Clone)]
pub(crate) struct DbHandle {
    client: Arc<Client>,
}

impl DbHandle {
    pub(crate) async fn new(url: &str) -> Result<(Self, JoinHandle<()>), Error> {
        let (client, connection) = tokio_postgres::connect(&url, NoTls).await?;

        let conn_hdl = tokio::spawn(async move {
            if let Err(e) = connection.await {
                log::error!("DB connection error: {}", e);
            }
        });

        client.batch_execute(include_str!("../setup.sql")).await?;

        Ok((DbHandle {client: Arc::new(client)}, conn_hdl))
    }

    pub(crate) async fn clean_old_data(&self) -> Result<(), Error> {
        let query = r#"DELETE FROM secrets
                              WHERE "timestamp" < (CURRENT_TIMESTAMP - interval '15 minutes')"#;
        self.client.query(query, &[]).await?;
        let query = r#"DELETE FROM proximity_msgs
                              WHERE "timestamp" < (CURRENT_TIMESTAMP - interval '15 minutes')"#;
        self.client.query(query, &[]).await?;
        Ok(())
    }

    pub(crate) async fn get_proximity_msgs(&self) -> Result<Vec<ProximityMsg>, Error> {
        let query = r#"SELECT userid, data_enc, data_iv, data_key_enc
                              FROM proximity_msgs
                              WHERE "timestamp" > (CURRENT_TIMESTAMP - interval '10 minutes')
                              ORDER BY "timestamp" desc"#;

        let rows = self.client.query(query, &[]).await?;

        let mut proximity = Vec::new();
        for row in rows {
            let userid = row.get(0);
            let data_enc = row.get(1);
            let data_iv = row.get(2);
            let data_key_enc = row.get(3);
            proximity.push(ProximityMsg {
                userid,
                data_enc,
                data_iv,
                data_key_enc,
            })
        }
        Ok(proximity)
    }

    pub(crate) async fn add_proximity_msgs(&self, msg: &ProximityMsg) -> Result<(), Error> {
        let query = r#"INSERT INTO proximity_msgs
                              (userid, data_enc, data_iv, data_key_enc)
                              values ($1, $2, $3, $4)"#;

        self.client.query(
            query,
            &[
                &msg.userid,
                &msg.data_enc,
                &msg.data_iv,
                &msg.data_key_enc,
            ],
        ).await?;
        Ok(())
    }

    pub(crate) async fn get_secrets(&self) -> Result<Vec<String>, Error> {
        let query = r#"SELECT secret
                              FROM secrets
                              WHERE "timestamp" > (CURRENT_TIMESTAMP - interval '10 minutes')
                              ORDER BY "timestamp" desc"#;

        let rows = self.client.query(query, &[]).await?;

        let mut secrets = Vec::new();
        for row in rows {
            let secret = row.get(0);
            secrets.push(secret);
        }
        Ok(secrets)
    }

    pub(crate) async fn get_latest_secret(&self) -> Option<(String, String)> {
        let query = r#"SELECT secret, userid
                              FROM secrets
                              ORDER BY "timestamp" desc
                              LIMIT 1
                              "#;

        self.client.query_one(query, &[]).await
            .map(|row| (row.get(0), row.get(1)))
            .ok()
    }

    pub(crate) async fn add_secret(&self, secret: &str, userid: &str) -> Result<(), Error> {
        let query = r#"INSERT INTO secrets
                              (secret, userid)
                              values ($1, $2)"#;

        self.client.query(query, &[&secret, &userid]).await?;
        Ok(())
    }
}
