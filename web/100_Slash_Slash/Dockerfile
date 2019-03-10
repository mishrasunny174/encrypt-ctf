FROM python:3

WORKDIR /usr/src/app

COPY app ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
RUN export FLAG="encryptCTF{comments_&_indentations_makes_johnny_a_good_programmer}"
CMD gunicorn -w 4 -b 0.0.0.0:8080 application:app
