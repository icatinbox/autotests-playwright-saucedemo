import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

from page.login_page.login_page import LoginPage


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

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