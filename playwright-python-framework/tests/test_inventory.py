import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.data_reader import read_json


@allure.feature("Inventory")
@pytest.mark.smoke
def test_add_single_product_to_cart(page):
    users = read_json("users.json")
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.login(users["valid_user"]["username"], users["valid_user"]["password"])
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    assert cart_page.get_cart_items_count() == 1


@allure.feature("Inventory")
@pytest.mark.regression
def test_add_multiple_products_to_cart(page):
    users = read_json("users.json")
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.login(users["valid_user"]["username"], users["valid_user"]["password"])
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
    inventory_page.open_cart()

    assert cart_page.get_cart_items_count() == 2