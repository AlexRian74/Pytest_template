from base.base_page import BasePage
from pages.welcome_page import WelcomePage
from pages.locators import FirstPageLocators
# this file represent functionality of first page through class MainPage that inherits BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    def login(self, login, pswd):
        #these methods are inherited from BasePage
        self.enter_text(FirstPageLocators.username, login)
        self.enter_text(FirstPageLocators.password, pswd)
        self.click(FirstPageLocators.formbtn)
        return WelcomePage(self.driver) #return class that is used for manipulating next page



