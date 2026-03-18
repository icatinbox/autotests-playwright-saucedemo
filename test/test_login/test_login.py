import allure
from playwright.sync_api import expect

from page.assertation.assertation import assert_equal_str
from utils.utils import attach_allure_text


def test_success_login(login_page, credentials_success_user):
    with allure.step('Получаем логин и пароль юзера'):
        login, password = credentials_success_user
        attach_allure_text(name='Логин и пароль', text=f'login={login}, password={password}')
    login_page.open_login_page()
    login_page.login(login, password)
    with allure.step('Проверка, что произошел редирект после логина'):
        login_page.page.wait_for_url('https://www.saucedemo.com/inventory.html')
        assert_equal_str(login_page.page.url,'https://www.saucedemo.com/inventory.html')

def test_locked_failed_login(login_page, credentials_locked_user):
    with allure.step('Получаем логин и пароль юзера'):
        login, password = credentials_locked_user
        attach_allure_text(name='Логин и пароль', text=f'login={login}, password={password}')
    login_page.open_login_page()
    login_page.login(login, password)
    error_text = login_page.get_error_message()
    assert_equal_str(error_text, 'Epic sadface: Sorry, this user has been locked out.')
    input_username = login_page.get_input_username()
    input_password = login_page.get_input_password()
    with allure.step('Проверяем наличие класса error'):
        expect(input_username).to_contain_class('error')
        expect(input_username).to_contain_class('input_error')
        expect(input_password).to_contain_class('error')
        expect(input_password).to_contain_class('input_error')
    with allure.step('Проверяем наличие иконки error'):
        error_icon_username = input_username.locator("xpath=..").locator("input + svg")
        error_icon_password = input_password.locator("xpath=..").locator("input + svg")
        expect(error_icon_username).to_be_visible()
        expect(error_icon_password).to_be_visible()



