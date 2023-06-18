import json

import requests

def douban():
    url = "https://movie.douban.com/j/chart/top_list"
    param = {
        "type": "24",
        "interval_id": "100:90",
        "action":"",
        "start": "0",  # 第几部开始
        "limit": "100", # 总共抓取多少部
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41"
    }
    response = requests.get(url=url,params=param,headers=headers)
    list = response.json()
    fp = open("text/豆瓣喜剧排行.json","w",encoding="utf-8")
    json.dump(list,fp=fp,ensure_ascii=False)
    print("完成！")

douban()