mod crypto;
mod database;
mod messages;

use crate::database::DbHandle;
use crate::messages::{MessageHandler, Broadcaster};
use tokio::net::TcpListener;
use tokio::time::{timeout, Duration};

async fn recv_loop(mut listener: TcpListener, db: DbHandle) {
    loop {
        match listener.accept().await {
            Err(e) => log::error!("couldn't create connection to client: {}", e),
            Ok((socket, _)) => {
                let msg_handle = MessageHandler::new(db.clone());
                tokio::spawn(async move {
                    if let Err(e) = timeout(Duration::from_secs(15), msg_handle.process_request(socket)).await {
                        log::error!("processing request: {}", e);
                    }
                });
            }
        }
    }
}

const DATABASE_CONFIG: &str = "host=pgdb user=rusty_contacts password=rusty_contacts";

#[tokio::main]
async fn main() {
    env_logger::builder()
        .filter_level(log::LevelFilter::Info)
        .init();

    let (db, conn_handler) = DbHandle::new(DATABASE_CONFIG).await
        .expect("failed to connect to database");

    let broadcaster_handle = tokio::spawn(Broadcaster::broadcast_worker(db.clone()));

    let listener = TcpListener::bind("0.0.0.0:1234").await
        .expect("could not bind socket");

    let main_loop = recv_loop(listener, db);

    tokio::select! {
        _ = main_loop => {
            log::error!("main loop panic");
        }
        _ = broadcaster_handle => {
            log::error!("broadcaster panic");
        }
        _ = conn_handler => {
            log::error!("db connection panic");
        }
    };
    panic!("some future panicked, check logs");
}
