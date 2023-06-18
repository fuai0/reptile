import requests
from lxml import etree
from multiprocessing.dummy import Pool

url = "https://www.pearvideo.com/panorama"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41"
}
page_text = requests.get(url=url,headers=header).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="listvideoListUl"]/li/div/a/@href')

#/html/body/div[2]/div[1]/div[1]/div[1]/div[1]/div/video
for li in li_list:
    li_url = "https://www.pearvideo.com/" + li
    data = {
        "contId": "1783549",
        "mrd": "0.33269057758802734",
    }
    li_text = requests.get(url=li_url,data=data,headers=header)
    print(li_text)


