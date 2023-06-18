import requests

url = "https://www.baidu.com/s?wd=ip"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41"
}
page_text = requests.get(url=url,headers=header)
page_text.encoding = "utf-8"
page_text = page_text.text

with open("wudaili.html","w",encoding="utf-8") as fp:
    fp.write(page_text)
    # ,proxies={"https":""}