# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import random
import pandas
import datetime as dt
import smtplib


def send_bday_email(new_content):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="j00hoon1101@gmail.com",
            msg=f"Subject:Happy bday!!!\n\n{new_content}"
        )


my_email = "j00hoon1101@gmail.com"
password = "btpygqgeztdqczhl"

today = dt.datetime.now()
today_tuple = (today.month, today.day)
# month = dt.datetime.now().month
# day = dt.datetime.now().day
#today = (month, day)

try:
    data = pandas.read_csv("birthdays.csv")
except FileNotFoundError:
    print("No b'days.csv file!")
else:
    bday_dict = {(data["month"], data["day"]):data for (index, data) in data.iterrows()}

    if today_tuple in bday_dict: # check month and day
        name = bday_dict[today_tuple]["name"]
        with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as letter_format: # open letter file
            content = letter_format.read()
        new_content = content.replace('[NAME]', name) # replace with a real name

        # send email with bday message
        send_bday_email(new_content)

