from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
blue_button = driver.find_elements(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
blue_button = WebDriverWait (driver, 10).until(EC.element_to_be_clickable ((By.CSS_SELECTOR, 'button[class="btn btn-primary"]')))
sleep(5) 
blue_button.click()

sleep(5)

driver.quit()
