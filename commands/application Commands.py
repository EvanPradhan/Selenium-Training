from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://inspiringlab.com.np/")
#get page title
print(driver.title)

#get current url
print(driver.current_url)

#get page source
print(driver.page_source)

driver.close()

