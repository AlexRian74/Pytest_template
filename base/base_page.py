#base_page.py
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Contains basic actions that can be reused on all the pages
class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            match = False
            while (match == False):
                lastCount = pageLength
                time.sleep(1)
                pageLength = self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
                if lastCount == pageLength:
                    match = True
            time.sleep(4)

    def wait_for_presence_of_all_elements(self,locator):
        wait = WebDriverWait(self.driver, 20)
        list_of_elements = wait.until(EC.presence_of_all_elements_located(locator))
        return list_of_elements

    def wait_until_element_is_clickable(self, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable(locator))
        return element

    def wait_until_element_is_present(self, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.presence_of_element_located(locator))
        return element

    def enter_text(self, locator, text):
        f = self.wait_until_element_is_clickable(locator)
        f.clear()
        return f.send_keys(text)

    def click(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator)).click()