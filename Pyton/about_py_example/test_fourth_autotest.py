""" 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://erikdark.github.io/QA_autotest_stop_list/')

def test_insert_text():
    try:
        driver.find_element(By.ID,'inputField').send_keys('7218312')
        time.sleep(3)
        driver.find_element(By.ID,'submitButton').click()
        time.sleep(3)
        result = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID,'result')))
        result_in_string = result.text.strip()
        if '7218312' in result_in_string:
            assert 'Все хорошо'
        else:
            assert 'Все плохо'
    finally:
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    import pytest
    pytest.main() """

