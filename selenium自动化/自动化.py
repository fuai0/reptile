from selenium import webdriver
import time
bro = webdriver.Edge(executable_path="./msedgedriver.exe")
bro.get(url="https://www.bilibili.com/")
time.sleep(2)

# 回退
bro.back()
time.sleep(2)
# 前进
bro.forward()
time.sleep(2)

# 标签定位
search_input = bro.find_element_by_class_name("nav-search-input")

# 执行一组js操作
bro.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)

# 标签交互
search_input.send_keys("游戏")
btn = bro.find_element_by_class_name("nav-search-btn")
btn.click()