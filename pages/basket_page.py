from .base_page import BasePage
from .locators import BasePageLocators
class BasketPage(BasePage):
	def should_cant_see_product_in_basket(self):
		self.link_to_basket()
		login_page = BasketPage(self.browser,self.browser.current_url)
		login_page.should_empty_basket()
		login_page.is_not_element_in_basket()
	def is_not_element_in_basket(self):
		assert self.is_not_element_present(*BasePageLocators.SELECTOR_NOT_ITEM_IN_BASKET), \
			"select item in basket"

