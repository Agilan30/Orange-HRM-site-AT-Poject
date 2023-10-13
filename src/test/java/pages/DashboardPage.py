from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.btnProfileTab = self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name")
        self.linkLogout = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")
        self.menus = self.driver.find_elements(By.CLASS_NAME, "oxd-text--span")
        self.dropdown = self.driver.find_elements(By.CLASS_NAME, "oxd-select-text-input")
        self.employeeName = self.driver.find_elements(By.TAG_NAME, "input")

    def doLogout(self):
        self.btnProfileTab.click()
        self.linkLogout.click()
