from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.options import Options

edge_option = Options()
# 使用无头模式
edge_option.add_argument('--headless')
# 禁用GPU，防止无头模式出现莫名的BUG
edge_option.add_argument('--disable-gpu')

bro = webdriver.Edge(options=edge_option)
bro.get("https://www.baidu.com")

print(bro.title)
bro.quit()