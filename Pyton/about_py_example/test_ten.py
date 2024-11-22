import requests
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

api_key = '5490b8926ca044d494971ccd6f0bca84'
url = f'https://api.spoonacular.com/recipes/findByIngredients'
params = {"apiKey": api_key, "ingredients": "apples"}

def test_get_from_api():
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        title = data[0].get("title")  
        return title
    else:
        print(f"Произошла ошибка при выполнении запроса. Код ошибки: {response.status_code}")

def test_insert():
    title = test_get_from_api()
    driver = webdriver.Chrome()  
    driver.get('https://erikdark.github.io/recept_api/')
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'ingredients'))
    )
    input_field.send_keys(title)
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
    WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.ID,'results')))
    assert not driver.find_element(By.ID,'results').is_displayed()
    
    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    test_insert()