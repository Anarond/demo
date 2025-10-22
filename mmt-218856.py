from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import json

with open("config.json", "r") as f:
    config = json.load(f)

def test_scenario():
    username = config["username"]
    password = config["password"]
    url = config["url"]

    driver = webdriver.Chrome()
    driver.get(url)

        login_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]'))
    )
    login_field.send_keys(username)

    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
    password_field.send_keys(password)

    enter_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="mp-btn_default-login-enter"]')))
    enter_button.click()

    settings_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Настройки')]")))
    settings_button.click()

    bp_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Бизнес-процессы')]")))
    bp_button.click()

    bp_list_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Схемы процессов')]")))
    bp_list_button.click()

    test_bp1_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'test bp1')]")))
    test_bp1_button.click()
    time.sleep(4)
    iframe = driver.find_element(By.NAME, "reactBrowserFrame")
    driver.switch_to.frame(iframe)

    add_scenario_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Добавление сценария')]")))
    add_scenario_button.click()

    #driver.switch_to.default_content()

    time.sleep(111)
    #driver.find_element(By.XPATH, '//*[@id="login"]').send_keys(username)
    #driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    #driver.find_element(By.XPATH, '//*[@id="mp-btn_default-login-enter"]').click()
