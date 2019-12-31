import time
from selenium.webdriver import ChromeOptions, Chrome

executable_path = "C:\Python\chromedriver.exe"
driver = Chrome(executable_path=executable_path)
chrome_options=ChromeOptions()
chrome_options.add_argument("--headless")
base_url = "http://google.com"
driver.get(base_url)

links=driver.find_elements_by_tag_name('a')
print("number of links in browser are : "+str(len(links)))

for link in links:
    print(link.text)

print(links)
driver.close()
