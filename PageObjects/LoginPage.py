from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        self.dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")

    def  enter_username(self, username):
        username_input_field = self.wait.until(EC.visibility_of_element_located(self.username_field))
        username_input_field.clear()
        username_input_field.send_keys(username)

    def enter_password(self, password):
        password_input_field = self.wait.until(EC.visibility_of_element_located(self.password_field))
        password_input_field.clear()
        password_input_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self.login_button))
        login_button.click()

    def perform_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_dashboard_loaded(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.dashboard_header))
            return True
        except:
            return False
