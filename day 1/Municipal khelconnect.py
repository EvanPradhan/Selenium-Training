from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://municipal-dev.khelconnect.com/login")
driver.maximize_window()
time.sleep(8)
Municipal = driver.find_element(*(By.NAME,"organizer_id"))
time.sleep(2)
options_visible=driver.find_element(*(By.XPATH,"//option[contains(text(), 'Kathmandu Municipality')]"))
# options=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,options_visible)))
options_visible.click()
time.sleep(5)
Username = driver.find_element(*(By.NAME, "username"))
Username.send_keys("organizer1")
time.sleep(2)
Password = driver.find_element(*(By.NAME,"password"))
Password.send_keys("Admin!123")
login = driver.find_element(*(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[2]/button"))
login.click()
time.sleep(9)
page_height = driver.execute_script("return document.body.scrollHeight")
scroll_speed = 900
scroll_iteration = int(page_height / scroll_speed)

for _ in range(scroll_iteration):
    driver.execute_script(f"window.scrollBy(0, {scroll_speed})")
    time.sleep(3)
driver.close()