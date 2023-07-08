import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/index.htm")
driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[1]/input').send_keys("jak")
driver.find_element(By.NAME, "password").send_keys("1234")
driver.find_element(By.XPATH, "//input[@class='button']").click()
act_title=driver.title
exp_title="ParaBank | Accounts Overview"
if act_title==exp_title:
    print("login successful")
else:
    print("login failed")
time.sleep(3)
driver.close()

