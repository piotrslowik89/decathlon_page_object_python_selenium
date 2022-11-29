import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.button_accept_id = 'didomi-notice-agree-button'
        self.button_menu = 'menu-button svelte-156j4bw'

    @allure.step("Test 1")
    def privacy_policy(self):
        self.driver.find_element(By.ID, self.button_accept_id).click()
        # doddać jakąś asercję

    @allure.step("Test 2")
    def left_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, '.menu-button').click()
        # asercja dotyczaca menu
        self.driver.find_element(By.CSS_SELECTOR, '.close').click()

    def navbar(self):
        navbar_element_1 = self.driver.find_element(By.CSS_SELECTOR, 'button.svelte-13mgb6t:nth-child(1)')
        navbar_element_2 = self.driver.find_element(By.CSS_SELECTOR, 'button.svelte-13mgb6t:nth-child(2)')
        navbar_element_3 = self.driver.find_element(By.CSS_SELECTOR, 'button.svelte-13mgb6t:nth-child(3)')
        navbar_element_4 = self.driver.find_element(By.CSS_SELECTOR, 'button.svelte-13mgb6t:nth-child(4)')
        navbar_element_5 = self.driver.find_element(By.CSS_SELECTOR, 'button.svelte-13mgb6t:nth-child(5)')
        navbar_element_6 = self.driver.find_element(By.CSS_SELECTOR, 'button.svelte-13mgb6t:nth-child(6)')
        navbar_element_7 = self.driver.find_element(By.CSS_SELECTOR, 'button.svelte-13mgb6t:nth-child(7)')
        navbar_element_8 = self.driver.find_element(By.CSS_SELECTOR, 'button.svelte-13mgb6t:nth-child(8)')
        webdriver.ActionChains(self.driver).move_to_element(navbar_element_1).perform()
        webdriver.ActionChains(self.driver).move_to_element(navbar_element_2).perform()
        webdriver.ActionChains(self.driver).move_to_element(navbar_element_3).perform()
        webdriver.ActionChains(self.driver).move_to_element(navbar_element_4).perform()
        webdriver.ActionChains(self.driver).move_to_element(navbar_element_5).perform()
        webdriver.ActionChains(self.driver).move_to_element(navbar_element_6).perform()
        webdriver.ActionChains(self.driver).move_to_element(navbar_element_7).perform()
        webdriver.ActionChains(self.driver).move_to_element(navbar_element_8).perform()







        # allure.attach(self.driver.get_screenshot_as_png(), name="exampleName", attachment_type=AttachmentType.PNG)
