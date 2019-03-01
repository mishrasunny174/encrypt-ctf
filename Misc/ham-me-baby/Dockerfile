FROM python:2-alpine

WORKDIR /usr/src/app

COPY hamming_code.py /usr/src/app
RUN apk add socat
EXPOSE 4444
CMD socat -T10 TCP-LISTEN:4444,reuseaddr,fork EXEC:"python -u /usr/src/app/hamming_code.py"
