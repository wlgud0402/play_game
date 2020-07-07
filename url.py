from selenium import webdriver
from urllib import parse
import time

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.instagram.com/accounts/login/?hl=ko")
time.sleep(3)

print(driver.current_url)

