from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://erikdark.github.io/QA_autotest_16/')


dynamic_element = (By.ID, 'price1')
WebDriverWait(driver, 5).until( EC.text_to_be_present_in_element(dynamic_element, '550')
) 
driver.find_element(By.ID, 'buyButton1').click()
message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'message1'))
    ).text
if message == 'Вы успешно купили автомобиль!':
        print('Хорошо!')
else:
        print('Что-то пошло не так.')

time.sleep (2)
driver.quit()



