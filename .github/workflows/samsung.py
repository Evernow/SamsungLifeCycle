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
            Device_Support[securitybranch['strong']['text']] = list(chain.from_iterable(devices))
    except:
        pass
import os
if os.path.exists("SamsungReleases.json"):
  os.remove("SamsungReleases.json")
with open('SamsungReleases.json', 'w') as fp:
    json.dump(Device_Support, fp, indent = 2)

print(Device_Support)