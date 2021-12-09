# 2021 Dec 4 - LoginPage.py
# Elliot Erstein Edit
# Page Object Model (POM) implementation for example login web page. Examples show different methods of how
# to find elements and select/input information to log in to the example website. Elements are passed from this
# page to the test cases located in testCases package.
class LoginPage:
    # Login Page
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//input[@value='Log in']" # this did not work
    button_login_class_name = "buttons" # added to fix xpath ^ error
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

  #  def clickLogin(self): # this method does not work for xpath
   #     self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogin(self):
        self.driver.find_element_by_class_name(self.button_login_class_name).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()