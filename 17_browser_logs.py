import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import random


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def is_element_present(driver, *args):
  try:
    driver.find_element(*args)
    return True
  except NoSuchElementException:
    return False


# Задание 11. Сделайте сценарий регистрации пользователя

def test_browser_logs(driver):

    driver.get("http://localhost/litecart/admin/")
    driver.find_element(By.NAME, 'username').send_keys('admin')
    driver.find_element(By.NAME, 'password').send_keys('admin')
    driver.find_element(By.NAME, 'login').click()
    WebDriverWait(driver, 10).until(EC.title_contains('My Store'))

    driver.find_element(By.XPATH, "//span[text()='Catalog']").click()

# ОКТРЫВАЮ ВСЕ ПАПОЧКИ
    while is_element_present(driver, By.XPATH, '//td[i[@class ="fa fa-folder"]]/a'):
            closed_folder = driver.find_element(By.XPATH, '//td[i[@class ="fa fa-folder"]]/a')
            closed_folder.click()

    pro_ducks = driver.find_elements(By.XPATH, "//table[ @class =\"dataTable\"] //a[(contains( @ href, 'product')) and not ( @ title=\"Edit\")]")

    for i in range(len(pro_ducks)):
            pro_ducks = driver.find_elements(By.XPATH, "//table[ @class =\"dataTable\"] //a[(contains( @ href, 'product')) and not ( @ title=\"Edit\")]")
            pro_ducks[i].click()

# 3) последовательно открывать страницы товаров и проверять, не появляются ли в логе браузера сообщения(любого уровня)

# Я, ЧЕСТНО ГОВОРЯ, ИЗ УСЛОВИЯ МАЛО ЧТО ПОНЯЛ
# ПРОВЕРЯЮ, ЧТО НЕ ПОЯВИЛОСЬ НИКАКИХ СООБЩЕНИЙ ПРИ ПЕРЕХОДАХ

            assert (driver.get_log("browser") == [])

            driver.find_element(By.NAME, 'cancel').click()

            assert (driver.get_log("browser") == [])



