from page.base_page.base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super(LoginPage, self).__init__(page)

    def open_login_page(self):
        self.open()

    def login(self, login, password):
        input_login = self.get_input_username()
        input_password = self.get_input_password()
        button_submit = self.get_by_role(role='button', name='Login')
        self.fill(input_login, login)
        self.fill(input_password, password)
        self.click(button_submit)

    def get_error_message(self):
        error_message = self.locator('[data-test="error"]').inner_text()
        return error_message

    def get_input_username(self):
        return self.locator('[data-test="username"]')

    def get_input_password(self):
        return self.locator('[data-test="password"]')
