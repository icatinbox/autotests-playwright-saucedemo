from page.base_page.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def open_cart(self):
        self.open('/cart.html')

    def get_products_cart(self):
        return self.locator('.cart_item_label')

    def get_title(self):
        return self.get_products_cart().locator('.inventory_item_name').inner_text()

    def get_description(self):
        return self.get_products_cart().locator('.inventory_item_desc').inner_text()

    def get_price(self):
        return self.get_products_cart().locator('.inventory_item_price').inner_text()

    def click_btn_checkout(self):
        self.click(self.locator('[data-test="checkout"]'))

    def fill_first_name(self, value):
        input_first_name = self.locator('[data-test="firstName"]')
        self.fill(input_first_name, value)

    def fill_last_name(self, value):
        input_last_name = self.locator('[data-test="lastName"]')
        self.fill(input_last_name, value)

    def fill_postal_code(self, value):
        input_postal_code = self.locator('[data-test="postalCode"]')
        self.fill(input_postal_code, value)

    def click_btn_continue(self):
        self.click(self.locator('[data-test="continue"]'))

    def click_btn_finish(self):
        self.click(self.locator('[data-test="finish"]'))

    def get_complete_header_message(self):
        return self.locator('[data-test="complete-header"]').inner_text()

    def get_complete_description(self):
        return self.locator('[data-test="complete-text"]').inner_text()