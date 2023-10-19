
from selenium.webdriver import ActionChains
from pages.locators import WelcomePageLocators
from base.base_page import BasePage
from pages.get_payments import GetPayments

#creating new class that inherits methods of BasePage. Method of Welcome page are used to manipulate the particular page
class WelcomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def FindPayment(self):
        # moving 'mouse' over the element
        element_tmp = self.wait_until_element_is_clickable(WelcomePageLocators.disp_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_tmp).perform()
        self.click(WelcomePageLocators.poisk_link)
        return GetPayments(self.driver) #returns object for next page

