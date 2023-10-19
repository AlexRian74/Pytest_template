import os
import time

import pytest
from selenium import webdriver
#for Chrome browser
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#for Edge browser
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.utilities import Utils
#since the test function includes a parameter named browser,
# pytest will look for a fixture named browser and provide its return value to the test function.
log = Utils().StartLog()
@pytest.fixture(autouse=True)
def setup(request, browser):
    global driver
    if browser == "Chrome":
        log.info("Starting Chrome...")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #driver = webdriver.Chrome()
    else:
        log.info("Starting Edge...")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        #driver = webdriver.Edge()
    driver.maximize_window()
    #driver should be available withing requesting class
    request.cls.driver = driver #this line is used to pass driver to a class that will call this fixture
    request.cls.login = "LOGIN_TO_THE_ADMIN_PANEL"
    request.cls.pswd = "PASSWORD_TO_THE_ADMIN_PANEL"
    yield
    log.info("Quiting browser...")
    driver.quit()

#This is a hook implementation that allows you to add custom command-line
# options to your test suite. In this case, it adds the --browser option.
def pytest_addoption(parser):
    parser.addoption("--browser")

#This is a fixture named browser
@pytest.fixture(autouse=True)
def browser(request):
    return request.config.getoption('--browser')
# if we don't want the browser to be closed after end of each method in TestExecution class,
# we need to change the scope of fixtures 'setup' and 'browser' to "class"


#this function takes screenshot when test fails and embeds it in the report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def pytest_html_report_title(report):
    report.title = "Title of the report"
