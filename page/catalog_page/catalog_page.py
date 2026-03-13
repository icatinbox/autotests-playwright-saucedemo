import random

import allure
from playwright.sync_api import expect
from pygments.lexers import q

from page.base_page.base_page import BasePage
from utils.utils import attach_allure_text


class CatalogPage(BasePage):
    def __init__(self, page):
        super(CatalogPage, self).__init__(page)

    def open_catalog_page(self):
        self.open('/inventory.html')

    def get_products_card(self):
        cards = self.locator('[data-test="inventory-item"]')
        expect(cards.first).to_be_visible()
        return cards

    def random_product(self):
        with allure.step("Выбор рандомной карточки продукта"):
            cards = self.get_products_card()
            random_product = cards.nth(random.randrange(cards.count()))
            attach_allure_text('random_product', str(random_product))
            return random_product

    @staticmethod
    def get_tittle_product(card):
        with allure.step("Получение названия продукта"):
            title = card.locator('[data-test="inventory-item-name"]')
            attach_allure_text('title', str(title))
        return title

    @staticmethod
    def get_btn_add_to_cart(card):
        with allure.step("Получение кнопки add to cart"):
            btn_add_cart = card.get_by_role("button", name="Add to cart")
            attach_allure_text('add_to_cart', str(btn_add_cart))
        return btn_add_cart

    def add_to_cart(self, btn_add_cart):
        self.click(btn_add_cart)

    @staticmethod
    def get_btn_remove_from_cart(card):
        with allure.step("Получение кнопки remove"):
            btn_remove = card.get_by_role("button", name="Remove")
            attach_allure_text('remove', str(btn_remove))
        return btn_remove

    def remove_from_cart(self, btn_remove):
        self.click(btn_remove)

    def click_tittle_product(self, title):
        self.click(title)

    @staticmethod
    def get_link_title(card):
        return card.locator('[data-test="inventory-item-name"]').locator('xpath=..')

    @staticmethod
    def get_price_products(card):
        return card.locator('[data-test="inventory-item-price"]')

    @staticmethod
    def get_description_products(card):
        return card.locator('[data-test="inventory-item-desc"]')