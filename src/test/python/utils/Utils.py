import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Utils:
    @staticmethod
    def do_scroll(driver, height_pixel):
        driver.execute_script("window.scrollBy(0," + str(height_pixel) + ")")

    @staticmethod
    def load_json_file(file_location):
        with open(file_location, 'r') as file:
            return json.load(file)

    @staticmethod
    def load_json_file_containing_array(file_location, index):
        with open(file_location, 'r') as file:
            data = json.load(file)
            return data[index]

    @staticmethod
    def wait_for_element(driver, element, time_unit_seconds):
        wait = WebDriverWait(driver, time_unit_seconds)
        wait.until(EC.visibility_of(element))

    @staticmethod
    def generate_random_number(min_val, max_val):
        import random
        return random.randint(min_val, max_val)

    @staticmethod
    def add_json_array(first_name, last_name, employee_id, username, password):
        file_name = "./src/test/resources/Employee.json"
        with open(file_name, 'r') as file:
            data = json.load(file)
            user_obj = {
                "firstname": first_name,
                "lastname": last_name,
                "employeeId": employee_id,
                "username": username,
                "password": password
            }
            data.append(user_obj)
        with open(file_name, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def update_json_object(file_name, key, value, index):
        with open(file_name, 'r') as file:
            data = json.load(file)
            data[index][key] = value
        with open(file_name, 'w') as file:
            json.dump(data, file)

# Example usage
if __name__ == "__main__":
    user_object = Utils.load_json_file("./src/test/resources/Admin.json")
    username = user_object["username"]
    password = user_object["password"]
    print(username)
    print(password)
