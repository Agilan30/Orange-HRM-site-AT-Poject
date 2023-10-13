import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages import DashboardPage, LoginPage, EmployeeInfoPage
from utils import Utils

class TestEmployeeRunner:

    @pytest.fixture(scope="class")
    def setup(self):
        driver = webdriver.Chrome(executable_path="./path/to/chromedriver")
        yield driver
        driver.quit()

    @pytest.mark.run(order=1)
    def test_login_with_second_users(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        user_object = Utils.load_json_file_containing_array("./src/test/resources/Employee.json", 1)
        username = user_object.get("username")
        password = user_object.get("password")
        login_page.do_login(username, password)
        driver.implicitly_wait(10)

        # Assertion
        header_text = driver.find_element(By.TAG_NAME, "h6").text
        assert header_text == "Dashboard"

    @pytest.mark.run(order=2)
    def test_update_user_information(self, setup):
        driver = setup
        employee_info_page = EmployeeInfoPage(driver)
        employee_info_page.user_menu[2].click()
        Utils.do_scroll(driver, 500)
        employee_info_page.select_gender()
        driver.implicitly_wait(1)
        Utils.do_scroll(driver, 500)
        employee_info_page.select_blood_type()
        driver.refresh()
        driver.implicitly_wait(1)
        employee_info_page.select_contact()
        driver.implicitly_wait(1)

        # Assertion
        header_text = driver.find_element(By.TAG_NAME, "h6").text
        assert header_text == "PIM"

    @pytest.mark.run(order=3)
    def test_logout(self, setup):
        driver = setup
        dashboard_page = DashboardPage(driver)
        dashboard_page.do_logout()
