from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
for i in range(5):
    add_element_button=driver.find_element(By.CSS_SELECTOR,'button[onclick="addElement()"]')
    add_element_button.click()
delete_buttons=driver.find_elements(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
    
sleep (10)
print("Размер списка кнопок Delete:", len('delete_buttons'))
driver.quit()
