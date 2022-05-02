import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import random
import os

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


# Задание 12. Сделайте сценарий добавления товара

def test_new_product(driver):

    driver.get("http://localhost/litecart/admin/")
    driver.find_element(By.NAME, 'username').send_keys('admin')
    driver.find_element(By.NAME, 'password').send_keys('admin')
    driver.find_element(By.NAME, 'login').click()
    WebDriverWait(driver, 10).until(EC.title_contains('My Store'))

    driver.find_element(By.XPATH, '//span[text()="Catalog"]').click()
    driver.find_element(By.XPATH, '// a[text() = " Add New Product"]').click()



# GENERAL
    driver.find_element(By.CSS_SELECTOR, 'a[href = "#tab-general"]').click()

    driver.find_element(By.XPATH, '// label[text() = " Enabled"]').click()

# ------------------------------------------------ ИСПРАВЛЕНИЕ, РЕШИЛ ИСПОЛЬЗОВАТЬ УНИКАЛЬНОСТЬ ------------------------------------------------------------------

    r_number = random.randint(1000000000, 9999999999)
    dark_duck_name = 'DD' + str(r_number)

    driver.find_element(By.NAME, 'name[en]').send_keys(dark_duck_name)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------



    driver.find_element(By.NAME, 'code').send_keys('740')


    driver.find_element(By.CSS_SELECTOR, 'input[data-name = "Root"]').click()
    driver.find_element(By.CSS_SELECTOR, 'input[data-name = "Rubber Ducks"]').click()

    select_element = driver.find_element(By.CSS_SELECTOR, 'select[name = default_category_id]')
    select_object = Select(select_element)
    select_object.select_by_visible_text('Rubber Ducks')

    driver.find_element(By.XPATH, '//tr[td[text() = \'Unisex\']]//input').click()

    quantity = driver.find_element(By.NAME, 'quantity')
    quantity.clear()
    quantity.send_keys('100')

    select_element = driver.find_element(By.CSS_SELECTOR, 'select[name = sold_out_status_id]')
    select_object = Select(select_element)
    select_object.select_by_visible_text('Temporary sold out')


# ПОЛУЧАЮ АБСОЛЮТНЫЙ ПУТЬ ДО КАРТИНКИ (ДОЛЖНА ЛЕЖАТЬ В ОДНОЙ ПАПКЕ С ИСПОЛНЯЕМЫМ ФАЙЛОМ)
    script_name_py = os.path.basename(__file__) # Название скрипта с расширением .py
    project = os.path.abspath(script_name_py)
    project_folder = project.replace(script_name_py, '')
    image_path = project_folder + 'darkwing_duck.png'


    driver.find_element(By.NAME, 'new_images[]').send_keys(image_path)

    driver.find_element(By.NAME, 'date_valid_from').send_keys('10102020')
    driver.find_element(By.NAME, 'date_valid_to').send_keys('10102025')




# INFORMATION
    driver.find_element(By.CSS_SELECTOR, 'a[href = "#tab-information"]').click()
    time.sleep(1)
# ОЖИДАЮ
    select_element = driver.find_element(By.CSS_SELECTOR, 'select[name = manufacturer_id]')
    select_object = Select(select_element)
    select_object.select_by_visible_text('ACME Corp.')

    driver.find_element(By.NAME, 'keywords').send_keys('AbraCadabra')
    driver.find_element(By.NAME, 'short_description[en]').send_keys('AhalaiMahalai')

    description = driver.find_element(By.CSS_SELECTOR, "div.trumbowyg-editor")
    driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'Long Story Short'}", description)

    driver.find_element(By.NAME, 'head_title[en]').send_keys('Head Dark Duck')
    driver.find_element(By.NAME, 'meta_description[en]').send_keys('Meta Dark Duck')




# PRICES
    driver.find_element(By.CSS_SELECTOR, 'a[href = "#tab-prices"]').click()
    time.sleep(1)
# ОЖИДАЮ
    purchase_price = driver.find_element(By.NAME, 'purchase_price')
    purchase_price.clear()
    purchase_price.send_keys('199')

    select_element = driver.find_element(By.CSS_SELECTOR, 'select[name = purchase_price_currency_code]')
    select_object = Select(select_element)
    select_object.select_by_visible_text('US Dollars')

    driver.find_element(By.NAME, 'prices[USD]').send_keys('123.25')
    driver.find_element(By.NAME, 'prices[EUR]').send_keys('234.56')

    driver.find_element(By.NAME, 'save').click()



# ПРОВЕРКА НАЛИЧИЯ ЧЁРНОЙ УТОЧКИ

    # ------------------------------------------------ ИСПРАВЛЕНИЕ ------------------------------------------------------------------

    assert (is_element_present(driver, By.XPATH, '//a[text() = ' + dark_duck_name + ' ]'))

    # ------------------------------------------------ ИСПРАВЛЕНИЕ ------------------------------------------------------------------