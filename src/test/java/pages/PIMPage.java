from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.button = driver.find_elements(By.CLASS_NAME, "oxd-button--secondary")
        self.txtFirstName = driver.find_element(By.CSS_SELECTOR, "[name=firstName]")
        self.txtLastName = driver.find_element(By.CSS_SELECTOR, "[name=lastName]")
        self.txtEmployeeId = driver.find_elements(By.CLASS_NAME, "oxd-input")
        self.btnToggle = driver.find_element(By.CLASS_NAME, "oxd-switch-input")
        self.txtUserName = driver.find_elements(By.TAG_NAME, "input")
        self.txtPassword = driver.find_elements(By.TAG_NAME, "input")
        self.txtConfirmPassword = driver.find_elements(By.TAG_NAME, "input")
        self.Submit = driver.find_element(By.CSS_SELECTOR, "[type=submit]")
        self.txtSearchEmpName = driver.find_elements(By.TAG_NAME, "input")
        self.btnUpdateEmployee = driver.find_elements(By.TAG_NAME, "button")
        self.txtUpdateEmployeeId = driver.find_elements(By.CLASS_NAME, "oxd-input")

    def createEmployee(self, firstname, lastname, employeeId, username, password):
        self.txtFirstName.send_keys(firstname)
        self.txtLastName.send_keys(lastname)
        empID = self.txtEmployeeId[4]
        empID.clear()
        empID.send_keys(employeeId)
        self.btnToggle.click()
        self.txtUserName[7].send_keys(username)
        self.txtPassword[10].send_keys(password)
        self.txtConfirmPassword[11].send_keys(password)
        self.Submit.click()

    def createEmployeeWithoutUsername(self, firstname, lastname, employeeId, password):
        self.txtFirstName.send_keys(firstname)
        self.txtLastName.send_keys(lastname)
        empID = self.txtEmployeeId[4]
        empID.clear()
        empID.send_keys(employeeId)
        self.btnToggle.click()
        self.txtPassword[10].send_keys(password)
        self.txtConfirmPassword[11].send_keys(password)
        self.Submit.click()

    def searchEmployeeByInvalidName(self, employeeName):
        self.txtSearchEmpName[1].send_keys(employeeName)
        self.Submit.click()

    def searchEmployeeByValidName(self, employeeName):
        self.txtSearchEmpName[1].send_keys(employeeName)
        self.Submit.click()

    def updateEmployeeById(self, employeeId):
        self.btnUpdateEmployee[6].click()
        self.txtUpdateEmployeeId[5].clear()
        self.txtUpdateEmployeeId[5].send_keys(employeeId)
        self.btnUpdateEmployee[1].click()

    def searchEmployeeByValidId(self, randomEmployeeId):
        self.txtEmployeeId[1].send_keys(randomEmployeeId)
        self.Submit.click()
