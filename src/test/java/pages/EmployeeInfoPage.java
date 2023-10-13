import time
from faker import Faker
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class EmployeeInfoPage:
    def __init__(self, driver):
        self.driver = driver
        self.userMenu = driver.find_elements_by_class_name("oxd-main-menu-item")
        self.btnRadio = driver.find_elements_by_class_name("oxd-radio-input")
        self.dropdown = driver.find_elements_by_class_name("oxd-select-text-input")
        self.contactDetails = driver.find_elements_by_class_name("orangehrm-tabs-item")
        self.txtInput = driver.find_elements_by_class_name("oxd-input")
        self.dropdownCountry = driver.find_element_by_class_name("oxd-select-text-input")
        self.Submit = driver.find_elements_by_css_selector("[type=submit]")

    def selectGender(self):
        self.btnRadio[1].click()
        time.sleep(1.5)
        self.Submit[0].click()

    def selectBloodType(self):
        dropdown = Select(self.dropdown[2])
        dropdown.select_by_index(1)
        time.sleep(1)
        dropdown.select_by_index(2)
        time.sleep(1)
        dropdown.select_by_index(3)
