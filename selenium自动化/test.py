from selenium import webdriver

# 实例化一个浏览器对象
bro = webdriver.Edge(executable_path="./msedgedriver.exe")
# 让浏览器发起一个指定url的请求
bro.get(url="https://www.baidu.com")
# 获取浏览器当前页面的源码数据
page_text = bro.page_source
print(page_text)
bro.quit()