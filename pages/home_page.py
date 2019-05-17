# -*- coding: utf-8 -*-
from pages.base_page import BasePage
from locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    def _verify_page(self):
        assert "Apple (Polska)" in self.driver.title

    def click_apple_id(self):
        self.driver.find_element(*HomePageLocators.APPLE_ID_BTN).click()
