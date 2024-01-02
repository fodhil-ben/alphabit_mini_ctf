FROM ubuntu:22.04

FROM ubuntu:22.04

RUN dpkg --add-architecture i386 \
    && apt-get update \
    && apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 \
    && apt-get clean

RUN apt-get install -y socat 

RUN useradd ctf 

WORKDIR /challenge

COPY challenge .

RUN chown -R root:root .
RUN chmod +x chall entrypoint.sh

EXPOSE 1010

USER ctf

ENTRYPOINT [ "./entrypoint.sh" ]