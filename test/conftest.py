import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page
from page.assertation.assertation import assert_equal_str
from page.login_page.login_page import LoginPage

@pytest.fixture
def credentials_success_user():
    load_dotenv()
    login = os.getenv("STANDART_USER")
    password = os.getenv("PASSWORD")
    return login, password

@pytest.fixture
def credentials_locked_user():
    load_dotenv()
    login = os.getenv("LOCKED_OUT_USES")
    password = os.getenv("PASSWORD")
    return login, password

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def login_standard_user(login_page, credentials_success_user):
    login, password = credentials_success_user
    login_page.open()
    login_page.login(login, password)
    login_page.page.wait_for_url('https://www.saucedemo.com/inventory.html')
    assert_equal_str(login_page.page.url, 'https://www.saucedemo.com/inventory.html')