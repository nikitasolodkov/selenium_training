from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_element_present(self, driver, *args):
        try:
            self.driver.find_element(*args)
            return True
        except NoSuchElementException:
            return False


    def remove_all_products(self):
            while self.is_element_present(self.driver, By.NAME, 'remove_cart_item'):
                items = self.driver.find_elements(By.CSS_SELECTOR, 'tr td.item')
                self.driver.find_element(By.NAME, 'remove_cart_item').click()
                wait = WebDriverWait(self.driver, 10)  # seconds
                wait.until(EC.staleness_of(items[len(items) - 1]))  # ПРОВЕРЯЮ, ЧТО ПОСЛЕДНИЙ ЭЛЕМЕНТ МАССИВА ИСЧЕЗ