import time
from selenium.webdriver import ChromeOptions, Chrome

executable_path = "C:\Python\chromedriver.exe"
#driver = Chrome(executable_path=executable_path)

chrome_options = ChromeOptions()
chrome_options.add_argument("--headless")
driver = Chrome(executable_path=executable_path, chrome_options=chrome_options)


base_url = "https://freesearch.naukri.com/search/advSearch"
driver.get(base_url)

driver.find_element_by_class_name("tabsel").click()
#driver.find_element_by_class_name("tabUnsel").click()
#driver.find_element_by_link_text("/search/ezSearch").click()
#driver.find_element_by_link_text("/search/roleSearch").click()
print("home page title : " +driver.title)
print("current URL is : "+driver.current_url)
links=driver.find_elements_by_tag_name("a")
print("Total number of links in this page are : "+str(len(links)))
for link in links:
    print(link.text, link.get_attribute("href"))

any_of_the_keyword="Python"
driver.find_element_by_name("EZ_KEYWORD_ANY").send_keys(any_of_the_keyword)

min_expyr=4
driver.find_element_by_name("MIN_EXPYR").send_keys(min_expyr)

max_expyr=7
driver.find_element_by_name("MAX_EXPYR").send_keys(max_expyr)

driver.find_element_by_class_name("submitMain").click()

driver.quit()
