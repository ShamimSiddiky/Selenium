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
    #driver = webdriver.Chrome()
    #driver.maximize_window()

    driver.get("http://localhost/project/view/login.php")

    email = driver.find_element(By.ID, "id")
    email.send_keys("A-1")

    passwd = driver.find_element(By.ID, "password")
    passwd.send_keys("123")

    submit = driver.find_element(By.ID, "submit")
    submit.click()
    success_message = driver.find_element(By.LINK_TEXT, 'Log out')
    assert "Log out" in success_message.text
    #driver.close()

def test_register_admin():
    
    #driver = webdriver.Chrome()
    #driver.maximize_window()

    driver.get("http://localhost/project/view/registerAdmin.php")
    profile = fake.simple_profile()

    username = driver.find_element(By.NAME, "username")
    username.send_keys(profile["username"])

    password = driver.find_element(By.NAME, "password")
    password.send_keys(fake.pystr())

    gender = driver.find_element(By.ID, 'male')
    gender.click()

    age = driver.find_element(By.NAME, "age")
    age.send_keys(random.randint(18, 50))

    address = driver.find_element(By.NAME, "address")
    address.send_keys(fake.pystr())

    fname = driver.find_element(By.NAME, "fname")
    fname.send_keys(profile["name"].split(" ")[0])

    lname = driver.find_element(By.NAME, "lname")
    lname.send_keys(profile["name"].split(" ")[1])

    nid = driver.find_element(By.NAME, "nid")
    nid.send_keys(fake.pyint(1000000000000, 9999999999999))

    contact = driver.find_element(By.NAME, "contact")
    contact.send_keys(fake.pyint(11111111111, 99999999999))

    email = driver.find_element(By.NAME, "email")
    email.send_keys(profile["mail"])

    submit = driver.find_element(By.ID, "register")
    submit.click()
    
    time.sleep(0.5)

    success_message = driver.find_element(By.CLASS_NAME, "success").text
    assert "User insertion successful" in success_message
    
def test_edit_doctos():
    
    driver.get("http://localhost/project/view/editDoctors.php")
    ID = "D-1"
    
    id = driver.find_element(By.ID, "id")
    id.send_keys(ID)
    
    search = driver.find_element(By.ID, "search")
    search.click()
    
    profile = driver.find_element(By.ID, ID)
    profile.click()
    time.sleep(0.5)
    
    text = driver.find_element(By.ID, "text")
    text.send_keys(fake.pystr())
    
    update = driver.find_element(By.XPATH, "/html/body/div[@class='container']/div[@class='container-2']/div[@class='container-2b card']/div[@id='content']/div[@id='update']/button[@id='D-1']")
    update.click()
    
    time.sleep(0.5)
    
    success_message = driver.find_element(By.XPATH, "/html/body/div[@class='container']/div[@class='container-2']/div[@class='container-2b card']/div[@id='updatemsg']/small[@class='success']").text
    assert "Successfully updated!" in success_message
    
def test_update_profile():
    driver.get("http://localhost/project/view/editProfile.php")
    
    edit = driver.find_element(By.ID, "edit")
    edit.click()
    
    uname = "test"
    username = driver.find_element(By.ID, "username")
    username.clear()
    username.send_keys(uname)
    
    update = driver.find_element(By.ID, "update")
    update.click()
    
    driver.refresh();
    time.sleep(1)
    
    username = driver.find_element(By.ID, "username")
    updatedUname = username.get_attribute("value")
    
    assert uname in updatedUname
    driver.close()
