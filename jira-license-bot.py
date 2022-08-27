import time
from datetime import datetime
import requests
import json


def getAllUnlicensedPlugins(Link, creds):
    r = requests.request(
        method="GET",
        url=Link + "rest/plugins/1.0/",
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + creds
            }
        )
    jsonLoaded = json.loads(r.text)
    return jsonLoaded["plugins"]


def parcePluginLink(Link, creds):
    r = requests.request(
        method="GET",
        url=Link,
        headers={
            'Content-Type': 'application/json',
            'Authorization':  'Basic ' + creds}
        )
    jsonLoaded = json.loads(r.text)
    return jsonLoaded

encodedCreds =
curTime=int(time.time())
baseLink = "https://helpdesk.dom.gosuslugi.ru/"

commonJson = getAllUnlicensedPlugins(baseLink, encodedCreds)

for plugin in commonJson:
    if plugin["userInstalled"]:
        pluginLink = baseLink + plugin["links"]["self"] + "/license"
        if 'expiryDate' not in parcePluginLink(pluginLink, encodedCreds):
            continue
        else:
            expTime = datetime.fromtimestamp(parcePluginLink(pluginLink, encodedCreds)["expiryDate"]/1000) - datetime.fromtimestamp(time.time())
            print(str(expTime.days) + " : " + plugin["name"])
