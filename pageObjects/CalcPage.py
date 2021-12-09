# 2021 Dec 5 - CalcPage.py
# Elliot Erstein
# Page Object Model (POM) implementation for example calculator. Examples show different methods of how
# to find elements and select/input information. Elements are passed from this
# page to the test cases located in testCases package.
class CalcPage:
    def __init__(self,driver):
        self.driver=driver
# Calculator Numbers
    def calcZero(self):
        return self.driver.find_element_by_name("Zero")

    def calcOne(self):
        return self.driver.find_element_by_name("One")

    def calcTwo(self):
        return self.driver.find_element_by_name("Two")

    def calcThree(self):
        return self.driver.find_element_by_name("Three")

    def calcFour(self):
        return self.driver.find_element_by_name("Four")

    def calcFive(self):
        return self.driver.find_element_by_name("Five")

    def calcSix(self):
        return self.driver.find_element_by_name("Six")

    def calcSeven(self):
        return self.driver.find_element_by_name("Seven")

    def calcEight(self):
        return self.driver.find_element_by_name("Eight")

    def calcNine(self):
        return self.driver.find_element_by_name("Nine")
# Calculator Operators
    def calcEquals(self):
        return self.driver.find_element_by_name("Equals")

    def calcPlus(self):
        return self.driver.find_element_by_name("Plus")

    def calcMinus(self):
        return self.driver.find_element_by_name("Minus")

    def calcDivide(self):
        return self.driver.find_element_by_name("Divide by")

    def calcMultiply(self):
        return self.driver.find_element_by_name("Multiply by")
# Calculator Results
    def getDisplayResults(self):
        text = self.driver.find_element_by_accessibility_id("CalculatorResults").text
        text = text.strip("Display is ").rstrip(' ').lstrip(' ')
        return text