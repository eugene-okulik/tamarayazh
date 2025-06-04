import pytest
from test_UI_tyazhova_pw.pages.create_new_account import CreateNewAccount
from test_UI_tyazhova_pw.pages.sale_page import SalePage
from test_UI_tyazhova_pw.pages.eco_friendly_page import EcoFriendlyPage


@pytest.fixture()
def create_new_account(page):
    return CreateNewAccount(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendlyPage(page)
