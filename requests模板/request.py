import requests

# 指定url
url = "https://www.sogou.com/"
# 发起请求
response = requests.get(url)
# 获取响应数据
page_text = response.text
print(page_text)
# 持久化存储数据
with open("text/sogou.html","w",encoding="utf-8") as fp:
    fp.write(page_text)
print("爬取成功！")