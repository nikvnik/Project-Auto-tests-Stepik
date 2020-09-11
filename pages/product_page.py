from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def add_to_basket(self):
		button = self.browser.find_element(*ProductPageLocators.CLASS_BUTTON_BASKET)
		button.click()
	def check_name_product_in_string_basket(self):
		name_product = self.browser.find_element(*ProductPageLocators.SELECTOR_CHECK_NAME_PRODUCT).text
		name_basket_product = self.browser.find_element(*ProductPageLocators.SELECTOR_CHECK_BASKET).text
		assert name_product == name_basket_product, "Item not added to basket"
	def check_price_product_in_price_bakset(self):
		price_product = self.browser.find_element(*ProductPageLocators.SELECTOR_PRICE).text.replace(',','.')
		basket_price_product = self.browser.find_element(*ProductPageLocators.SELECTOR_PRICE_BASKET).text.replace(',','.')
		assert float(price_product.replace(' £','')) == float(basket_price_product.replace(' £','')), "The product price and the amount in the shopping cart do not match."
	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SELECTOR_SUCCESS_MESSAGE), \
			"Success message is presented, but should not be"
	def should_element_is_disappeared(self):
		assert self.is_disappeared(*ProductPageLocators.SELECTOR_SUCCESS_MESSAGE), \
			"Success message is presented, but should not be"