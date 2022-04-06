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


def test_example(driver):
    driver.get("http://www.google.com/")
    driver.find_element(By.NAME, 'q').send_keys('webdriver')
    time.sleep(3)
    driver.find_element(By.NAME, 'btnK').click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.title_is('webdriver - Поиск в Google'))

