import softest
from ddt import ddt, data, unpack, file_data
import pytest
from pages.main_page import MainPage
from pages.locators import Credentials
from utilities.utilities import Utils
import yaml #only if you need support of yaml files

@ddt
# This means the "setup" fixture will run prior to this class/ class methods
@pytest.mark.usefixtures("setup") #this string isn't necessary if the setup fixture has autouse=True attribute
class TestExecution(softest.TestCase):
    log = Utils().StartLog()

    # @data(("1.07.2023 0:00", "1.07.2023 22:00"))
    #@file_data("../test_data/test1_data.yaml")
    @data(*Utils.readExcelFile("../test_data/test1_data.xlsx"))
    @unpack
    def test_first(self, dateF, dateT):
        self.log.info("Starting first test")
        self.driver.get("https://cloud.pay-point.com/")
        first_page = MainPage(self.driver)
        welcome_page = first_page.login(Credentials.login, Credentials.pswd) #proceed to the next page
        payments = welcome_page.FindPayment() #proceed to third page
        payment_info = payments.Get(dateF,dateT)
        self.log.info(f"total: {payment_info.total}, cash:{payment_info.cash}, free:{payment_info.free_cuts}")
    def test_second(self):
        self.log.info("Starting second test")
        self.driver.get("https://google.com")


