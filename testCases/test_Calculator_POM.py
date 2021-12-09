# 2021 Dec 5 - test_Calculator.py
# Example testing calculator using winAppdriver. This test does not follow the Page Object Model (POM) format and
# directly finds and selects the elements within the test case.
import pytest
from utilities.customLogger import LogGen
from pageObjects.CalcPage import CalcPage

class Test_Calculator_B:

    logger = LogGen.loggen()

    @pytest.mark.calc
    def test_add(self,setup):
        self.driver = setup
        self.cp = CalcPage(self.driver)
        self.cp.calcOne().click()
        self.cp.calcTwo().click()
        self.cp.calcPlus().click()
        self.cp.calcNine().click()
        self.cp.calcEquals().click()
        results = self.cp.getDisplayResults()
        if results == "21":
            self.logger.info("**** Addition test passed ****")
            self.driver.close()
            self.driver.quit()
            assert True
        else:
            self.logger.error("**** Addition test failed****")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addition.png")
            self.driver.close()
            self.driver.quit()
            assert False

    @pytest.mark.calc
    def test_subtraction(self,setup):
        self.driver = setup
        self.cp = CalcPage(self.driver)
        self.cp.calcOne().click()
        self.cp.calcTwo().click()
        self.cp.calcMinus().click()
        self.cp.calcNine().click()
        self.cp.calcEquals().click()
        results = self.cp.getDisplayResults()
        if results == "13":
            self.logger.info("**** Subtraction test passed ****")
            self.driver.close()
            self.driver.quit()
            assert True
        else:
            self.logger.error("**** Subtraction test failed****")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_subtraction.png")
            self.driver.close()
            self.driver.quit()
            assert False

    @pytest.mark.calc
    def test_division(self, setup):
        self.driver = setup
        self.cp = CalcPage(self.driver)
        self.cp.calcFour().click()
        self.cp.calcEight().click()
        self.cp.calcDivide().click()
        self.cp.calcEight().click()
        self.cp.calcEquals().click()
        results = self.cp.getDisplayResults()
        if results == "6":
            self.logger.info("**** Division test passed ****")
            self.driver.close()
            self.driver.quit()
            assert True
        else:
            self.logger.error("**** Division test failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_division.png")
            self.driver.close()
            self.driver.quit()
            assert False

    @pytest.mark.calc
    def test_multiplication(self, setup):
        self.driver = setup
        self.cp = CalcPage(self.driver)
        self.cp.calcEight().click()
        self.cp.calcMultiply().click()
        self.cp.calcSix().click()
        self.cp.calcEquals().click()
        results = self.cp.getDisplayResults()
        if results == "48":
            self.logger.info("**** Multiplication test passed ****")
            self.driver.close()
            self.driver.quit()
            assert True
        else:
            self.logger.error("**** Multiplication test failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_multiplication.png")
            self.driver.close()
            self.driver.quit()
            assert False

    # def getDisplayResults(self):
    #     text = self.driver.find_element_by_accessibility_id("CalculatorResults").text
    #     text = text.strip("Display is ").rstrip(' ').lstrip(' ')
    #     return text

#     def ChooseCalculator(self, locator):
#         self.driver.find_element_by_accessibility_id("TogglePaneButton").click()
#         listElement = self.driver.find_elements_by_class_name("ListViewItem")
#         for l in listElement:
#             if l.get_attribute("AutomationId") == locator:
#                 l.click()
#                 break
#
#     def test_choosecaculator(self):
#         self.ChooseCalculator("Scientific")
# #        self.calcsession.find_element(By.NAME, "Equals").click()
#
#     def ChooseCalculatorXpath(self, locator):
#         self.driver.find_element_by_accessibility_id("TogglePaneButton").click()
#         listElement = self.driver.find_elements_by_xpath("//ListItem")
#         for l in listElement:
#             if l.get_attribute("AutomationId") == locator:
#                 l.click()
#                 break
#
#     def test_choosecaculatorxpath(self):
#         self.ChooseCalculatorXpath("Scientific")
# #        self.calcsession.find_element(By.NAME, "Equals").click()