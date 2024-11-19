""" import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')

def test_insert_correct():
    try:
        driver.find_element(By.ID,'openModalButton').click()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element(By.ID,'username').send_keys('testuser')
        time.sleep(1)
        driver.find_element(By.ID,'password').send_keys('password123')
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
    # Дождаться исчезновения модального окна
        WebDriverWait(driver, 10).until_not(EC.visibility_of_element_located((By.ID, 'loginModal')))
    # Убедиться, что модальное окно пропало
        if pytest.raises(NoSuchElementException):
            driver.find_element(By.CLASS_NAME, '.modal-content')
            print('Модальное окно успешно закрылось.')


    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    import pytest
    pytest.main() 
 """
