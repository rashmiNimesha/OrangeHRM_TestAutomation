import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.LogoutPage import LogoutPage

@pytest.mark.run(order=3)
def test_verify_logout_function():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page = LoginPage(driver)
    login_page.perform_login("Admin", "admin123")

    logout_page = LogoutPage(driver)
    logout_page.perform_logout()

    assert "login" in driver.current_url.lower()
    driver.quit()
