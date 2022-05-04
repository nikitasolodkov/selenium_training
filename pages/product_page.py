from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_element_present(self, driver, *args):
        try:
            self.driver.find_element(*args)
            return True
        except NoSuchElementException:
            return False


    def add_product(self):
        quantity = self.driver.find_element(By.CSS_SELECTOR, 'span.quantity')  #
        current_quantity = str(quantity.get_property('innerText'))  #
        self.driver.find_element(By.XPATH, '// span[ @class ="quantity"][text()="' + current_quantity + '"]')  #

        quantity = self.driver.find_element(By.CSS_SELECTOR, 'span.quantity')
        current_quantity = str(quantity.get_property('innerText'))
        new_quantity = str(int(current_quantity) + 1)

        quantity = self.driver.find_element(By.CSS_SELECTOR, 'span.quantity')
        current_quantity = str(quantity.get_property('innerText'))
        new_quantity = str(int(current_quantity)+1)

        # 2) добавить его в корзину
        self.driver.find_element(By.NAME, 'add_cart_product').click()

        # 3) подождать, пока счётчик товаров в корзине обновится
        wait = WebDriverWait(self.driver, 10)  # seconds
        wait.until(EC.presence_of_element_located((By.XPATH, '// span[ @class ="quantity"][text()="' + new_quantity + '"]')))



    def size_select_check(self):
        if (self.is_element_present(self.driver, By.CSS_SELECTOR, "[name='options[Size]']")):
            select_element = self.driver.find_element(By.CSS_SELECTOR, "[name='options[Size]']")
            select_object = Select(select_element)
            select_object.select_by_visible_text('Small')

    def go_to_main_page(self):
        self.driver.find_element(By.CSS_SELECTOR, 'img[title=\'My Store\']').click()