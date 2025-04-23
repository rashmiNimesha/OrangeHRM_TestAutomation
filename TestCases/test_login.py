import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage

base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
username = "Admin"
password = "admin123"

@pytest.mark.run(order=1)
def test_verify_login_function():
    driver = webdriver.Chrome()
    driver.get(base_url)

    # Perform login
    login_page = LoginPage(driver)
    login_page.perform_login(username, password)

    # Verify that the dashboard page is loaded
    assert login_page.is_dashboard_loaded() is True, "Login failed or Dashboard page failed to load"

    driver.quit()