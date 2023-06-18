import requests
from lxml import etree

url = "https://pic.netbian.com/4kdongman/"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41"}
print("sss")
page_text = requests.get(url=url,headers=header).content

tree = etree.HTML(page_text)
li_list = tree.xpath("//ul[@class='clearfix']/li")

# for li in li_list:
#     img_name = li.xpath("./a/img/@alt")[0]
#     img_data = li.xpath("./a/img/@src")[0]
#     url1 = "https://pic.netbian.com"
#     img_url = url1+img_data
#     img = requests.get(img_url).content
#     fp = open(f"4k图片/{img_name}.jpg","wb")
#     fp.write(img)

for li in li_list:
    img_name = li.xpath("./a/img/@alt")[0]
    img_data = li.xpath("./a/@href")[0]
    url1 = "https://pic.netbian.com"
    img_page_url = url1+img_data
    page_text1 = requests.get(url=img_page_url,headers=header).content

    tree1 = etree.HTML(page_text1)
    img = tree1.xpath("//div[@class='photo-pic']/a/img/@src")[0]
    img_url = url1 + img
    img_data1 = requests.get(url=img_url,headers=header).content
    fp = open(f"4k图片/{img_name}.jpg","wb")
    fp.write(img_data1)
    print("成功")
