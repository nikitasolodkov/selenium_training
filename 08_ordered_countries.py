import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(firefox_binary='c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd



def is_element_present(driver, *args):
  try:
    driver.find_element(*args)
    return True
  except NoSuchElementException:
    return False


# ЗАДАНИЕ 08 СТРАНЫ В АЛФАВИТНОМ ПОРЯДКЕ

def test_ordered_countries(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element(By.NAME, 'username').send_keys('admin')
    driver.find_element(By.NAME, 'password').send_keys('admin')
    driver.find_element(By.NAME, 'login').click()
    WebDriverWait(driver, 10).until(EC.title_contains('My Store'))

# а) проверяет, что страны расположены в алфавитном порядке

    countries = driver.find_elements(By.CSS_SELECTOR, 'table.dataTable tr.row a:not([title])')
    original_list = []
    for country in countries:
        original_list.append(country.get_property('textContent'))

    ordered_list = original_list.copy()
    ordered_list.sort(reverse=False)
    assert (ordered_list == original_list)

# б) для тех стран, у которых количество зон отлично от нуля --
# открывает страницу этой страны и там проверяет, что геозоны расположены в алфавитном порядке



