""" import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

driver = webdriver.Chrome()
driver.get('https://erikdark.github.io/PyTest_01_reg_form/')

def test_registration_form():
    try:
        driver.find_element(By.ID,'text').send_keys('zsadfszdfg')
        driver.find_element(By.ID,'password').send_keys('7218312')
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        result   = re.match(pattern,'example@mail.ru')
        driver.find_element(By.ID,'email').send_keys(result)
        driver.find_element(By.ID,'submit').click()
    
    finally:
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    import pytest
    pytest.main() """
