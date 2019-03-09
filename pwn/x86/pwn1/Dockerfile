FROM ubuntu:14.04
RUN dpkg --add-architecture i386
RUN apt update
RUN apt --assume-yes dist-upgrade
RUN apt --assume-yes install socat build-essential libc6:i386 libncurses5:i386 libstdc++6:i386
RUN useradd -m pwn1
WORKDIR /home/pwn1
RUN chown -R root:pwn1 /home/pwn1
RUN chmod -R 755 /home/pwn1
COPY flag.txt pwn1 /home/pwn1/
CMD su pwn1 -c "socat -T10 TCP-LISTEN:4444,reuseaddr,fork EXEC:/home/pwn1/pwn1"
EXPOSE 4444
