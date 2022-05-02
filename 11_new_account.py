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

def test_new_account(driver):

    driver.get("http://localhost/litecart/admin/")
    driver.find_element(By.NAME, 'username').send_keys('admin')
    driver.find_element(By.NAME, 'password').send_keys('admin')
    driver.find_element(By.NAME, 'login').click()
    WebDriverWait(driver, 10).until(EC.title_contains('My Store'))

# ОТКЛЮЧАЕМ КАПЧУ
    driver.find_element(By.XPATH, '//span[text()="Settings"]').click()
    driver.find_element(By.XPATH, '//span[text()="Security"]').click()
    driver.find_element(By.XPATH, '//tr[td[text()="CAPTCHA"]]//a').click() # pencil
    driver.find_element(By.XPATH, '// label[text() = " False"] / input[ @ type = "radio"]').click()
    driver.find_element(By.XPATH, '//button[@name = "save"]').click()

# РАНДОМИЗИРУЕМ ЕМАИЛ
    r_number = random.randint(100000000000, 999999999999)
    email = 'solod' + str(r_number) + '@mail.ru'


    driver.get("http://localhost/litecart/en/")
    new_customer = driver.find_element(By.XPATH, '//a[text() = "New customers click here"]').click()

# ЗАПОЛНЯЕМ ФОРМУ
    driver.find_element(By.NAME, 'firstname').send_keys("Nikita")
    driver.find_element(By.NAME, 'lastname').send_keys("Solodkov")
    driver.find_element(By.NAME, 'address1').send_keys("Homeless")
    driver.find_element(By.NAME, 'postcode').send_keys("35808")
    driver.find_element(By.NAME, 'city').send_keys("Huntsville")

    driver.find_element(By.CSS_SELECTOR, '.select2-selection__arrow').click()
    driver.find_element(By.CSS_SELECTOR, '.select2-search__field').send_keys("United States")
    driver.find_element(By.CSS_SELECTOR, '.select2-search__field').send_keys(Keys.ENTER)

    driver.find_element(By.NAME, 'email').send_keys(email)
    driver.find_element(By.NAME, 'phone').send_keys('+12223334444')

    password = 'password'
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.NAME, 'confirmed_password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'button[type = "submit"]').send_keys(Keys.ENTER)

# ЛОГ АУТ
    driver.find_element(By.XPATH, '//aside//a[text() = "Logout"]').click()

# ЛОГ ИН
    driver.find_element(By.CSS_SELECTOR, 'input[name = \'email\']').send_keys(email)
    driver.find_element(By.CSS_SELECTOR, 'input[name = \'password\']').send_keys(password)

    driver.find_element(By.CSS_SELECTOR, 'button[name = \'login\']').click()

# ЛОГ АУТ
    driver.find_element(By.XPATH, '//aside//a[text() = "Logout"]').click()
