import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
username=input("enter username")
password=input("enter password")
driver= webdriver.Chrome(ChromeDriverManager().install())
print("Test Case Started")
driver.maximize_window()
driver.get("https://www.instagram.com/?hl=en")
time.sleep(1)
driver.find_element_by_name("username").send_keys(username)
time.sleep(1)
driver.find_element_by_name("password").send_keys(password)
time.sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)
driver.close()
print("test is sucesfully conducted")