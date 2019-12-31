from selenium import webdriver

driver = webdriver.Chrome('C:\Python\chromedriver.exe')
driver.get("http://www.google.com")

"""X
from selenium import webdriver
driver = webdriver.Firefox("C:\Python\geckodriver.exe")
driver.get("http://www.google.com")
"""
driver.quit()

