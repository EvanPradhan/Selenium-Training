import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.implicitly_wait(10)

# # 1) select specific checkbox
# driver.find_element(*(By.XPATH,"//label[@for='gender-radio-1']")).click()
# time.sleep(3)

# 2) Print number of checkboxes)
checkboxes = driver.find_elements(*(By.XPATH,"//label[contains(@for,'hobbies')]"))
print(len(checkboxes))

#3) select all the checkboxes from 2
for checkbox in checkboxes:
    checkbox.click()
    time.sleep(5)

# 4) select last two checkboxes
# for i in range(len(checkboxes)-2,len(checkboxes)):  #range(3-2,3)-->2,3  jati ota last ko select garne, teti minus garne
#     checkboxes[i].click()
#     time.sleep(3)

# #5) Select first 2 checkbox
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()
#         time.sleep(3)

# 6) clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
driver.quit()
