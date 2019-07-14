from selenium.webdriver.common.by import By


class MainPageLocators:
    # LOGIN_LINK = (By.CSS_SELECTOR, '#registration_link')
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_USERNAME_INPUT = (By.CSS_SELECTOR, 'input#id_login-username')
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input#id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')

    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, 'input#id_registration-email')
    REGISTRATION_PASSWORD_INPUT1 = (By.CSS_SELECTOR, 'input#id_registration-password1')
    REGISTRATION_PASSWORD_INPUT2 = (By.CSS_SELECTOR, 'input#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

