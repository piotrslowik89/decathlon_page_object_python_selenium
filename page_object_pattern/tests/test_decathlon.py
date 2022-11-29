import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from page_object_pattern.pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestGoogleSearch:

    def test_page_load(self,setup):

        self.driver.get("https://www.decathlon.pl/")

        home_page = HomePage(self.driver)
        home_page.privacy_policy()
        home_page.left_menu()
        home_page.navbar()





        self.driver.get("https://www.wp.pl/")
        # home_page.closing()

    # def test_adding_products(self):
    #
    # def test_purchase(self):




