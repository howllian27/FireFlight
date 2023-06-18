# from faker import Faker
# import random
# import gspread
# import os
# import time

# fake = Faker()

# # Define the possible interests and ageGroupPreferences.
# interests = ["beach", "history", "adventure", "nature", "shopping", "food", "nightlife", "cultural"]
# ageGroupPreferences = ["18-25", "26-35", "36-45", "46-55", "56+"]

# def generate_user(user_id):
#     # Randomly generate the data.
#     name = fake.name()
#     gender = random.choice(["male", "female"])
#     age = random.randint(18, 60)
#     genderPreference = random.choice(["male", "female"])
#     user_interests = random.sample(interests, random.randint(1, len(interests)))  # At least one interest, could be more
#     ageGroupPreference = random.choice(ageGroupPreferences)

#     return {
#         'userID': user_id,
#         'name': name,
#         'gender': gender,
#         'age': age,
#         'genderPreference': genderPreference,
#         'interests': ", ".join(user_interests),  # Convert list to comma-separated string.
#         'ageGroupPreference': ageGroupPreference,
#         'bio': fake.text()  # Randomly generated text as bio
#     }

# # Generate the users.
# users = {}
# for i in range(1, 501):  # IDs from 1 to 500.
#     user_id = f"user{i}"
#     users[user_id] = generate_user(user_id)

# script_dir = os.path.dirname(os.path.realpath(__file__))
# os.chdir(script_dir)
# with open("generate.py", "w") as outfile:
#     outfile.write("users = %s" % users)

# print(users)

# # Assuming you have the credentials file and its path is in your environment variable.
# gc = gspread.service_account(filename="credentials.json")

# # Open the Google spreadsheet where you want to store the data.
# spreadsheet = gc.open_by_key("10RDxyuBw5ygMn79vQA5aove-bzjDJ9mNWblUO0SK-xw")

# # Select the first sheet in the spreadsheet.
# worksheet = spreadsheet.get_worksheet(0)

# # Define the column headers.
# column_headers = ['userID', 'name', 'gender', 'age', 'genderPreference', 'interests', 'ageGroupPreference', 'bio']

# # Write the column headers to the first row of the spreadsheet.
# worksheet.append_row(column_headers)

# # Write the user data to the spreadsheet.
# for user_id, user in users.items():
#     row = [user[column] for column in column_headers]
#     worksheet.append_row(row)
#     time.sleep(1)

from generate import users
import os

for user in users:
    users[user]['interests'] = users[user]["interests"].split(",")

script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)
with open("generate.py", "w") as outfile:
    outfile.write("users = %s" % users)