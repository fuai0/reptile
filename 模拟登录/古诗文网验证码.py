import requests
from lxml import etree
from chaojiying import Chaojiying_Client

url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41"}

page_text = requests.get(url=url,headers=header).text
tree = etree.HTML(page_text)

pic_url = "https://so.gushiwen.cn"+tree.xpath("//*[@id='imgCode']/@src")[0]

pic_page_text = requests.get(url=pic_url,headers=header).content
with open("code.jpg","wb") as fp:
    fp.write(pic_page_text)

def getcode():
    chaojiying = Chaojiying_Client('wangziyi', '20020715q', '949720')
    im = open("code.jpg", 'rb').read()
    print(chaojiying.PostPic(im, 1902))

getcode()