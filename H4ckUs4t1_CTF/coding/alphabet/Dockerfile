FROM rust:1.49

RUN useradd -m ctf
WORKDIR /home/ctf
COPY ./ ./
RUN cargo build --release

EXPOSE 7024 # change this to the port you want to expose

ENTRYPOINT ["/bin/sh", "-c", "socat TCP-LISTEN:7024,fork,reuseaddr EXEC:./target/release/alphabet"]
