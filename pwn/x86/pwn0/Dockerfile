FROM ubuntu:14.04
RUN dpkg --add-architecture i386
RUN apt update
RUN apt --assume-yes dist-upgrade
RUN apt --assume-yes install socat build-essential libc6:i386 libncurses5:i386 libstdc++6:i386
RUN useradd -m pwn0
WORKDIR /home/pwn0
RUN chown -R root:pwn0 /home/pwn0
RUN chmod -R 755 /home/pwn0
COPY flag.txt pwn0 /home/pwn0/
CMD su pwn0 -c "socat -T10 TCP-LISTEN:4444,reuseaddr,fork EXEC:/home/pwn0/pwn0"
EXPOSE 4444
