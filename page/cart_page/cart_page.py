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

    def get_input_first_name(self):
        return self.locator('[data-test="firstName"]')

    def fill_first_name(self, value):
        self.fill(self.get_input_first_name(), value)

    def get_input_last_name(self):
        return self.locator('[data-test="lastName"]')

    def fill_last_name(self, value):
        self.fill(self.get_input_last_name(), value)

    def get_input_postal_code(self):
        return self.locator('[data-test="postalCode"]')

    def fill_postal_code(self, value):
        self.fill(self.get_input_postal_code(), value)

    def click_btn_continue(self):
        self.click(self.locator('[data-test="continue"]'))

    def click_btn_finish(self):
        self.click(self.locator('[data-test="finish"]'))

    def get_complete_header_message(self):
        return self.locator('[data-test="complete-header"]').inner_text()

    def get_complete_description(self):
        return self.locator('[data-test="complete-text"]').inner_text()

    def get_error_message(self):
        return self.locator('.error-message-container [data-test="error"]').inner_text()

    def click_btn_cancel(self):
        self.click(self.get_by_role('button', name='cancel'))