import requests
from lxml import etree

url = "https://www.aqistudy.cn/historydata/"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41"}

page_text = requests.get(url=url,headers=header).text
tree = etree.HTML(page_text)


hot_list = tree.xpath("//div[@class='hot']//li")

fp = open("text/全国城市.txt","a",encoding="utf-8")
fp.write("热门城市:\n")
for li in hot_list:
    hot_city = li.xpath("./a/text()")[0]
    fp.write(hot_city+" ")


fp.write("\n"+"全部城市："+"\n")
all_city = tree.xpath("//div[@class='bottom']/ul/div[2]/li")

for li in all_city:
    all_city_name = li.xpath("./a/text()")[0]
    fp.write(all_city_name+" ")

