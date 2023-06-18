from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service =  Service(executable_path="./msedgedriver.exe")
bro = webdriver.Edge(service=service)
bro.get("https://qzone.qq.com/")

bro.switch_to.frame("login_frame")
search = bro.find_element(By.ID,"switcher_plogin")
search.click()

user_name = bro.find_element(By.ID,"u")
user_code = bro.find_element(By.ID,"p")
user_name.send_keys("3439093274")
user_code.send_keys("20020715q...")

log = bro.find_element(By.ID,"login_button")
log.click()