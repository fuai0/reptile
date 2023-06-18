import json

import requests

str = input()
def baidu(str):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41"
    }
    post_url = "https://fanyi.baidu.com/sug"
    data = {
        "kw":str
    }
    reponse = requests.post(url=post_url,data=data,headers=headers)
    reponse_dic = reponse.json()
    fp = open(f"text/{str}.json","w",encoding="utf-8")
    json.dump(reponse_dic,fp=fp,ensure_ascii=False)
    print("爬取完成！")

baidu(str)