import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.get("https://inspiringlab.com.np/")
driver.maximize_window()

# 1) Using Link text
# driver.find_element(*(By.LINK_TEXT,"About Us")).click()

# 2) Partial Link text
# driver.find_element(*(By.PARTIAL_LINK_TEXT,"About")).click()

# 3) Find number of links in a page
links= driver.find_elements(*(By.TAG_NAME,"a"))
print("total no of links",len(links))

time.sleep(3)
driver.quit()