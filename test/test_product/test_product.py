import allure
from playwright.sync_api import expect

from page.assertation.assertation import assert_equal_str
from utils.utils import attach_allure_text


def test_add_to_cart(catalog_page, cart_page):
    catalog_page.open_catalog_page()
    with allure.step('Получаем рандомную карточку и элементы внутри карточки'):
        card = catalog_page.random_product()
        btn_add_to_card = catalog_page.get_btn_add_to_cart(card)
        title = catalog_page.get_title_product(card).inner_text()
        description = catalog_page.get_description_products(card).inner_text()
        price = catalog_page.get_price_products(card).inner_text()
        title_attr_format = title.lower().replace(' ', '-')
    with allure.step('Собираем атрибуты кнопок'):
        attribute_btn_add = f'add-to-cart-{title_attr_format}'
        attribute_btn_remove = f'remove-{title_attr_format}'
        attach_allure_text('full attribute', f'attribute_btn_add: {attribute_btn_add},'
                                             f' attribute_btn_remove: {attribute_btn_remove}')
    with allure.step('Проверяем, что кнопка add to cart содержит атрибут name'):
        expect(btn_add_to_card).to_have_attribute('name', attribute_btn_add)
    with allure.step('Клик на кнопку add to cart'):
        catalog_page.add_to_cart(btn_add_to_card)
    with allure.step('Проверяем, что у иконки корзины появился каунтер'):
        badge = catalog_page.get_badge_count_cart()
        expect(badge).to_be_visible()
        assert_equal_str('1', badge.inner_text())
    with allure.step('Проверяем, что кнопка remove содержит атрибут name'):
        btn_remove = catalog_page.get_btn_remove_from_cart(card)
        expect(btn_remove).to_have_attribute('name', attribute_btn_remove)
    with allure.step('Проверяем, что предмет отображается в корзине'):
        cart_page.open_cart()
        assert_equal_str(cart_page.get_title(), title)
        assert_equal_str(cart_page.get_description(), description)
        assert_equal_str(cart_page.get_price(), price)

def test_remove_from_cart(catalog_page):
    catalog_page.open_catalog_page()
    with allure.step('Получаем рандомную карточку и элементы внутри карточки'):
        card = catalog_page.random_product()
        btn_add_to_card = catalog_page.get_btn_add_to_cart(card)
        title_attr_format = catalog_page.get_title_product(card).inner_text().lower().replace(' ', '-')
    with allure.step('Собираем атрибуты кнопок'):
        attribute_btn_add = f'add-to-cart-{title_attr_format}'
        attribute_btn_remove = f'remove-{title_attr_format}'
        attach_allure_text('full attribute', f'attribute_btn_add: {attribute_btn_add},'
                                             f' attribute_btn_remove: {attribute_btn_remove}')
    with allure.step('Проверяем, что кнопка add to cart содержит атрибут name'):
        expect(btn_add_to_card).to_have_attribute('name', attribute_btn_add)
    with allure.step('Клик на кнопку add to cart'):
        catalog_page.add_to_cart(btn_add_to_card)
    with allure.step('Проверяем, что у иконки корзины появился каунтер'):
        badge = catalog_page.get_badge_count_cart()
        expect(badge).to_be_visible()
        assert_equal_str('1', badge.inner_text())
    with allure.step('Проверяем, что кнопка remove содержит атрибут name'):
        btn_remove = catalog_page.get_btn_remove_from_cart(card)
        expect(btn_remove).to_have_attribute('name', attribute_btn_remove)
    with allure.step('Клик на кнопку remove'):
        catalog_page.remove_from_cart(btn_remove)
        expect(btn_add_to_card).to_have_attribute('name', attribute_btn_add)
    with allure.step('Проверяем, что у иконки корзины пропал каунтер'):
        badge = catalog_page.get_badge_count_cart()
        expect(badge).not_to_be_visible()

