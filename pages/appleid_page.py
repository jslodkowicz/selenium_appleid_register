# -*- coding: utf-8 -*-
from pages.base_page import BasePage
from locators import AppleIdPageLocators
from selenium.webdriver.common.by import By

class AppleIdPage(BasePage):
    def _verify_page(self):
        assert "Zarządzaj swoim Apple ID - Apple (PL)" in self.driver.title

    def click_create_account(self):
        self.driver.find_element(*AppleIdPageLocators.CREATE_APPLE_ID_BTN).click()
