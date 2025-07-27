from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

URL = "http://localhost:3000"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def login(driver, username, password):
    driver.get(f"{URL}/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-btn").click()

def test_login_valid(driver):
    login(driver, "admin", "admin")
    assert "dashboard" in driver.current_url

def test_login_invalid(driver):
    login(driver, "admin", "wrongpass")
    assert "Invalid credentials" in driver.page_source

def test_create_item(driver):
    login(driver, "admin", "admin")
    driver.find_element(By.ID, "new-item").send_keys("My Task")
    driver.find_element(By.ID, "add-btn").click()
    time.sleep(1)
    assert "My Task" in driver.page_source

def test_edit_item(driver):
    login(driver, "admin", "admin")
    driver.find_element(By.CSS_SELECTOR, ".edit-btn").click()
    input_box = driver.find_element(By.CSS_SELECTOR, ".edit-input")
    input_box.clear()
    input_box.send_keys("Updated Task")
    driver.find_element(By.CSS_SELECTOR, ".save-btn").click()
    time.sleep(1)
    assert "Updated Task" in driver.page_source

def test_delete_item(driver):
    login(driver, "admin", "admin")
    driver.find_element(By.CSS_SELECTOR, ".delete-btn").click()
    time.sleep(1)
    assert "Updated Task" not in driver.page_source