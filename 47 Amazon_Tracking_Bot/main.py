from bs4 import BeautifulSoup
import requests
#import lxml
import smtplib

PRODUCT_URL = "https://www.amazon.in/dp/B088F98GGH/ref=cm_sw_em_r_mt_dp_46BSY692QM1T7J77W3J9"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get(url=PRODUCT_URL, headers=headers)
product_html = response.text
soup = BeautifulSoup(product_html, "lxml")
price_text = soup.find(name="span", class_="a-price-whole")
title = soup.find(name="span", class_="a-size-large product-title-word-break")
product_title = title.text.strip()
price = int(price_text.getText()[:-1].replace(",", ""))

email = "test@gmail.com"
password = "123456"

if price < 8000:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(to_addrs="youremail@gmail.com",
                            from_addr=email,
                            msg=f"Subject:Price Drop: {product_title}\n\n{product_title}\nNew Price: {price}\nlink: {PRODUCT_URL}")




