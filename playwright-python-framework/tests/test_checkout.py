import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.data_reader import read_json


@allure.feature("Checkout")
@pytest.mark.regression
def test_complete_checkout(page):
    users = read_json("users.json")
    checkout_data = read_json("checkout_data.json")

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.login(users["valid_user"]["username"], users["valid_user"]["password"])
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.click_checkout()

    customer = checkout_data["customer_1"]
    checkout_page.enter_checkout_information(
        customer["first_name"],
        customer["last_name"],
        customer["postal_code"]
    )
    checkout_page.click_continue()
    checkout_page.click_finish()

    assert "Thank you for your order!" in checkout_page.get_success_message()