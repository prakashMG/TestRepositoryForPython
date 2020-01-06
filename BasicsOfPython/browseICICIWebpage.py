import time

from selenium.webdriver import ChromeOptions, Chrome

path = "C:\Python\chromedriver.exe"
# in win u must give chromedriver.exe
# webdriver.Firefox(executable_path=path)
chrome_options = ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--headless")

driver = Chrome(executable_path=path, options=chrome_options)
baseUrl = "https://www.icicibank.com/"
driver.get(baseUrl)
print("driver initiated")
# driver.find_element_by_class_name("pl-login-ornage-box").click()
time.sleep(3)
driver.close()