def test_open_detail_product_page_by_click_title(catalog_page, detail_product_page):
    catalog_page.open_catalog_page()
    with allure.step('Получаем рандомную карточку и элементы внутри карточки'):
        card = catalog_page.random_product()
        link_title = catalog_page.get_link_title(card)
        title = catalog_page.get_title_product(card).inner_text()
        price = catalog_page.get_price_products(card).inner_text()
        description = catalog_page.get_description_products(card).inner_text()

    with allure.step('Получаем атрибут, который содержит id карточки'):
        attr_id = link_title.get_attribute('id')
        attach_allure_text('attr_id', str(attr_id))

    with allure.step('Выбираем только цифры(id) из атрибута карточки'):
        id_product = filter(lambda num: num.isdigit(), attr_id)
        attach_allure_text('list nums(id)', str(id_product))

    with allure.step('Кликаем на название'):
        catalog_page.click_title_product(link_title)

    with allure.step('Проверяем, что url соответствует'):
        assert_equal_str(catalog_page.page.url, f'https://www.saucedemo.com/inventory-item.html?id={''.join(id_product)}')

    with allure.step('Получаем данные с детальной страницы товара'):
        detail_title = detail_product_page.get_title_products().inner_text()
        detail_desc = detail_product_page.get_description_products().inner_text()
        detail_price = detail_product_page.get_price_products().inner_text()

    with allure.step('Проверяем одинаковые ли данные на карточке товара и детальной странице'):
        assert_equal_str(title, detail_title)
        assert_equal_str(price, detail_price)
        assert_equal_str(description, detail_desc)

def test_sort_name_z_to_a(catalog_page):
    catalog_page.open_catalog_page()
    with allure.step('Получаем список названий карточек'):
        old_sort_titles = catalog_page.get_list_title_products()
    with allure.step('Сортируем список от Z до A(по убыванию)'):
        catalog_page.select_sort('za')
        new_sort_titles = catalog_page.get_list_title_products()
    with allure.step('Проверяем, что выбрано значение z-a в селекте'):
        assert_equal_str('Name (Z to A)', catalog_page.get_active_select().inner_text())
    with allure.step('Проверяем, что старая сортировка != новой)'):
        assert old_sort_titles != new_sort_titles
        assert sorted(old_sort_titles, reverse=True) == new_sort_titles

def test_default_sort_name_a_to_z(catalog_page):
    catalog_page.open_catalog_page()
    with allure.step('Получаем список названий карточек'):
        titles = catalog_page.get_list_title_products()
    with allure.step('Проверяем, что по умолчанию выбрано значение a-z в селекте'):
        assert_equal_str('Name (A to Z)', catalog_page.get_active_select().inner_text())
    with allure.step('Проверяем, что сортировка по умолчанию a-z)'):
        assert titles == sorted(titles)

def test_sort_price_l_to_h(catalog_page):
    catalog_page.open_catalog_page()
    with allure.step('Получаем список цен карточек'):
        old_sort_price = catalog_page.get_price_list_products()
    with allure.step('Сортируем список по цене от low до high(по убыванию)'):
        catalog_page.select_sort('lohi')
    with allure.step('Проверяем, что выбрано значение low-high в селекте'):
        assert_equal_str('Price (low to high)', catalog_page.get_active_select().inner_text())
    with allure.step('Проверяем, что старая сортировка != новой)'):
        new_sort_price = catalog_page.get_price_list_products()
        assert old_sort_price != new_sort_price
        assert sorted(old_sort_price) == new_sort_price

def test_sort_price_h_to_l(catalog_page):
    catalog_page.open_catalog_page()
    with allure.step('Получаем список цен карточек'):
        old_sort_price = catalog_page.get_price_list_products()
    with allure.step('Сортируем список по цене от high до low(по убыванию)'):
        catalog_page.select_sort('hilo')
    with allure.step('Проверяем, что выбрано значение high-low в селекте'):
        assert_equal_str('Price (high to low)', catalog_page.get_active_select().inner_text())
    with allure.step('Проверяем, что старая сортировка != новой)'):
        new_sort_price = catalog_page.get_price_list_products()
        assert old_sort_price != new_sort_price
        assert sorted(old_sort_price, reverse=True) == new_sort_price



