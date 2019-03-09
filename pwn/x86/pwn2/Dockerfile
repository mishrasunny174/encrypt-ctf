FROM ubuntu:14.04
RUN dpkg --add-architecture i386
RUN apt update
RUN apt --assume-yes dist-upgrade
RUN apt --assume-yes install socat build-essential libc6:i386 libncurses5:i386 libstdc++6:i386
RUN useradd -m pwn2
WORKDIR /home/pwn2
RUN chown -R root:pwn2 /home/pwn2
RUN chmod -R 755 /home/pwn2
COPY flag.txt pwn2 /home/pwn2/
CMD su pwn2 -c "socat -T10 TCP-LISTEN:4444,reuseaddr,fork EXEC:/home/pwn2/pwn2"
EXPOSE 4444
