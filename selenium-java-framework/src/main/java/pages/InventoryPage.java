package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class InventoryPage {
    WebDriver driver;

    By title = By.className("title");
    By addBackpack = By.id("add-to-cart-sauce-labs-backpack");
    By addBikeLight = By.id("add-to-cart-sauce-labs-bike-light");
    By cartLink = By.className("shopping_cart_link");

    public InventoryPage(WebDriver driver) {
        this.driver = driver;
    }

    public String getPageTitle() {
        return driver.findElement(title).getText();
    }

    public void addBackpackToCart() {
        driver.findElement(addBackpack).click();
    }

    public void addBikeLightToCart() {
        driver.findElement(addBikeLight).click();
    }

    public void openCart() {
        driver.findElement(cartLink).click();
    }
}