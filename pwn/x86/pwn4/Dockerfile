FROM ubuntu:14.04
RUN dpkg --add-architecture i386
RUN apt update
RUN apt --assume-yes dist-upgrade
RUN apt --assume-yes install socat build-essential libc6:i386 libncurses5:i386 libstdc++6:i386
RUN useradd -m pwn4
WORKDIR /home/pwn4
RUN chown -R root:pwn4 /home/pwn4
RUN chmod -R 755 /home/pwn4
COPY flag.txt pwn4 /home/pwn4/
CMD su pwn4 -c "socat -T10 TCP-LISTEN:4444,reuseaddr,fork EXEC:/home/pwn4/pwn4"
EXPOSE 4444
