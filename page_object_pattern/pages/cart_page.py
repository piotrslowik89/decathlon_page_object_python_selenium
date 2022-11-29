import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver


    @allure.step("Test 1")
    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '.cart-button').click()
        self.driver.find_element(By.CSS_SELECTOR,'.cta').click()
