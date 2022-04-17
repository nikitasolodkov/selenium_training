import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver(request):
    # "C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
    # "c:\\Program Files (x86)\\Nightly\\firefox.exe"
    wd = webdriver.Firefox(firefox_binary='c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

# ЗАДАНИЕ 03 СЦЕНАРИЙ ЛОГИРОВАНИЯ
def test_login(driver):

    driver.get("http://localhost/litecart/admin/")
    driver.find_element(By.NAME, 'username').send_keys('admin')
    driver.find_element(By.NAME, 'password').send_keys('admin')
    driver.find_element(By.NAME, 'login').click()
    WebDriverWait(driver, 10).until(EC.title_contains('My Store'))
    print('Yes, the title contains "Template | My Store"')