FROM python:2

WORKDIR /usr/src/app

COPY server.py requirements.txt /usr/src/app/
RUN apt-get update --assume-yes
RUN apt-get dist-upgrade --assume-yes
RUN apt-get install --assume-yes socat
RUN pip install -r requirements.txt
EXPOSE 4444
CMD socat -T10 TCP-LISTEN:4444,reuseaddr,fork EXEC:"python -u /usr/src/app/server.py"