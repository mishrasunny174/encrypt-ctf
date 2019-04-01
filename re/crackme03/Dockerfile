FROM i386/ubuntu

RUN apt-get update
RUN apt-get --yes dist-upgrade
RUN apt-get --yes install socat
EXPOSE 4444
RUN useradd -m crackme03
RUN chown -R root:crackme03 /home/crackme03
RUN chmod -R 755 /home/crackme03
WORKDIR /home/crackme03
COPY flag.txt crackme03 /home/crackme03/
CMD su crackme03 -c "socat -T10 TCP-LISTEN:4444,reuseaddr,fork EXEC:/home/crackme03/crackme03"
