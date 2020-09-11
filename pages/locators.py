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
	LOGIN_USER_SELECTOR = (By.CSS_SELECTOR, "#id_registration-email")
	PASSWORD_USER_SELECTOR = (By.CSS_SELECTOR, "#id_registration-password1")
	PASSWORD_USER_SELECTOR2 = (By.CSS_SELECTOR, "#id_registration-password2")
	BUTTON_LOGIN_SELECTOR = (By.CSS_SELECTOR, "#login_form > button")
	BUTTON_REGISTRATION_SELECTOR = (By.CSS_SELECTOR, "#register_form > button")
class ProductPageLocators():
	CLASS_BUTTON_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
	SELECTOR_CHECK_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
	SELECTOR_CHECK_NAME_PRODUCT = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
	SELECTOR_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
	SELECTOR_PRICE_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
	SELECTOR_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SELECTOR_BUTTON_BASKET = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SELECTOR_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    SELECTOR_NOT_ITEM_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")