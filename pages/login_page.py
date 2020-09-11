from .base_page import BasePage
from .locators import LoginPageLocators
import time



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        str_url = self.url
        assert "login" in str_url, "Login do not find in URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_ID), "Did not find LOGIN FORM"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM_ID), "Did not find REGISTRATION FORM"
    def register_new_user(self, email, password):
    	login = self.browser.find_element(*LoginPageLocators.LOGIN_USER_SELECTOR)
    	login.send_keys(email)
    	passwords = self.browser.find_element(*LoginPageLocators.PASSWORD_USER_SELECTOR)
    	passwords.send_keys(password)
    	passwords2 = self.browser.find_element(*LoginPageLocators.PASSWORD_USER_SELECTOR2)
    	passwords2.send_keys(password)
    	button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION_SELECTOR)
    	button.click()
    	