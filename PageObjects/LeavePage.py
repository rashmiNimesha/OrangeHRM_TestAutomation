from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.leave_menu_xpath = "//span[text()='Leave']/parent::a"

    def navigate_to_leave(self):
        leave_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.leave_menu_xpath)))
        leave_menu.click()

    def verify_leave_page(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Leave']")))
        print("Successfully navigated to the Leave page.")
