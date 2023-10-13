from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.btnProfileTab = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-userdropdown-tab")))
        self.logOutLink = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Logout")))
        self.menus = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "oxd-main-menu-item--name")))
    
    def doLogout(self):
        self.btnProfileTab.click()
        self.logOutLink.click()
