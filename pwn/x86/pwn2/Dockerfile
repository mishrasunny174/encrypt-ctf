FROM ubuntu:14.04
RUN dpkg --add-architecture i386
RUN apt update
RUN apt --assume-yes dist-upgrade
RUN apt --assume-yes install socat build-essential libc6:i386 libncurses5:i386 libstdc++6:i386
WORKDIR /root
COPY flag.txt pwn2 /root/
CMD socat -T10 TCP-LISTEN:4444,reuseaddr,fork EXEC:/root/pwn2
EXPOSE 4444
