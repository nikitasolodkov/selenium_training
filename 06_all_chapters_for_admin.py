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


# ЗАДАНИЕ 06 Сделайте сценарий, проходящий по всем разделам админки

def test_all_chapters_admin(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element(By.NAME, 'username').send_keys('admin')
    driver.find_element(By.NAME, 'password').send_keys('admin')
    driver.find_element(By.NAME, 'login').click()
    WebDriverWait(driver, 10).until(EC.title_contains('My Store'))

   # element = driver.find_element(By.XPATH, '// ul[ @ id = "box-apps-menu"] / li // * [text() = "Catalog"]')

    box_apps_menu = driver.find_element(By.XPATH, '// ul[ @ id = "box-apps-menu"]')

    sections = box_apps_menu.find_elements(By.XPATH, '// ul[ @ id = "box-apps-menu"]/li')
    for x in range(0, len(sections)):

        box_apps_menu = driver.find_element(By.XPATH, '// ul[ @ id = "box-apps-menu"]')

        # РАЗДЕЛЫ
        sections = box_apps_menu.find_elements(By.XPATH, '// ul[ @ id = "box-apps-menu"]/li') # РАЗДЕЛЫ
        section = sections[x] # КОНКРЕТНЫЙ РАЗДЕЛ
        if section.is_displayed():
            section.click()
            # time.sleep(1)

            # САМА ПРОВЕРКА НАЛИЧИЯ h1 - FAST FAIL
            assert (is_element_present(driver, By.CSS_SELECTOR, "h1"))

            # ПОДРАЗДЕЛЫ
            subsections = driver.find_elements(By.XPATH, '//ul[@id="box-apps-menu"]/li/ul/li')
            for y in range(0, len(subsections)):

                subsections = driver.find_elements(By.XPATH, '//ul[@id="box-apps-menu"]/li/ul/li')
                subsection = subsections[y]

                subsection.click()
                # time.sleep(1)

                # САМА ПРОВЕРКА НАЛИЧИЯ h1 - FAST FAIL
                assert(is_element_present(driver, By.CSS_SELECTOR, "h1"))


