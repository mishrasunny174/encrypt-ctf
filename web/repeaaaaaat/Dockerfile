FROM python:3

WORKDIR /usr/src/app

COPY app ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
COPY flag.txt /usr/src/app
RUN adduser repeat
RUN chmod 744 flag.txt
CMD su repeat -c "gunicorn -w 4 -b 0.0.0.0:8080 application:app"