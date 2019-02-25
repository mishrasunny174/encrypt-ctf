FROM i386/ubuntu
RUN apt update
RUN apt --assume-yes dist-upgrade
RUN apt --assume-yes install socat
WORKDIR /root
COPY flag.txt pwn1 /root/
CMD socat -T10 TCP-LISTEN:4444,reuseaddr,fork EXEC:/root/pwn1
EXPOSE 4444
