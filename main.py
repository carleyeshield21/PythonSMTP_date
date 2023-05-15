#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explanations.


from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "carleyeshield21@gmail.com"
MY_PASSWORD = "qtqwejktaeqkldps"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
print(today)
# birthday_dict = {
#     (bithday_month, birthday_day): data_row
# }

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
list = [data_row for (index, data_row) in data.iterrows()]
# print(birthdays_dict)
# print(list)

# file_dict = {(row["name"],row['email']) for(index,row) in data.iterrows()}
# file_dict2 = {(row["name"],row['email']):row["year"] for(index,row) in data.iterrows()}
# print(file_dict)
# print(file_dict2)

# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )
