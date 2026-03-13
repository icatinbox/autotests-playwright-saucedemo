from page.base_page.base_page import BasePage


class DetailPage(BasePage):
    def __init__(self, page):
        super(DetailPage, self).__init__(page)

    def get_description_products(self):
       return self.locator('[data-test="inventory-item-desc"]')

    def get_title_products(self):
        return self.locator('[data-test="inventory-item-name"]')

    def get_price_products(self):
        return self.locator('[data-test="inventory-item-price"]')