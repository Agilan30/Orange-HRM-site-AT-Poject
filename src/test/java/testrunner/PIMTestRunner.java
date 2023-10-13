import time
import json
import random
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class PIMTestRunner(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  
        self.driver.get("your_login_page_url_here") 

    def test_doLoginWithInvalidCreds(self):
        login_page = LoginPage(self.driver)
        message_actual = login_page.doLoginWithInvalidCreds("admin", "wrong password")
        message_expected = "Invalid credentials"
        self.assertTrue(message_expected in message_actual)
        time.sleep(1.5)

    def test_doLogin(self):
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        username, password = self.get_credentials()
        login_page.doLogin(username, password)

        # Assertion
        header_text = self.driver.find_element_by_tag_name("h6").text
        header_expected = "Dashboard"
        self.assertEqual(header_text, header_expected)
        time.sleep(1.5)
        dashboard_page.menus[1].click()
        time.sleep(1.5)



    def tearDown(self):
        self.driver.close()

    def get_credentials(self):
        pass

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def doLoginWithInvalidCreds(self, username, password):
        pass

    def doLogin(self, username, password):
        pass

class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.menus = []  
    
if __name__ == "__main__":
    unittest.main()
