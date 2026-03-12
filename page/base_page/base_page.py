from dotenv import load_dotenv
from playwright.sync_api import Page
import allure
import os

from utils.utils import attach_allure_text


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str | None = None):
        load_dotenv()
        base_url = os.getenv("BASE_URL").rstrip('/')
        url = f'{base_url}/{path.lstrip("/")}' if path else base_url
        with allure.step('Открываем страницу'):
            attach_allure_text("final url", url)
            self.page.goto(url)

    @staticmethod
    def click(el):
        with allure.step('Клик на элемент'):
            attach_allure_text("click", str(el))
            el.click()

    def locator(self, locator):
        with allure.step('Выбор элемента'):
            attach_allure_text("locator", str(locator))
            el = self.page.locator(locator)
            attach_allure_text("locator_result", str(el))
            return el

    def get_by_role(self, role, name):
        with allure.step('Выбор элемента'):
            attach_allure_text("locator", f'role={role}, name={name}')
            el = self.page.get_by_role(name=name, role=role)
            attach_allure_text("locator_result", str(el))
            return el

    @staticmethod
    def fill(el, text):
        with allure.step('Ввод текста в поле'):
            attach_allure_text("element", str(el))
            attach_allure_text("text", text)
            el.fill(text)