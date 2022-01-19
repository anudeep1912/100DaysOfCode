from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

s = Service('D:\\Anudeep\\100DaysOfCode\\Development\\chromedriver')

driver = webdriver.Chrome(service=s)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&keywords=python%20developer")

time.sleep(2)
login_button = driver.find_element(By.CLASS_NAME, "cta-modal__primary-btn")
login_button.click()

time.sleep(2)
username = driver.find_element(By.NAME, "session_key")
username.send_keys("stylishstardeepu@gmail.com")
password = driver.find_element(By.NAME, "session_password")
password.send_keys("Lazyspider@123")
password.send_keys(Keys.ENTER)

all_jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for job in all_jobs:

    job.click()

    job_save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
    job_save_button.click()
    time.sleep(10)


    # try:
    #     follow_button = driver.find_element(By.CSS_SELECTOR, ".follow")
    #     follow_button.click()
    # except:
    #     continue



