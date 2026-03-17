import allure
from playwright.sync_api import expect

from page.assertation.assertation import assert_equal_str


def test_successful_checkout(cart_page, catalog_page, product_cart):
    with allure.step('Получаем данные карточки, которую добавили в корзину'):
        title = catalog_page.get_title_product(product_cart).inner_text()
        description = catalog_page.get_description_products(product_cart).inner_text()
        price = catalog_page.get_price_products(product_cart).inner_text()
    cart_page.open_cart()
    with allure.step('Проверяем что данные карточки, соответствуют данным в корзине'):
        assert_equal_str(cart_page.get_title(), title)
        assert_equal_str(cart_page.get_description(), description)
        assert_equal_str(cart_page.get_price(), price)
    with allure.step('Нажимаем кнопку "Checkout"'):
        cart_page.click_btn_checkout()
        assert_equal_str('https://www.saucedemo.com/checkout-step-one.html', cart_page.page.url)
    with allure.step('Заполняем форму отправки'):
        cart_page.fill_first_name('Ivan')
        cart_page.fill_last_name('Gusev')
        cart_page.fill_postal_code('12345678')
        cart_page.click_btn_continue()
        assert_equal_str('https://www.saucedemo.com/checkout-step-two.html', cart_page.page.url)
    with allure.step('Подтверждаем заказ'):
        cart_page.click_btn_finish()
        assert_equal_str('https://www.saucedemo.com/checkout-complete.html', cart_page.page.url)
        assert_equal_str('Thank you for your order!', cart_page.get_complete_header_message())
        assert_equal_str('Your order has been dispatched, '
                         'and will arrive just as fast as the pony can get there!', cart_page.get_complete_description())

def test_checkout_without_fill_first_name(cart_page, catalog_page, product_cart):
    with allure.step('Получаем данные карточки, которую добавили в корзину'):
        title = catalog_page.get_title_product(product_cart).inner_text()
        description = catalog_page.get_description_products(product_cart).inner_text()
        price = catalog_page.get_price_products(product_cart).inner_text()
    cart_page.open_cart()
    with allure.step('Проверяем что данные карточки, соответствуют данным в корзине'):
        assert_equal_str(cart_page.get_title(), title)
        assert_equal_str(cart_page.get_description(), description)
        assert_equal_str(cart_page.get_price(), price)
    with allure.step('Нажимаем кнопку "Checkout"'):
        cart_page.click_btn_checkout()
    with allure.step('Заполняем поля кроме first name'):
        cart_page.fill_last_name('Gusev')
        cart_page.fill_postal_code('12345678')
        cart_page.click_btn_continue()
    with allure.step('Проверяем, что появилась ошибка'):
        input_first_name = cart_page.get_input_first_name()
        expect(input_first_name).to_contain_class('input_error')
        error_message = cart_page.get_error_message()
        assert_equal_str('Error: First Name is required', error_message)

def test_checkout_without_fill_last_name(cart_page, catalog_page, product_cart):
    with allure.step('Получаем данные карточки, которую добавили в корзину'):
        title = catalog_page.get_title_product(product_cart).inner_text()
        description = catalog_page.get_description_products(product_cart).inner_text()
        price = catalog_page.get_price_products(product_cart).inner_text()
    cart_page.open_cart()
    with allure.step('Проверяем что данные карточки, соответствуют данным в корзине'):
        assert_equal_str(cart_page.get_title(), title)
        assert_equal_str(cart_page.get_description(), description)
        assert_equal_str(cart_page.get_price(), price)
    with allure.step('Нажимаем кнопку "Checkout"'):
        cart_page.click_btn_checkout()
    with allure.step('Заполняем поля кроме first name'):
        cart_page.fill_first_name('Ivan')
        cart_page.fill_postal_code('12345678')
        cart_page.click_btn_continue()
    with allure.step('Проверяем, что появилась ошибка'):
        input_last_name = cart_page.get_input_last_name()
        expect(input_last_name).to_contain_class('input_error')
        error_message = cart_page.get_error_message()
        assert_equal_str('Error: Last Name is required', error_message)

def test_checkout_without_fill_postal_code(cart_page, catalog_page, product_cart):
    with allure.step('Получаем данные карточки, которую добавили в корзину'):
        title = catalog_page.get_title_product(product_cart).inner_text()
        description = catalog_page.get_description_products(product_cart).inner_text()
        price = catalog_page.get_price_products(product_cart).inner_text()
    cart_page.open_cart()
    with allure.step('Проверяем что данные карточки, соответствуют данным в корзине'):
        assert_equal_str(cart_page.get_title(), title)
        assert_equal_str(cart_page.get_description(), description)
        assert_equal_str(cart_page.get_price(), price)
    with allure.step('Нажимаем кнопку "Checkout"'):
        cart_page.click_btn_checkout()
    with allure.step('Заполняем поля кроме first name'):
        cart_page.fill_first_name('Ivan')
        cart_page.fill_last_name('Gusev')
        cart_page.click_btn_continue()
    with allure.step('Проверяем, что появилась ошибка'):
        input_postal_code = cart_page.get_input_postal_code()
        expect(input_postal_code).to_contain_class('input_error')
        error_message = cart_page.get_error_message()
        assert_equal_str('Error: Postal Code is required', error_message)

def test_cansel_checkout_step_one(cart_page, catalog_page, product_cart):
    with allure.step('Получаем данные карточки, которую добавили в корзину'):
        title = catalog_page.get_title_product(product_cart).inner_text()
        description = catalog_page.get_description_products(product_cart).inner_text()
        price = catalog_page.get_price_products(product_cart).inner_text()
    cart_page.open_cart()
    with allure.step('Проверяем что данные карточки, соответствуют данным в корзине'):
        assert_equal_str(cart_page.get_title(), title)
        assert_equal_str(cart_page.get_description(), description)
        assert_equal_str(cart_page.get_price(), price)
    with allure.step('Нажимаем кнопку "Checkout"'):
        cart_page.click_btn_checkout()
        assert_equal_str('https://www.saucedemo.com/checkout-step-one.html', cart_page.page.url)
    with allure.step('Отменяем оформление'):
        cart_page.click_btn_cancel()
        assert_equal_str('https://www.saucedemo.com/cart.html', cart_page.page.url)

def test_cansel_checkout_step_two(cart_page, catalog_page, product_cart):
    with allure.step('Получаем данные карточки, которую добавили в корзину'):
        title = catalog_page.get_title_product(product_cart).inner_text()
        description = catalog_page.get_description_products(product_cart).inner_text()
        price = catalog_page.get_price_products(product_cart).inner_text()
    cart_page.open_cart()
    with allure.step('Проверяем что данные карточки, соответствуют данным в корзине'):
        assert_equal_str(cart_page.get_title(), title)
        assert_equal_str(cart_page.get_description(), description)
        assert_equal_str(cart_page.get_price(), price)
    with allure.step('Нажимаем кнопку "Checkout"'):
        cart_page.click_btn_checkout()
        assert_equal_str('https://www.saucedemo.com/checkout-step-one.html', cart_page.page.url)
    with allure.step('Заполняем форму отправки'):
        cart_page.fill_first_name('Ivan')
        cart_page.fill_last_name('Gusev')
        cart_page.fill_postal_code('12345678')
        cart_page.click_btn_continue()
        assert_equal_str('https://www.saucedemo.com/checkout-step-two.html', cart_page.page.url)
    with allure.step('Отменяем оформление'):
        cart_page.click_btn_cancel()
        assert_equal_str('https://www.saucedemo.com/inventory.html', cart_page.page.url)