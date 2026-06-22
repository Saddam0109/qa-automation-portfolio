package tests;

import base.BaseTest;
import org.testng.Assert;
import org.testng.annotations.Test;
import pages.CartPage;
import pages.CheckoutPage;
import pages.InventoryPage;
import pages.LoginPage;
import utils.ConfigReader;

public class CheckoutTest extends BaseTest {

    @Test
    public void testCompleteCheckout() {
        LoginPage loginPage = new LoginPage(driver);
        InventoryPage inventoryPage = new InventoryPage(driver);
        CartPage cartPage = new CartPage(driver);
        CheckoutPage checkoutPage = new CheckoutPage(driver);

        loginPage.login(
                ConfigReader.getProperty("validUsername"),
                ConfigReader.getProperty("validPassword")
        );

        inventoryPage.addBackpackToCart();
        inventoryPage.openCart();
        cartPage.clickCheckout();

        checkoutPage.enterCheckoutInfo(
                ConfigReader.getProperty("firstName"),
                ConfigReader.getProperty("lastName"),
                ConfigReader.getProperty("postalCode")
        );
        checkoutPage.clickContinue();
        checkoutPage.clickFinish();

        Assert.assertEquals(checkoutPage.getSuccessMessage(), "Thank you for your order!");
    }
}