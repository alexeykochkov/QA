""" import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_result_column(browser):
    url = 'https://erikdark.github.io/zachet_selenium_01/index.html'
    browser.get(url)

    # Переход на страницу с таблицей
    link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="table.html"]'))
    )
    link.click()

    # Ожидаем загрузки таблицы
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'data-table'))
    )

    # Поиск таблицы и извлечение данных
    table = browser.find_element(By.ID, 'data-table')
    rows = table.find_elements(By.TAG_NAME, 'tr')[1:]  # Исключаем заголовок

    names_dict = {}
    ages_dict = {}
    cities_dict = {}

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        name = cells[0].text
        age = cells[1].text
        city = cells[2].text
        names_dict[name] = True
        ages_dict[age] = True
        cities_dict[city] = True
 
    # Проверка результата
    assert len(names_dict) == 3  # Проверяем количество уникальных имен
    assert list(names_dict.keys()) == ['Анна', 'Иван', 'Мария']  # Проверяем сами имена
    assert len(ages_dict) == 3  # Проверяем количество уникальных возрастов
    assert list(map(int, ages_dict.keys())) == [25, 30, 22]  # Проверяем сами возрасты
    assert len(cities_dict) == 3  # Проверяем количество уникальных городов
    assert list(cities_dict.keys()) == ['Москва', 'Санкт-Петербург', 'Новосибирск']  # Проверяем сами города

if __name__ == '__main__':
    pytest.main(['-v']) """