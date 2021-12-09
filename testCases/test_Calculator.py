# 2021 Dec 5 - test_Calculator.py
# Example testing calculator using winAppdriver. This test does not follow the Page Object Model (POM) format and
# directly finds and selects the elements within the test case.
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from pytest_html import extras
import sys


class Test_Calculator_A:

    logger = LogGen.loggen()

    @pytest.mark.calc
    def test_subtraction(self, setup):
        self.driver = setup
        self.driver.find_element(By.NAME, "One").click()
        self.driver.find_element(By.NAME, "Two").click()
        self.driver.find_element(By.NAME, "Minus").click()
        self.driver.find_element(By.NAME, "Nine").click()
        self.driver.find_element(By.NAME, "Equals").click()
        results = self.getDisplayResults()
        if results == "4":
            self.logger.info("**** Subtraction test passed ****")
            self.driver.close()
            self.driver.quit()
            assert True
        else:
            self.logger.error("**** Subtraction test failed****")
            # test_name = sys._getframe().f_code.co_name
            self.driver.save_screenshot(".\\Reports\\Screenshots\\" + "test_subtraction.png")
            #extra.append(extras.image(".\\Screenshots\\"+"test_subtraction.png"))
            self.driver.close()
            self.driver.quit()
            assert False

    @pytest.mark.calc
    def test_addition(self, setup):
        self.driver = setup
        self.driver.find_element(By.NAME, "One").click()
        self.driver.find_element(By.NAME, "Two").click()
        self.driver.find_element(By.NAME, "Plus").click()
        self.driver.find_element(By.NAME, "Nine").click()
        self.driver.find_element(By.NAME, "Equals").click()
        results = self.getDisplayResults()
        if results == "22":
            self.logger.info("**** Addition test passed ****")
            self.driver.close()
            self.driver.quit()
            assert True
        else:
            self.logger.error("**** Addition test failed****")
            self.driver.save_screenshot(".\\Reports\\Screenshots\\"+"test_add123.png")
            #extra.append(extras.image(".\\Screenshots\\"+"test_add123.png"))
            self.driver.close()
            self.driver.quit()
            assert False


    # def test_division(self):
    #     print("division")
    #     self.calcsession.find_element(By.NAME, "Four").click()
    #     self.calcsession.find_element(By.NAME, "Eight").click()
    #     self.calcsession.find_element(By.NAME, "Divide by").click()
    #     self.calcsession.find_element(By.NAME, "Six").click()
    #     self.calcsession.find_element(By.NAME, "Equals").click()
    #     self.assertEqual(self.getDisplayResults(), "8")

    # def test_multiplication(self):
    #     print("multiplication")
    #     self.calcsession.find_element(By.NAME, "Eight").click()
    #     self.calcsession.find_element(By.NAME, "Multiply by").click()
    #     self.calcsession.find_element(By.NAME, "Six").click()
    #     self.calcsession.find_element(By.NAME, "Equals").click()
    #     self.assertEqual(self.getDisplayResults(), "48")

    def getDisplayResults(self):
        text = self.driver.find_element_by_accessibility_id("CalculatorResults").text
        text = text.strip("Display is ").rstrip(' ').lstrip(' ')
        return text

    def ChooseCalculator(self, locator):
        self.driver.find_element_by_accessibility_id("TogglePaneButton").click()
        listElement = self.driver.find_elements_by_class_name("ListViewItem")
        for l in listElement:
            if l.get_attribute("AutomationId") == locator:
                l.click()
                break

    def test_choosecaculator(self):
        self.ChooseCalculator("Scientific")
#        self.calcsession.find_element(By.NAME, "Equals").click()

    def ChooseCalculatorXpath(self, locator):
        self.driver.find_element_by_accessibility_id("TogglePaneButton").click()
        listElement = self.driver.find_elements_by_xpath("//ListItem")
        for l in listElement:
            if l.get_attribute("AutomationId") == locator:
                l.click()
                break

    def test_choosecaculatorxpath(self):
        self.ChooseCalculatorXpath("Scientific")
#        self.calcsession.find_element(By.NAME, "Equals").click()