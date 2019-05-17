# -*- coding: utf-8 -*-
import unittest
from locators import HomePageLocators, AppleIdPageLocators, RegisterPageLocators
from pages.home_page import HomePage
from pages.appleid_page import AppleIdPage
from pages.register_page import RegisterPage
from values import TestValues
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class AppleIdRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.apple.com/pl/")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

        HomePage(self.driver).click_apple_id()
        AppleIdPage(self.driver).click_create_account()

    def tearDown(self):
        self.driver.quit()

    def test_birthday_today(self):

        driver = self.driver

        RegisterPage(driver).first_name(TestValues.valid_first_name)
        RegisterPage(driver).last_name(TestValues.valid_last_name)
        RegisterPage(driver).country(TestValues.valid_country)
        RegisterPage(driver).birthdate(TestValues.today)
        RegisterPage(driver).email(TestValues.valid_email)
        RegisterPage(driver).password(TestValues.valid_password)
        RegisterPage(driver).conf_password(TestValues.valid_password)
        RegisterPage(driver).question_answer(*TestValues.q_a[0], 0)
        RegisterPage(driver).question_answer(*TestValues.q_a[1], 1)
        RegisterPage(driver).question_answer(*TestValues.q_a[2], 2)
        RegisterPage(driver).news_checkbox(False)
        RegisterPage(driver).itunes_checkbox(True)
        RegisterPage(driver).captcha()
        RegisterPage(driver).continue_btn()

        error_messages = self.driver.find_elements(*RegisterPageLocators.ERROR_MSGS)

        self.assertEqual(len(error_messages), 1)
        self.assertIn(error_messages[0].get_attribute('innerText').strip(), (
            'Data urodzenia musi być datą przeszłą.',
            'Nie możesz utworzyć Apple ID, ponieważ nie spełniasz kryterium wieku minimalnego. Poproś rodzica lub opiekuna o skonfigurowanie Chmury rodzinnej. Dowiedz się więcej…')
)

    def test_wrong_captcha(self):

        driver = self.driver

        RegisterPage(driver).first_name(TestValues.valid_first_name)
        RegisterPage(driver).last_name(TestValues.valid_last_name)
        RegisterPage(driver).country(TestValues.valid_country)
        RegisterPage(driver).birthdate(TestValues.valid_birthdate)
        RegisterPage(driver).email(TestValues.valid_email)
        RegisterPage(driver).password(TestValues.valid_password)
        RegisterPage(driver).conf_password(TestValues.valid_password)
        RegisterPage(driver).question_answer(*TestValues.q_a[0], 0)
        RegisterPage(driver).question_answer(*TestValues.q_a[1], 1)
        RegisterPage(driver).question_answer(*TestValues.q_a[2], 2)
        RegisterPage(driver).news_checkbox(False)
        RegisterPage(driver).itunes_checkbox(True)
        RegisterPage(driver).captcha(TestValues.invalid_captcha)
        RegisterPage(driver).continue_btn()

        error_messages = self.driver.find_elements(*RegisterPageLocators.ERROR_MSGS)

        self.assertIn(
            error_messages[0].get_attribute('innerText').strip(),
            'Aby kontynuować, wpisz znaki, które widzisz lub słyszysz.')


if __name__ == '__main__':
    unittest.main(verbosity=2)
