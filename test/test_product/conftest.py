import pytest
from playwright.sync_api import Page
from page.catalog_page.catalog_page import CatalogPage
from page.detail_page.detail_page import DetailPage


@pytest.fixture
def catalog_page(page: Page, login_standard_user):
    return CatalogPage(page)

@pytest.fixture
def detail_product_page(page: Page, login_standard_user):
    return DetailPage(page)