import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import time

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

# Задание 13. Сделайте сценарий работы с корзиной


def test_cart_scenario(driver):

# 1) открыть главную страницу

        driver.get("http://localhost/litecart/")

        for i in range(3):

        # 2) открыть первый товар из списка

                driver.find_element(By.CSS_SELECTOR, 'li.product').click()


                quantity = driver.find_element(By.CSS_SELECTOR, 'span.quantity')
                current_quantity = str(quantity.get_property('innerText'))

                driver.find_element(By.XPATH, '// span[ @class ="quantity"][text()="' + current_quantity + '"]')


                if (is_element_present(driver, By.CSS_SELECTOR, "[name='options[Size]']")):

                    select_element = driver.find_element(By.CSS_SELECTOR, "[name='options[Size]']")
                    select_object = Select(select_element)
                    select_object.select_by_visible_text('Small')

                quantity = driver.find_element(By.CSS_SELECTOR, 'span.quantity')
                current_quantity = str(quantity.get_property('innerText'))
                new_quantity = str(int(current_quantity)+1)

        # 2) добавить его в корзину

                driver.find_element(By.NAME, 'add_cart_product').click()

        # 3) подождать, пока счётчик товаров в корзине обновится

                wait = WebDriverWait(driver, 10)  # seconds
                wait.until(EC.presence_of_element_located((By.XPATH, '// span[ @class ="quantity"][text()="' + new_quantity + '"]')))

        # 4) вернуться на главную страницу

                driver.find_element(By.CSS_SELECTOR, 'img[title=\'My Store\']').click()

# 5) открыть корзину (в правом верхнем углу кликнуть по ссылке Checkout)

        driver.find_element(By.XPATH, '//a[text()=\'Checkout »\']').click()


# 6) удалить все товары из корзины один за другим, после каждого удаления подождать, пока внизу обновится таблица

        while is_element_present(driver, By.NAME, 'remove_cart_item'):

                items = driver.find_elements(By.CSS_SELECTOR, 'tr td.item')

                driver.find_element(By.NAME, 'remove_cart_item').click()

                wait = WebDriverWait(driver, 10)  # seconds
                wait.until(EC.staleness_of(items[len(items)-1])) # ПРОВЕРЯЮ, ЧТО ПОСЛЕДНИЙ ЭЛЕМЕНТ МАССИВА ИСЧЕЗ





# my_store = driver.find_element(By.CSS_SELECTOR, 'img[alt = \'My Store\']') # - ДЕБАЖИЛСЯ, ПРОВЕРЯЛ РАБОТУ МЕТОДА
# wait.until(EC.staleness_of(my_store)) # - ДЕБАЖИЛСЯ, ПРОВЕРЯЛ РАБОТУ МЕТОДА
