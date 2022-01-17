from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

s = Service('D:\\Anudeep\\100DaysOfCode\\Development\\chromedriver')

driver = webdriver.Chrome(service=s)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()                                        # Open the site and maximize window
cookie = driver.find_element(By.ID, "cookie")                   # Get Cookie Element

# Get all upgrade element id's and form a list
menu = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_list = [item.get_attribute("id") for item in menu]

#  timeout of 5 secs
timeout = time.time() + 5

five_minutes = time.time() + 5*60

while True:

    cookie.click()

    if time.time() > timeout:
        # Get Prices of all items
        item_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices_list = []

        # format the item prices and add it to the list
        for price in item_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices_list.append(cost)

        # Create a Dict with Item prices and Id's
        upgrades_dict = {}
        for i in range(len(item_prices_list)):
            upgrades_dict[item_prices_list[i]] = item_list[i]

        # Get current cookie count
        current_score_text = driver.find_element(By.ID, "money").text
        if "," in current_score_text:
            current_score_text = current_score_text.replace(",", "")
        current_score = int(current_score_text)

        # finding upgrades we can currently afford
        affordable_upgrades = {}
        for cost, upgrade in upgrades_dict.items():
            if cost < current_score:
                affordable_upgrades[cost] = upgrade

        # Purchase the highest price upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        # Increase the time to another 5 secs
        timeout = time.time() + 5

    # Quit after 5 minutes and get the cps value
    if time.time() > five_minutes:
        cps = driver.find_element(By.ID, "cps")
        print(cps.text)
        break
        
driver.quit()
