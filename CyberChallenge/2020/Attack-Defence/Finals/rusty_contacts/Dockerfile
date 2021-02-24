
FROM rust as builder

RUN USER=root cargo new --bin rusty_contacts
WORKDIR ./rusty_contacts
COPY ./Cargo.toml ./Cargo.toml
RUN cargo build --release
RUN rm src/*.rs target/release/deps/rusty_contacts*

COPY ./src ./src
COPY setup.sql ./Cargo.toml ./Cargo.lock ./

RUN cargo build --release


FROM debian:buster-slim

ARG APP=/usr/src/app

RUN apt-get update \
    && apt-get install -y ca-certificates tzdata \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 1234

ENV TZ=Etc/UTC \
    APP_USER=appuser

RUN groupadd $APP_USER \
    && useradd -g $APP_USER $APP_USER \
    && mkdir -p ${APP}

COPY --from=builder /rusty_contacts/target/release/rusty_contacts ${APP}/rusty_contacts

RUN chown -R $APP_USER:$APP_USER ${APP}

USER $APP_USER
WORKDIR ${APP}

CMD ["./rusty_contacts"]