from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
class LoginPageLocators():
	LOGIN_FORM_ID = (By.ID, "login_form")
	REGISTRATION_FORM_ID = (By.ID, "register_form")
	PASSWORD_ID = (By.ID, "id_login-password")
	EMAIL_ID = (By.ID, "id_registration-email")
	PASSWORD_REGISTRATION_ID = (By.ID, "id_registration-password1")
	PASSWORD_REGISTRATION_CONTROL_ID = (By.ID, "id_registration-password2")
