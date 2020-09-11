from pages.main_page import MainPage
from pages.basket_page import BasketPage
import pytest
#def test_guest_can_go_to_login_page(browser):
  #  link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
 #   page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
   # page.open()                      # открываем страницу
    #page.should_be_login_page()

@pytest.mark.login_guest
class TestLoginFromMainPage():
	def test_guest_should_see_login_link(self, browser):
		link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
		page = MainPage(browser, link)
		page.open()
		page.go_to_login_page()
		login_page = MainPage(page.browser,page.browser.current_url)
		login_page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_login_page()

#Check for after registration user autentification
def guest_cant_see_product_in_basket_opened_from_main_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/"
	page = LoginPage(browser, link)
	page.open()
	page.go_to_login_page()
	email = str(time.time()) + "@fakemail.org"
	login_page = LoginPage(page.browser,page.browser.current_url)
	login_page.register_new_user(email,"2354641234a!")
	login_page2 = LoginPage(login_page.browser,login_page.browser.current_url)
	login_page2.should_be_authorized_user()
