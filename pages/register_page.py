# -*- coding: utf-8 -*-
from pages.base_page import BasePage
from locators import HomePageLocators
from locators import RegisterPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class RegisterPage(BasePage):
    def _verify_page(self):
        assert self.driver.title in [
            'Zarządzaj swoim Apple ID - Apple (PL)',
            'Utwórz Apple ID - Apple (PL)']

    def first_name(self, name):
        self.driver.find_element(
            *RegisterPageLocators.FIRST_NAME_FIELD).send_keys(name)

    def last_name(self, name):
        self.driver.find_element(
            *RegisterPageLocators.LAST_NAME_FIELD).send_keys(name)

    def country(self, country):
        countries = self.driver.find_element(*RegisterPageLocators.COUNTRIES_MENU)
        countries_list = countries.find_elements_by_tag_name('option')
        for l in countries_list:
            if l.get_attribute('innerText').strip() == country:
                l.location_once_scrolled_into_view
                l.click()

    def birthdate(self, date):
        self.driver.find_element(
            *RegisterPageLocators.BIRTHDATE_FIELD).send_keys(date)

    def email(self, mail):
        self.driver.find_element(
            *RegisterPageLocators.EMAIL_FIELD).send_keys(mail)

    def password(self, password):
        self.driver.find_element(
            *RegisterPageLocators.PASSWORD_FIELD).send_keys(password)

    def conf_password(self, password):
        self.driver.find_element(
            *RegisterPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)

    def question_answer(self, question, answer, nr):
        question_fields = [
            RegisterPageLocators.QUESTION_FIELD_1,
            RegisterPageLocators.QUESTION_FIELD_2,
            RegisterPageLocators.QUESTION_FIELD_3,
        ]
        answer_fields = [
            RegisterPageLocators.ANSWER_FIELD_1,
            RegisterPageLocators.ANSWER_FIELD_2,
            RegisterPageLocators.ANSWER_FIELD_3,
        ]

        question_field = self.driver.find_element(
            *question_fields[nr])
        answers_list = question_field.find_elements_by_tag_name('option')
        answer_field = self.driver.find_element(*answer_fields[nr])
        for l in answers_list:
            if l.get_attribute('innerText').strip() == question:
                l.click()
                answer_field.send_keys(answer)

    def news_checkbox(self, x):
        if x == False:
            self.driver.find_element(
                *RegisterPageLocators.NEWS_CHECKBOX).send_keys(Keys.SPACE)

    def itunes_checkbox(self, x):
        if x == False:
            self.driver.find_element(
                *RegisterPageLocators.ITUNES_CHECKBOX).send_keys(Keys.SPACE)

    def captcha(self, value=False, seconds=10):
        captcha_field = self.driver.find_element(*RegisterPageLocators.CAPTCHA_FIELD)
        if value:
            captcha_field.send_keys(value)
        else:
            captcha_field.click()
            time.sleep(seconds)

    def continue_btn(self):
        self.driver.find_element(*RegisterPageLocators.CONTINUE_BTN).click()
