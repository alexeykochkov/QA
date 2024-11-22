import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://openweathermap.org/')

def test_get_euro():
    try:
        driver.find_element(By.XPATH, "//input[@placeholder='Search city']").send_keys('Moscow')
        
    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    import pytest
    pytest.main() 




