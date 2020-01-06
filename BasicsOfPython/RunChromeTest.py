from selenium import webdriver
import time

executable_path = "C:\Python\chromedriver.exe"
driver = webdriver.Chrome(executable_path=executable_path)
driver.get("Http://google.com")
time.sleep(100)
driver.close()
