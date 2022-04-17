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


# ЗАДАНИЕ 07 СТИКЕРЫ НА УТОЧКАХ

def test_products_stickers(driver):
    driver.get("http://localhost/litecart/")

    products = driver.find_elements(By.CSS_SELECTOR, '.product')
    for product in products:
        assert(is_element_present(product, By.CSS_SELECTOR, ".sticker"))

