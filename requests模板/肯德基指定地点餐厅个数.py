import json
import requests

def kfc(str):
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    data= {
        "cname": "",
        "pid":"",
        "keyword": str,
        "pageIndex": "1",
        "pageSize": "10"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41"
    }
    response = requests.post(url=url,data=data,headers=headers)
    response = eval(response.text)
    print(response)

    fp = open(f"text/kfc_{str}.json","w",encoding="utf-8")
    json.dump(response,fp=fp,ensure_ascii=False)
    print("完成！")

str = input()
kfc(str)

# import requests
#
# url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
# # UA伪装
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
# }
# word = input("请输入地址: ")
# numbers = 1
# # 页数
# number_pages = 0
# # 第一次检测页数
# state = True
# while numbers != 0:
#     number_pages += 1
#     data = {
#         'cname': '',
#         'pid': '',
#         'keyword': word,
#         'pageIndex': number_pages,
#         'pageSize': '10',
#     }
#     response = requests.post(url=url, data=data, headers=header)
#     text = response.text
#     numbers -= 1
#     # 计算页数,因为只需要一次即可
#     if state:
#         # 将列表text转化为字典
#         dictionary = eval(text)
#         # 获取第一段Table的页数
#         rowcount = dictionary['Table']
#         # 将这个列表中的字典赋给dicts
#         dicts = rowcount[0]
#         # 查询rowcount所指的页数
#         numbers = dicts['rowcount']
#         if numbers == 0:
#             print("抱歉,您所输入的地址没有肯德基餐厅")
#         else:
#             print(f"{word}一共有{numbers}家肯德基餐厅")
#         if numbers % 10 == 0:
#             numbers = numbers // 10
#         else:
#             numbers = numbers // 10  # 不加一是因为已经检查过一次了
#         state = False
#
#     print(text)