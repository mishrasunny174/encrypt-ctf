FROM i386/ubuntu

WORKDIR /root/
COPY flag.txt crackme02 /root/
RUN apt-get update
RUN apt-get --yes dist-upgrade
RUN apt-get --yes install socat
EXPOSE 4444
CMD socat -T10 TCP-LISTEN:4444,reuseaddr,fork EXEC:"/root/crackme02"
