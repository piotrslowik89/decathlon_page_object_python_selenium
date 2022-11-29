import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from page_object_pattern.pages.cart_page import CartPage
from page_object_pattern.pages.home_page import HomePage
from page_object_pattern.pages.shopping_page import ShoppingPage


@pytest.mark.usefixtures("setup")
class TestDecathlon:

    def test_page_load(self, setup):
        self.driver.get("https://www.decathlon.pl/")

        home_page = HomePage(self.driver)
        home_page.privacy_policy()
        home_page.left_menu()
        home_page.navbar()

    def test_shopping(self, setup):
        self.driver.get("https://www.decathlon.pl/")

        shopping_page = ShoppingPage(self.driver)
        shopping_page.privacy_policy()
        shopping_page.women_shopping()
        shopping_page.man_shopping()
        shopping_page.child_shopping()

        cart_page= CartPage(self.driver)
        cart_page.go_to_cart()


