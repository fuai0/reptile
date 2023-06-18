from selenium import webdriver

bro = webdriver.Edge(executable_path="./msedgedriver.exe")
page_text = bro.get("")