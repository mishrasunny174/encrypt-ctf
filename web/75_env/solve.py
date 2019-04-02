import requests
import time


host = "104.154.106.182"
port = '6060'

while True:
    response = requests.get('http://104.154.106.182:6060/whatsthetime/'+str(int(time.time())))
    if "404" not in response.content:
        print response.content
        break