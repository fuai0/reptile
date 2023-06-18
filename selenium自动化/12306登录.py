from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

service =  Service(executable_path="./msedgedriver.exe")
bro = webdriver.Edge(service=service)
bro.get("https://kyfw.12306.cn/otn/resources/login.html")

user_name = bro.find_element(By.ID,"J-userName")
user_code = bro.find_element(By.ID,"J-password")
user_name.send_keys("18336886357")
user_code.send_keys("20020715q")
sleep(2)

log = bro.find_element(By.ID,"J-login")
log.click()
sleep(2)

action = ActionChains(bro)
div = bro.find_element(By.CLASS_NAME,"nc_iconfont")
action.click_and_hold(div)
action.move_by_offset(400,0)
action.perform()
action.release()

sleep(20)