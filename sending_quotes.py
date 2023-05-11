import smtplib
import datetime
import random

aking_email = 'carleyeshield21@gmail.com'
password = 'qtqwejktaeqkldps'

time_now = datetime.datetime.now()
weekday = time_now.weekday()
print(weekday)

if weekday == 3 or weekday == 4:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote_for_today = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as kuneksyon:
        kuneksyon.starttls()
        kuneksyon.login(aking_email,password)
        kuneksyon.sendmail(from_addr=aking_email, to_addrs=aking_email,msg=f'Subject: Mutibasyon\n\n{quote_for_today}')