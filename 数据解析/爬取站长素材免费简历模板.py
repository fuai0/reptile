import requests
from lxml import etree

url = "https://sc.chinaz.com/jianli/free.html"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41"
}

page_text = requests.get(url=url,headers=header)
page_text.encoding = "utf-8"

tree = etree.HTML(page_text.text)

div_list = tree.xpath("//div[@id='main']/div/div")

for div in div_list:
    div_url = div.xpath("./a/@href")[0]
    itr_page = requests.get(url=div_url,headers=header)
    itr_page.encoding = "utf-8"


    itr_tree = etree.HTML(itr_page.text)
    itr_name = itr_tree.xpath("//div[@class='bgwhite']/div[1]/h1/text()")[0]
    itr_down_url = itr_tree.xpath("//ul[@class='clearfix']/li[1]/a/@href")[0]

    itr_down = requests.get(url=itr_down_url,headers=header).content
    fp =open(f"免费简历模板/{itr_name}.rar","wb")
    fp.write(itr_down)
    print(f"{itr_name}已爬取完成！")





