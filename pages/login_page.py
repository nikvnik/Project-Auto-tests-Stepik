from .base_page import BasePage
from .locators import LoginPageLocators




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
    
    def check_price_product_equals_price_basket(self):
    	name_product = self.is_element_present(*LoginPageLocators.SELECTOR_CHECK_NAME_PRODUCT)
    	name_basket_product = self.is_element_present(*LoginPageLocators.SELECTOR_CHECK_BASKET)
    	print(name_product, name_basket_product)