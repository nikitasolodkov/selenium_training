import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import re

@pytest.fixture
def driver(request):
    wd = webdriver.Ie()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd




def is_element_present(driver, *args):
  try:
    driver.find_element(*args)
    return True
  except NoSuchElementException:
    return False


# Задание 10. Проверить, что открывается правильная страница товара

def properties_checks(duck, product_name, product_r_price, product_c_price):
        # a) текст названия товара

        if is_element_present(duck, By.CSS_SELECTOR, ".name"):
            name = duck.find_element(By.CSS_SELECTOR, '.name').get_property('textContent')
        else:
            name = duck.find_element(By.CSS_SELECTOR, '.title').get_property('textContent')

        assert (name == product_name)

        # б) цены(обычная и акционная)
        regular_price = duck.find_element(By.CSS_SELECTOR, '.regular-price').get_property('textContent')
        campaign_price = duck.find_element(By.CSS_SELECTOR, '.campaign-price').get_property('textContent')
        assert (regular_price == product_r_price)
        assert (campaign_price == product_c_price)

        # в) перечеркнутая (обычная)
        regular_color = duck.find_element(By.CSS_SELECTOR, '.regular-price').value_of_css_property("color")
        campaign_color = duck.find_element(By.CSS_SELECTOR, '.campaign-price').value_of_css_property("color")

        # в) цвет (обычная) ПРОВЕРКА СЕРОГО
        r, g, b = map(int, re.search(r'rgba\((\d+),\s*(\d+),\s*(\d+)', regular_color).groups())
        assert (r == g == b)

        regular_style = duck.find_element(By.CSS_SELECTOR, '.regular-price').value_of_css_property("text-decoration")
        assert (regular_style.startswith('line-through'))

        # г) ЖИРНАЯ ЛИ НОВАЯ ЦЕНА (BOLD вроде как - это больше или равно 700)
        campaign_font_weight = duck.find_element(By.CSS_SELECTOR, '.campaign-price').value_of_css_property("font-weight")
        assert (int(campaign_font_weight) >= 700)

        # г) цвет (акционная) ПРОВЕРКА КРАСНОГО
        r, g, b = map(int, re.search(r'rgba\((\d+),\s*(\d+),\s*(\d+)', campaign_color).groups())
        assert (g == b == 0)

        # д) акционная цена крупнее, чем обычная
        regular_font_size = duck.find_element(By.CSS_SELECTOR, '.regular-price').value_of_css_property("font-size")
        campaign_font_size = duck.find_element(By.CSS_SELECTOR, '.campaign-price').value_of_css_property("font-size")

# ------------------------------------------------ ИСПРАВЛЕНИЕ ПОСЛЕ ПОПЫТКИ 01 IE --------------------------------------------------------------------------------------

        regular_font_size = float(regular_font_size.replace('px', ''))
        campaign_font_size = float(campaign_font_size.replace('px', ''))

        assert (campaign_font_size > regular_font_size)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------




def test_correct_page(driver):
        driver.get("http://localhost/litecart/en/")

        # Первый продукт - Жёлтая уточка
        first_duck = driver.find_element(By.CSS_SELECTOR, '#box-campaigns li:first-child')

        # Имя и цены берём от первого товара
        product_name = first_duck.find_element(By.CSS_SELECTOR, '.name').get_property('textContent')
        product_r_price = first_duck.find_element(By.CSS_SELECTOR, '.regular-price').get_property('textContent')
        product_c_price = first_duck.find_element(By.CSS_SELECTOR, '.campaign-price').get_property('textContent')

        properties_checks(first_duck, product_name, product_r_price, product_c_price)

        first_duck.click()

        second_duck = driver.find_element(By.CSS_SELECTOR, '#box-product')
        properties_checks(second_duck, product_name, product_r_price, product_c_price)

