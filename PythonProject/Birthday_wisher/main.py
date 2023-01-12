import smtplib
import datetime as dt
import random

my_email = "j00hoon1101@gmail.com"
password = "btpygqgeztdqczhl"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="j00hoon1101@gmail.com",
#         msg="Subject:Maichann~~ baka~~~\n\nThis is the body"
#     )




# bday = dt.datetime(year=1989, month=11, day=1)


now = dt.datetime.now().weekday()

# check today is whether Tuesday or not
if now == 1:
    with open("quotes.txt") as quotes_list:
        all_quotes = quotes_list.readlines()

    today_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="j00hoon1101@gmail.com",
            msg=f"Subject:Today's quote\n\n{today_quote}"
        )




