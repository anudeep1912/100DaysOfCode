from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

s = Service('D:\\Anudeep\\100DaysOfCode\\Development\\chromedriver')

driver = webdriver.Chrome(service=s)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

first_name.send_keys("Abcdef")
last_name.send_keys("Ghijkl")
email.send_keys("Abcdef.Ghijkl@gmail.com")

driver.find_element(By.XPATH, "/html/body/form/button").click()

time.sleep(5)

driver.quit()
