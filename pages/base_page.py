from selenium.common.exceptions import NoSuchElementException
import math
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(30)

    def open(self): 
    	self.browser.get(self.url)

    def is_element_present(self, how, what):
	    try:
	    	self.browser.find_element(how, what)
	    except (NoSuchElementException):
	    	return False
	    return True
    def alert_two(self):
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        #self.alert_two()
    def is_not_element_present(self, how, what, timeout=4): #check is not element on page
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    def is_disappeared(self, how, what, timeout=4): # checl element is disappereaded
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def link_to_basket(self):
        button = self.browser.find_element(*BasePageLocators.SELECTOR_BUTTON_BASKET)
        button.click()
    def should_empty_basket(self):
        element = self.browser.find_element(*BasePageLocators.SELECTOR_BASKET_EMPTY)
        assert "empty" in element.text, "The basket is empty"
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"

