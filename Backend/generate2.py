
from generate import users
import os
import requests
import random
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials


script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)
gc = gspread.service_account(filename='credentials.json')

spreadsheet = gc.open_by_key("10RDxyuBw5ygMn79vQA5aove-bzjDJ9mNWblUO0SK-xw")
worksheet = spreadsheet.get_worksheet(0)  # assuming we're working on the first worksheet

# Get the total number of columns
num_cols = len(worksheet.row_values(1))  # gets number of columns by checking the number of values in the first row

def get_random_image_url(keyword):
    # Replace 'your_access_key' with your actual Unsplash Access Key
    response = requests.get(f'https://api.unsplash.com/photos/random?query={keyword}&client_id=NEF2IgZ7OayWZnMJGb9HbKua-ru5623fRuKS6L6oFt4')
    data = response.json()
    print(data['urls']['small'])
    return data['urls']['small']  # Return the URL of a smaller version of the image for efficiency

for user_id, user_data in users.items():
    if user_data['gender'] == 'male':
        user_data['profile_pic'] = get_random_image_url('man')
    elif user_data['gender'] == 'female':
        user_data['profile_pic'] = get_random_image_url('woman')
    worksheet.append_row([user_data['name'], user_data['gender'], user_data['age'], user_data['genderPreference'],
                          ','.join(user_data['interests']), user_data['ageGroupPreference'], user_data['bio'], user_data['profile_pic']])
    time.sleep(5)

data = [[user_data['profile_pic']] for user_data in users.values()]
with open("generate.py", "w") as outfile:
    outfile.write("users = %s" % users)

worksheet.append_row
