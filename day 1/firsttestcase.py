from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://inspiringlab.com.np/blogs/")
driver.maximize_window()
time.sleep(3)
page_height = driver.execute_script("return document.body.scrollHeight")
scroll_speed = 900
scroll_iteration = int(page_height / scroll_speed)

for _ in range(scroll_iteration):
    driver.execute_script(f"window.scrollBy(0, {scroll_speed})")
    time.sleep(3)
# Name = driver.find_element(*(By.NAME,"et_pb_contact_name_0")).send_keys("Evan")
# time.sleep(2)
# Email = driver.find_element(*(By.ID,"et_pb_contact_email_0")).send_keys("pradhanevan123@gmail.com")
# time.sleep(2)
# Phone = driver.find_element(*(By.ID,"et_pb_contact_phone_0")).send_keys("9812435465")
# time.sleep(2)
# Company = driver.find_element(*(By.ID,"et_pb_contact_company_0")).send_keys("Inspiring labs")
# time.sleep(2)
print("Code executed successfully")
driver.close()





