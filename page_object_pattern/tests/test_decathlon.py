import pytest
from page_object_pattern.pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestGoogleSearch:

    def test_page_load(self,setup):

        self.driver.get("https://www.decathlon.pl/")

        home_page = HomePage(self.driver)


        # home_page.closing()

    # def test_adding_products(self):
    #
    # def test_purchase(self):




