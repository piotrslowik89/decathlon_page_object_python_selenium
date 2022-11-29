import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.button_accept_id = 'didomi-notice-agree-button'

    @allure.step("Test 1")
    def search_in_google(self):
        self.driver.find_element(By.XPATH,self.button_accept_id).click()

        allure.attach(self.driver.get_screenshot_as_png(), name="exampleName", attachment_type=AttachmentType.PNG)
