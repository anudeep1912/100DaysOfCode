from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

s = Service('D:\\Anudeep\\100DaysOfCode\\Development\\chromedriver')

driver = webdriver.Chrome(service=s)

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(2)




# while True:
#     cookie = driver.find_element(By.ID, "bigCookie")
#     cookie.click()
#     current_score = driver.find_element(By.ID, "cookies").text.split()[0]

    # for option in available_options[::-1]:
    #     if int(option.find_element(By.CLASS_NAME, "price").text) < int(current_score):
    #         print(int(option.find_element(By.CLASS_NAME, "price").text) < int(current_score))
    #         option.click()

cookie = driver.find_element(By.ID, "bigCookie")
for i in range(30):
    cookie.click()
available_options = driver.find_element(By.CSS_SELECTOR, ".product locked disabled toggledOff")
print(available_options)