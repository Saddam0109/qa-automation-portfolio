from utils.base_page import BasePage


class InventoryPage(BasePage):
    PAGE_TITLE = ".title"
    ADD_BACKPACK = "#add-to-cart-sauce-labs-backpack"
    ADD_BIKE_LIGHT = "#add-to-cart-sauce-labs-bike-light"
    SHOPPING_CART_LINK = ".shopping_cart_link"

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK)

    def add_bike_light_to_cart(self):
        self.click(self.ADD_BIKE_LIGHT)

    def open_cart(self):
        self.click(self.SHOPPING_CART_LINK)