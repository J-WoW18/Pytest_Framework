# 2021 Dec 4 - conftest.py
# Elliot Erstein
# Pytest CLI options for different webdriver options (Chrome,Firefox,etc) and WinAppDriver
#
########################################################################
import os.path

import pytest
from selenium import webdriver
from py._xmlgen import html # needed for pytest-html Summary section custom html content
# *** NEED TO ADD WinAppDriver setup hooks ***
#import subprocess # just open winAppDriver manually or as part of a batch script...
from appium import webdriver as ap_webdriver
from datetime import datetime

@pytest.fixture()
def setup(browser):
    #global driver
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    elif browser=='windows':
        #subprocess.run("C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe")
        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        driver = ap_webdriver.Remote(
            command_executor="http://127.0.0.1:4723",
            desired_capabilities=desired_caps)
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################
def pytest_html_report_title(report):
    report.title = "Custom Title (@conftest.py)"
# Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Project Name (@conftest.py)'
    config._metadata['Module Name'] = 'Module Name (@conftest.py)'
    config._metadata['Tester'] = 'J-WoW (@conftest.py)'
    config._metadata['Custom Section'] = 'Custom (@conftest.py)'
#    config._metadata['Packages'] = 'Custom (@conftest.py)'
# Delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
    metadata.pop("Python", None)
# Adding Summary info to HTML Report
@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("Add more custom text into the summary section (@conftest.py)")])

