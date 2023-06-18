import requests
from lxml import etree

url = "https://xa.58.com/ershoufang/"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41"
}
page_text = requests.get(url=url,headers=header).text

tree = etree.HTML(page_text)
div_list = tree.xpath("//section[@class='list']/div")

fp = open("text/二手房.txt","a",encoding="utf-8")
for div in div_list:
    title = div.xpath("./a/div[2]/div[1]/div[@class='property-content-title']/h3/text()")[0]
    fp.write(str(title)+"\n")
