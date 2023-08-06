import random
import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest

driver = webdriver.Chrome()
driver.maximize_window()
fake = Faker()


def test_login():
    # driver = webdriver.Chrome()
    # driver.maximize_window()

    driver.get("http://localhost/hms/project/view/login.php")

    email = driver.find_element(By.ID, "id")
    email.send_keys("N-1")

    passwd = driver.find_element(By.ID, "password")
    passwd.send_keys("123")

    submit = driver.find_element(By.ID, "submit")
    submit.click()
    success_message = driver.find_element(By.LINK_TEXT, 'Log out')
    assert "Log out" in success_message.text
    # driver.close()


def test_register_admin():
    # driver = webdriver.Chrome()
    # driver.maximize_window()

    driver.get("http://localhost/hms/project/view/newPatientReg.php")
    profile = fake.simple_profile()

    username = driver.find_element(By.NAME, "pName")
    username.send_keys(profile["username"])

    password = driver.find_element(By.NAME, "nppassword")
    password.send_keys("456")

    cpassword = driver.find_element(By.NAME, "cpassword")
    cpassword.send_keys("456")

    contact = driver.find_element(By.NAME, "npContact")
    contact.send_keys(fake.pyint(11111111111, 99999999999))

    acontact = driver.find_element(By.NAME, "contactNo")
    acontact.send_keys(fake.pyint(11111111111, 99999999999))

    age = driver.find_element(By.NAME, "npAge")
    age.send_keys(random.randint(18, 50))

    email = driver.find_element(By.NAME, "npEmail")
    email.send_keys(profile["mail"])

    email = driver.find_element(By.NAME, "occupation")
    email.send_keys(fake.pystr())

    address = driver.find_element(By.NAME, "npAddress")
    address.send_keys(fake.pystr())

    gender = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='male']")
    gender.click()

    submit = driver.find_element(By.ID, "submit")
    submit.click()

    time.sleep(1)

    obj = driver.switch_to.alert
    obj.accept()