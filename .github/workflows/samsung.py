import requests
from bs4 import BeautifulSoup
from itertools import chain
from bs2json import bs2json
import json
r = requests.get("https://security.samsungmobile.com/workScope.smsb")
soup=BeautifulSoup(r.text,'html.parser')
tags = soup.find_all(class_="txt_section")
converter = bs2json()
Device_Support = {}

for securitybranch in converter.convertAll(tags,join=True)[0]['div']:
    try:
        devices = []
        for device in securitybranch['ul']['li']:
            devices.append(device['text'].split(','))
        # print(securitybranch['strong']['text'])
        # print(devices)
        if 'Disclaimer' not in securitybranch['strong']['text']:
            devices = sorted([s.strip() for s in  list(chain.from_iterable(devices))])
            Device_Support[securitybranch['strong']['text']] = devices
    except:
        pass
import os
if os.path.exists("SamsungReleases.json"):
  os.remove("SamsungReleases.json")
with open('SamsungReleases.json', 'w') as fp:
    json.dump(Device_Support, fp, indent = 2)
import waybackpy

url = "https://security.samsungmobile.com/workScope.smsb" 
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"


wayback = waybackpy.Url(url, user_agent) 
archive = wayback.save() 
print(archive.archive_url) 


print(Device_Support)
