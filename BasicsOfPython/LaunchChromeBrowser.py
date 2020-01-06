from selenium import webdriver

def OpenChromeBrowser(site_url):
    path = "C:\Python\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    driver.get(site_url)

#driver.quit() "http://www.google.com"

OpenChromeBrowser("http://www.google.com")

