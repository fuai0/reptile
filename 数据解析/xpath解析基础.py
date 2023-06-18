import lxml
from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')


entre = etree.parse("../requests模板/text/王怡.html",parser=parser)
print(entre)

import requests

str = input()

def url_quire(str):
    # UA伪装
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41"
    }

    url = "https://sogou.com/web"
    # 处理url参数，封装到字典中
    param = {"query":str}
    # 指定的url是带有参数的，并在请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)
    page_text = response.text
    soup = Soup(page_text,"lxml")
    print(soup)

url_quire(str)