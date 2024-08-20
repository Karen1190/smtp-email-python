import datetime as dt
import random
import smtplib

my_email = "karen119054@gmail.com"
password = "xczu htyk oezk pgts"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs="ostad7test@gmail.com",
#                     msg="Subject:Hello\n\nThis is smtplib")
# connection.close()
now = dt.datetime.now()
weekday = now.weekday()
for i in range(1):
    if weekday == 1:
        with open("quotes.txt") as a:
            b = a.readlines()
            c = random.choice(b)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="karen119054@gmail.com",
                                msg=f"Subject:Hello\n\n{c}")
