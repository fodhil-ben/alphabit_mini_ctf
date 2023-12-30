FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y openssh-server sudo cron

RUN useradd -m -s /bin/bash ctf && \
    echo 'ctf:ctf' | chpasswd

WORKDIR /home/ctf

RUN chown -R root:root . && \
    chmod o+rx .

COPY challenge/flag.txt .
COPY challenge/sudoers /etc/sudoers

RUN chown root:root flag.txt && chmod 440 flag.txt

EXPOSE 22

ENTRYPOINT service ssh start \
    && tail -f /dev/null