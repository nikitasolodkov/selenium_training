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


# Задание 9. Проверить сортировку геозон на странице геозон

def test_ordered_geo_zones(driver):
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
        driver.find_element(By.NAME, 'username').send_keys('admin')
        driver.find_element(By.NAME, 'password').send_keys('admin')
        driver.find_element(By.NAME, 'login').click()
        WebDriverWait(driver, 10).until(EC.title_contains('My Store'))

        geo_zones = driver.find_elements(By.CSS_SELECTOR, 'tbody tr.row a:not([title])')

        for x in range(len(geo_zones)):

            geo_zones = driver.find_elements(By.CSS_SELECTOR, 'tbody tr.row a:not([title])')
            geo_zone = geo_zones[x]
            geo_zone.click()


            zones = driver.find_elements(By.XPATH, '// select[contains(@name, "][zone_code]")]/option[@selected="selected"]')
            original_list = []
            for zone in zones:
                original_list.append(zone.get_property('textContent'))

            ordered_list = original_list.copy()
            ordered_list.sort(reverse=False)
            assert (ordered_list == original_list)

            cancel = driver.find_element(By.CSS_SELECTOR, "button[name = 'cancel']")
            cancel.click()








