import pandas
import datetime as dt
import random
import smtplib

email = "test@gmail.com"
password = "123456"

# Get today's Date
today_date = dt.datetime.now()
current_year = today_date.year
current_day = today_date.day
current_month = today_date.month

# Reading the Birthday csv file and converting to a dict
data = pandas.read_csv("birthdays.csv")
birthday_dict = data.to_dict(orient="records")


# Loop through the birthday dict and check if Any of the birthdays occur today
for entry in birthday_dict:
    if entry["year"] == current_year and entry["day"] == current_day and entry["month"] == current_month:
        # If there is a birthday today choose a random letter format
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
            letter_content = letter_file.read()
            new_letter_content = letter_content.replace("[NAME]", entry["name"])
        # replace the placeholder in letter content and send an email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(to_addrs=entry["email"], from_addr=email, msg=f"Subject:Happy BirthDay!\n\n{new_letter_content}")


# This code can be used online on python anywhere and can be made to ru everyday.






