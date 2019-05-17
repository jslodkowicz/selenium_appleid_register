# -*- coding: utf-8 -*-
import datetime

class TestValues:
    valid_first_name = 'Hanna'
    valid_last_name = 'Wanna'
    valid_country = 'Gwatemala'
    valid_birthdate = '03061987'
    today = datetime.date.today().strftime('%d%m%Y')
    valid_email = 'jestemtesterem@hotmail.com'
    valid_password = 'qweRTY123!@?'
    invalid_captcha = 'I AM WRONG!'
    q_a = [('Jak się wabił Twój pierwszy zwierzak?', 'Tom'),
        ('Jakiej marki był Twój pierwszy pojazd?', 'Fiat'),
        ('Jaka była Twoja pierwsza kupiona płyta?', 'Fajna')]
