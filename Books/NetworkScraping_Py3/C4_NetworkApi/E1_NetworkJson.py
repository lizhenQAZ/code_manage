import json
from urllib.request import urlopen


def getCountry(ipdddress):
    response = urlopen("http://freegeoip.net/json/"+ipdddress).read().decode('utf-8')
    responsejson = json.loads(response)
    return responsejson.get("country_code")

print(getCountry("50.78.253.58"))