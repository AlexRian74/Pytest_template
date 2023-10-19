from selenium.webdriver.common.by import By
#here are all the locators for all the pages
class Credentials():
    login = "AKIO_Chelyabinsk"
    pswd = "P2Ssem4ui"
class FirstPageLocators():
    username = (By.ID, "loginForm:username")
    password = (By.XPATH, "//input[@id='loginForm:password']")
    formbtn = (By.XPATH, "//span[contains(text(),'Вход')]")

class WelcomePageLocators():
    disp_locator = (By.XPATH, "//span[contains(text(),'Диспетчерская')]")
    poisk_link = (By.XPATH, "//span[contains(text(),'Поиск платежа')]")

class get_payments_page_locators():
    p_from = (By.NAME, "filterForm:startDate_input")
    p_to = (By.NAME, "filterForm:endDate_input")
    all_payments_chkbx = (By.XPATH, "//div[@id='filterForm:stateAll']//span[@class='ui-chkbox-icon ui-icon ui-icon-blank ui-c']")
    search_btn = (By.XPATH, "//button[@id='filterForm:find']//span[1]")
    free_cuts = (By.XPATH, "//table[@role='grid']/tbody/tr/td[12]")
    total_income = (By.XPATH, "//div[@id='operationsForm:table:totalIncome']//div[@class='ra nwr']")
    cash_income = (By.XPATH, "//div[@id='operationsForm:table:totalSumCash']//div[@class='ra nwr']")