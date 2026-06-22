from utils.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = ".cart_item"
    CHECKOUT_BUTTON = "#checkout"

    def get_cart_items_count(self):
        return self.page.locator(self.CART_ITEMS).count()

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)