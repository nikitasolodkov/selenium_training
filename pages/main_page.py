from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By






class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/")
        return self

    def is_on_this_page(self):
        return len(self.driver.find_elements(By.XPATH, "//title[text()='Online Store | My Store']")) > 0

    def choose_first_product(self):
        self.driver.find_element(By.CSS_SELECTOR, 'li.product').click()
        return self

    def go_to_cart_page(self):
        self.driver.find_element(By.XPATH, '//a[text()=\'Checkout »\']').click()