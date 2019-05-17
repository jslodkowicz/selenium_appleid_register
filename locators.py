# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class HomePageLocators(object):
    APPLE_ID_BTN = (By.XPATH, '//a[@href="https://appleid.apple.com/pl/"]')

class AppleIdPageLocators(object):
    CREATE_APPLE_ID_BTN = (By.XPATH, '//a[@href="/account"][@class="btn btn-link tk-caption btn-create"]')

class RegisterPageLocators(object):
    FIRST_NAME_FIELD = (By.XPATH, '//first-name-input/div/idms-textbox/idms-error-wrapper/div/div/input')
    LAST_NAME_FIELD = (By.XPATH, '//last-name-input/div/idms-textbox/idms-error-wrapper/div/div/input')
    COUNTRIES_MENU = (By.XPATH, '//select[@class="generic-input-field form-control   form-dropdown form-dropdown country-picker idms-address-country "]')
    BIRTHDATE_FIELD = (By.XPATH, '//masked-date/idms-error-wrapper/div/div/input')
    EMAIL_FIELD = (By.XPATH, '//email-input/div/idms-textbox/idms-error-wrapper/div/div/input')
    PASSWORD_FIELD = (By.ID, 'password')
    CONFIRM_PASSWORD_FIELD = (By.XPATH, '//confirm-password-input/div/idms-textbox/idms-error-wrapper/div/div/input')
    QUESTION_FIELD_1 = (By.XPATH, '//idms-dropdown[@placeholder="Pytanie zabezpieczające 1"]')
    ANSWER_FIELD_1 = (By.XPATH, '//security-answer[@answer-number="1"]/div/idms-textbox/idms-error-wrapper/div/div/input')
    QUESTION_FIELD_2 = (By.XPATH, '//idms-dropdown[@placeholder="Pytanie zabezpieczające 2"]')
    ANSWER_FIELD_2 = (By.XPATH, '//security-answer[@answer-number="2"]/div/idms-textbox/idms-error-wrapper/div/div/input')
    QUESTION_FIELD_3 = (By.XPATH, '//idms-dropdown[@placeholder="Pytanie zabezpieczające 3"]')
    ANSWER_FIELD_3 = (By.XPATH, '//security-answer[@answer-number="3"]/div/idms-textbox/idms-error-wrapper/div/div/input')
    NEWS_CHECKBOX = (By.ID, 'news')
    ITUNES_CHECKBOX = (By.ID, 'itunes')
    CAPTCHA_FIELD = (By.XPATH, '//captcha-input/div/idms-textbox/idms-error-wrapper/div/div/input')
    CONTINUE_BTN = (By.XPATH, '//div[@class="overflow-text"]')
    ERROR_MSGS = (By.XPATH, '//div[@class="form-message-wrapper std-error "]/span')
