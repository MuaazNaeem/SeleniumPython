from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/HP/Downloads/automation/chromedriver")

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

time.sleep(2)
driver.close()
driver.quit()
print("Test completed.")