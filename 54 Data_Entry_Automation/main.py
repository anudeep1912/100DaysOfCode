from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import requests

GOOGLE_FORM_URL = "https://forms.gle/1W19bUyvNjCRr6XQ6"
ZILLOW_URL = "https://www.zillow.com/ny/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.59279440625%2C%22east%22%3A-69.94728659375%2C%22south%22%3A39.11961507181684%2C%22north%22%3A46.251601376670315%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A556737%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A2000%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D"

# Headers needed to access the Zillow URL
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url=ZILLOW_URL, headers=headers)
zillow_html = response.text
# Create a Soup Using the Html obtained
soup = BeautifulSoup(zillow_html, "lxml")

# Extract all the address into a list
addresses = soup.find_all(name="address", class_="list-card-addr")
address_list = [address.text for address in addresses]

# Extract all the prices into a list
prices = soup.find_all(name="div", class_="list-card-price")
prices_list = [int(price.text[1:6].replace(",", "")) for price in prices]

# Extract all the links into a list
links = soup.find_all(name="a", class_="list-card-link")
links_list = []
for link in links:
    link_text = link.get("href")
    if link_text not in links_list:
        if "zillow" in link_text:
            links_list.append(link_text)
        else:
            links_list.append("https://www.zillow.com/" + link_text)

print(links_list)

# Create a web driver for chrome browser and open the google form
s = Service('D:\\Anudeep\\100DaysOfCode\\Development\\chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")

# For each entry open a new form and fill the data
for n in range(len(prices_list)):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 't')
    driver.get(GOOGLE_FORM_URL)
    time.sleep(5)
    question_1 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question_2 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question_3 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    question_1.send_keys(address_list[n])
    question_2.send_keys(prices_list[n])
    question_3.send_keys(links_list[n])
    submit_button.click()
    time.sleep(2)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 'w')

# close all the browser
driver.quit()



