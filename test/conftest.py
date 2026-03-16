import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect
from page.assertation.assertation import assert_equal_str
from page.cart_page.cart_page import CartPage
from page.catalog_page.catalog_page import CatalogPage
from page.detail_page.detail_page import DetailPage
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

@pytest.fixture
def catalog_page(page: Page, login_standard_user):
    return CatalogPage(page)

@pytest.fixture
def detail_product_page(page: Page, login_standard_user):
    return DetailPage(page)

@pytest.fixture
def cart_page(page: Page, login_standard_user):
    return CartPage(page)

@pytest.fixture
def product_cart(catalog_page):
    card = catalog_page.random_product()
    btn_add_to_card = catalog_page.get_btn_add_to_cart(card)
    catalog_page.add_to_cart(btn_add_to_card)
    badge = catalog_page.get_badge_count_cart()
    expect(badge).to_be_visible()
    assert badge.inner_text() == '1'
    return card
