from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.txtUserName = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        self.txtPassword = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        self.btnLogin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[type=submit]")))
        self.lblInvalidCreds = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    
    def doLogin(self, username, password):
        self.txtUserName.send_keys(username)
        self.txtPassword.send_keys(password)
        self.btnLogin.click()
    
    def doLoginWithInvalidCreds(self, username, password):
        self.txtUserName.send_keys(username)
        self.txtPassword.send_keys(password)
        self.btnLogin.click()
        return self.lblInvalidCreds.text
