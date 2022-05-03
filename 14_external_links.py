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

# Задание 14. Проверьте, что ссылки открываются в новом окне

def there_is_window_other_than(driver, old_windows):

        current_windows = driver.window_handles
        current_windows.sort()
        old_windows.sort()

        for i in range (len(old_windows)):

                if (current_windows[i] != old_windows[i]):
                        new_window = current_windows[i]
                        return new_window
                else:
                    current_windows.pop(i)
                    old_windows.pop(i)

        new_window = current_windows[-i]
        return new_window




def test_external_links(driver):

        driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
        driver.find_element(By.NAME, 'username').send_keys('admin')
        driver.find_element(By.NAME, 'password').send_keys('admin')
        driver.find_element(By.NAME, 'login').click()
        WebDriverWait(driver, 10).until(EC.title_contains('My Store'))

        driver.find_element(By.XPATH, '//a[text()=\'Afghanistan\']').click()

        external_links = driver.find_elements(By.CSS_SELECTOR, 'i.fa-external-link')

        for link in external_links:

                main_window = driver.current_window_handle
                old_windows = driver.window_handles
                link.click()

                wait = WebDriverWait(driver, 10)  # seconds
                wait.until(EC.new_window_is_opened(old_windows))

                new_window = there_is_window_other_than(driver, old_windows)
                driver.switch_to.window(new_window)

                assert not (is_element_present(driver, By.CSS_SELECTOR, "img[alt='My Store']"))
                driver.close()

                driver.switch_to.window(main_window)

                assert (is_element_present(driver, By.CSS_SELECTOR, "img[alt='My Store']"))

