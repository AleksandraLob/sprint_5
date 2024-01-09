import random


class EnterSite:
    name = 'testpochta'
    email = 'testpochta@ya.ru'
    password = '123456'
    invalid_password = '777'

    @staticmethod
    def random_email():
        user = ""
        domen = random.choice(['gmail.com', 'ya.ru', 'yandex.ru', 'mail.com', 'indusoft.ru'])

        for i in range(8):
            user += random.choice('qazwsxedcRFVTGBYHN-!._123456')

        email = f"{user}@{domen}"
        return email

    @staticmethod
    def random_password():
        password = ""

        for i in range(8):
            digit = str(random.randint(0, 9))
            password += digit

        return password


class Site:
    main_site = 'https://stellarburgers.nomoreparties.site/'
    login_site = 'https://stellarburgers.nomoreparties.site/login'
    registration_site = 'https://stellarburgers.nomoreparties.site/register'
    forgot_pass_site = 'https://stellarburgers.nomoreparties.site/forgot-password'
    profile_site = 'https://stellarburgers.nomoreparties.site/account/profile'
