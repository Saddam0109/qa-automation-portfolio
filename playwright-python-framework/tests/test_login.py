import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_reader import read_json


@allure.feature("Login")
@pytest.mark.smoke
def test_valid_login(page):
    users = read_json("users.json")
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login(users["valid_user"]["username"], users["valid_user"]["password"])

    assert "Products" in inventory_page.get_page_title()


@allure.feature("Login")
@pytest.mark.regression
def test_invalid_login(page):
    users = read_json("users.json")
    login_page = LoginPage(page)

    login_page.login(users["invalid_user"]["username"], users["invalid_user"]["password"])

    assert "do not match" in login_page.get_error_message()