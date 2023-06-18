import requests
from bs4 import BeautifulSoup as Soup
import lxml

url = "http://www.kulemi.com/zt/127"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41"
}
page_text = requests.get(url=url,headers=header).content
soup = Soup(page_text,'lxml')
li_list = soup.select(".catalog > li")

for li in li_list:
    title = li.a.text
    htm = li.a["href"]
    chapter = requests.get(url=htm,headers=header).content
    soup1 = Soup(chapter,"lxml")
    div_tag = soup1.find("div",class_="chapter-content")
    fp = open(f"三国演义/{title}","w",encoding="utf-8")
    fp.write(div_tag.text)
    print(f"{title}已完成爬虫！")