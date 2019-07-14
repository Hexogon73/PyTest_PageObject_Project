from .base_page import BasePage
from .locators import LoginPageLocators as Locators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'Substring "login" should be in url but not'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_form_locators = [Locators.LOGIN_USERNAME_INPUT,
                               Locators.LOGIN_PASSWORD_INPUT,
                               Locators.LOGIN_BUTTON]
        for login_form_locator in login_form_locators:
            assert self.is_element_present(*login_form_locator), 'Element with locator "{}" is not found'.format(
                login_form_locator[1])

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        registration_form_locators = [Locators.REGISTRATION_EMAIL_INPUT,
                                      Locators.REGISTRATION_PASSWORD_INPUT1,
                                      Locators.REGISTRATION_PASSWORD_INPUT2,
                                      Locators.REGISTRATION_BUTTON]
        for registration_form_locator in registration_form_locators:
            assert self.is_element_present(*registration_form_locator), 'Element with locator "{}" is not found'.format(
                registration_form_locator[1])
