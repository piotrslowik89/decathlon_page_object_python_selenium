import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class ShoppingPage:

    def __init__(self, driver):
        self.driver = driver
        self.button_accept_id = 'didomi-notice-agree-button'

    @allure.step("Step 1")
    def privacy_policy(self):
        self.driver.find_element(By.ID, self.button_accept_id).click()

    @allure.step("Step 2")
    def women_shopping(self):
        navbar_element_2 = self.driver.find_element(By.CSS_SELECTOR, 'button.svelte-13mgb6t:nth-child(2)')
        webdriver.ActionChains(self.driver).move_to_element(navbar_element_2).perform()
        self.driver.find_element(By.LINK_TEXT, 'Spódniczki damskie').click()
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element(By.CSS_SELECTOR, 'button.svelte-172usj5:nth-child(3)').click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 'div.dpb-holder:nth-child(3) > div:nth-child(3) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)').click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 '#thumbnails-slider > div:nth-child(1) > section:nth-child(2) > button:nth-child(1)').click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 '#app > main > article.product-main-infos.svelte-6s3mg4 > section.svelte-3fkw1w > div.sizes.svelte-1uwhnft > button:nth-child(4)').click()
        self.driver.find_element(By.ID, 'fitAnalytics-pdp-add-to-cart').click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 'body > aside > div > div > div.cta-section.svelte-1bm63xk > button').click()

    @allure.step("Step 3")
    def man_shopping(self):
        navbar_element_3 = self.driver.find_element(By.CSS_SELECTOR, 'button.svelte-13mgb6t:nth-child(3)')
        webdriver.ActionChains(self.driver).move_to_element(navbar_element_3).perform()
        self.driver.find_element(By.LINK_TEXT, 'Kamizelki męskie').click()
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'div.dpb-holder:nth-child(16) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)').click()
        self.driver.find_element(By.CSS_SELECTOR, 'button.sizes__size:nth-child(5)').click()
        self.driver.find_element(By.ID, 'fitAnalytics-pdp-add-to-cart').click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 'body > aside > div > div > div.cta-section.svelte-1bm63xk > button').click()

    @allure.step("Step 4")
    def child_shopping(self):
        navbar_element_4 = self.driver.find_element(By.CSS_SELECTOR, 'button.svelte-13mgb6t:nth-child(4)')
        webdriver.ActionChains(self.driver).move_to_element(navbar_element_4).perform()
        self.driver.find_element(By.LINK_TEXT, 'Deskorolki').click()
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element(By.CSS_SELECTOR, 'button.svelte-172usj5:nth-child(3)').click()
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)
        self.driver.find_element(By.CSS_SELECTOR, 'div.dpb-holder:nth-child(21) > div:nth-child(4) > a:nth-child(1)').click()
        self.driver.find_element(By.CSS_SELECTOR, 'button.svelte-10vhdb8:nth-child(2)').click()
        self.driver.find_element(By.ID, 'fitAnalytics-pdp-add-to-cart').click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 'body > aside > div > div > div.cta-section.svelte-1bm63xk > button').click()