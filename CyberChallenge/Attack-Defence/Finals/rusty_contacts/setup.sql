--DROP TABLE IF EXISTS proximity_msgs, secrets CASCADE;

CREATE TABLE IF NOT EXISTS proximity_msgs (
    userid         text,
    data_enc       text,
    data_iv        text,
    data_key_enc   text,
    "timestamp"    timestamptz DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS secrets (
    secret         text,
    userid         text,
    "timestamp"    timestamptz DEFAULT CURRENT_TIMESTAMP
);
