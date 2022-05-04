from pages.product_page import ProductPage
from pages.main_page import MainPage
from pages.cart_page import CartPage

# Задание 19 Page Object Model

def test_page_object_model(driver):

        main_page = MainPage(driver)
        main_page.open() # 1) открыть главную страницу

        for i in range(3):
                main_page.is_on_this_page()
                main_page.choose_first_product() # 2) открыть первый товар из списка

                product_page = ProductPage(driver)
                product_page.size_select_check()
                product_page.add_product()
                product_page.go_to_main_page() # 4) вернуться на главную страницу

        main_page.go_to_cart_page() # 5) открыть корзину (в правом верхнем углу кликнуть по ссылке Checkout)

        cart_page = CartPage(driver)
        cart_page.remove_all_products() # 6) удалить все товары из корзины один за другим, после каждого удаления подождать, пока внизу обновится таблица

