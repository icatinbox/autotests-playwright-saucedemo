import allure


def test_successful_checkout(cart_page, catalog_page, product_cart):
    cart_page.open_cart()
    with allure.step('Получаем данные карточки, которую добавили в корзину'):
        title = catalog_page.get_title_product(product_cart).inner_text()
        description = catalog_page.get_description_products(product_cart).inner_text()
        price = catalog_page.get_price_products(product_cart).inner_text()
    with allure.step('Проверяем что данные карточки, соответствуют данным в корзине'):
        assert cart_page.get_title() == title
        assert cart_page.get_description() == description
        assert cart_page.get_price() == price
    with allure.step('Нажимаем кнопку "Checkout"'):
        cart_page.click_btn_checkout()
    with allure.step('Заполняем форму отправки'):
        cart_page.fill_first_name('Ivan')
        cart_page.fill_last_name('Gusev')
        cart_page.fill_postal_code('12345678')
        cart_page.click_btn_continue()
    with allure.step('Подтверждаем заказ'):
        cart_page.click_btn_finish()
        assert cart_page.get_complete_header_message() == 'Thank you for your order!'
        assert cart_page.get_complete_description() == ('Your order has been dispatched, '
                                                        'and will arrive just as fast as the pony can get there!')