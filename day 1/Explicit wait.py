from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# options=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,options_visible)))

mywait=WebDriverWait(driver,10) #explicit condition wait declaration
searchlink=mywait.until(EC.presence_of_element_located((By.XPATH,"give XPATH"))) #implementation of explicit wait(get element is not needed)
searchlink.click()

driver.quit()
