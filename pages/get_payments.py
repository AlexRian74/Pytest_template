from base.shared_classes import income_info
from base.base_page import BasePage
from pages.locators import get_payments_page_locators
class GetPayments(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    def Get(self,fromDate,toDate) -> income_info:
        self.enter_text(get_payments_page_locators.p_from, fromDate)
        self.enter_text(get_payments_page_locators.p_to, toDate)
        self.click(get_payments_page_locators.all_payments_chkbx)
        self.click(get_payments_page_locators.search_btn)
        list = self.wait_for_presence_of_all_elements(get_payments_page_locators.free_cuts)
        free_cuts = 0
        for x in list:
            if (x.text.strip() == "0.00" or x.text.strip() == "1.00"):
                free_cuts += 1
        total_income = self.wait_until_element_is_present(get_payments_page_locators.total_income).text
        total_cash = self.wait_until_element_is_present(get_payments_page_locators.cash_income).text
        a = int(total_income[:-7].replace(" ",""))
        b = int(total_cash[:-7].replace(" ",""))
        c = free_cuts
        return income_info(a,b,c)