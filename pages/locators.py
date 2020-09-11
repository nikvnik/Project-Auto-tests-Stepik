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
class ProductPageLocators():
	CLASS_BUTTON_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
	SELECTOR_CHECK_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
	SELECTOR_CHECK_NAME_PRODUCT = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
	SELECTOR_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
	SELECTOR_PRICE_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
