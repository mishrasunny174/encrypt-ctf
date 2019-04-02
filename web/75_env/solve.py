import requests
import time


host = "104.154.106.182"
port = '6060'

while True:
    t = str(int(time.time()) + 1)
    print t
    response = requests.get('http://104.154.106.182:6060/whatsthetime/'+t)
    if "404" not in response.content:
        print response.content
        break