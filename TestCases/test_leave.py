import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.LeavePage import LeavePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.run(order=2)
def test_leave_section_access():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


    # Perform login
    login_page = LoginPage(driver)
    login_page.perform_login("Admin", "admin123")

    WebDriverWait(driver, 14).until(
        EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )

    # Initialize LeavePage and navigate to Leave
    leave_page = LeavePage(driver)
    leave_page.navigate_to_leave()

    # Verify successful navigation to the Leave page
    leave_page.verify_leave_page()

    driver.quit()
