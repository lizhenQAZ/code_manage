# coding: utf-8
from xml.dom.minidom import parseString
import requests


def ParseDom():
    page = requests.get("http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName=58367")
    lines = page.text
    dom = parseString(lines)
    strings = dom.getElementsByTagName("string")
    for string in strings:
        print(string.childNodes[0].data)

if __name__ == '__main__':
    ParseDom()
