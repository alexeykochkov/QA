import requests
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

API_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = '1716b91f56f380231d3e3325e096413e'

@pytest.fixture
def api_params():
    return {
        "q": "Moscow",
        "appid": API_KEY,
        "units": "metric",
        "lang": "ru"
    }

def test_status_code(api_params):
    response = requests.get(API_URL,params=api_params)
    assert response.status_code == 200

def test_temperature(api_params):
    response = requests.get(API_URL,params=api_params)
    data = response.json()
    assert "main" in data
    assert "temp" in data["main"]

def test_weather_description_field(api_params):
    response = requests.get(API_URL,params=api_params)
    data = response.json()
    assert "weather" in data
    assert len(data["weather"]) >0
    assert "description" in data["weather"][0]

''' Надо изменить название города и поменять != на =='''
def test_fakecity (api_params):
    response = requests.get(API_URL,params=api_params)
    data = response.json()
    assert response.status_code != 404 

def test_go_to_site():
    driver = webdriver.Chrome()  
    driver.get('https://openweathermap.org/')
    keys = 'Moscow'
    driver.find_element(By.XPATH, "//input[@placeholder='Search city']").send_keys(keys)
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.search-dropdown-menu li:nth-child(3)'))).click()
    town = WebDriverWait(driver,2).until(EC.visibility_of_element_located((By.TAG_NAME,'h2'))).text
    split = town.split()
    correct_town = split[0]
    assert keys == correct_town

def test_fake_city_in_site():



    time.sleep(2)
    driver.quit()    