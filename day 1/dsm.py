from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://dsm.inspiringlab.com.np/")
driver.implicitly_wait(10)
driver.maximize_window()
#time.sleep(8)
username = driver.find_element(*(By.XPATH,"/html/body/div/div[1]/div[1]/div/div/div/section[1]/div[1]/div[3]/div/div/div/div/div[3]/div/div[1]/div/input"))
username.send_keys("evan@inspiringlab.com.np")
time.sleep(3)
password = driver.find_element(*(By.XPATH,"/html/body/div/div[1]/div[1]/div/div/div/section[1]/div[1]/div[3]/div/div/div/div/div[4]/div/div[1]/div/input"))
password.send_keys("evan")
time.sleep(3)
login = driver.find_element(*(By.XPATH,"/html/body/div/div[1]/div[1]/div/div/div/section[1]/div[1]/div[3]/div/div/div/div/div[5]/div/button/div/p"))
login.click()
time.sleep(2)
work_history = driver.find_element(*(By.XPATH,"/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div/div[4]/div/div[1]/div/button[2]/div/p"))
work_history.click()
time.sleep(3)
driver.close()

