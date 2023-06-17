# from flask import Flask, request, jsonify
# from matchmaker import Matchmaker
# from generate import users
# import os

# app = Flask(__name__)
# matchmaker = Matchmaker(users, "matchmaking_model.pth")

# @app.route('/match', methods=['GET','POST'])
# def match():
#     if request.method == 'POST':
#         print("HI IM POST")
#         user = request.json['user']
#         matched_users = matchmaker.graph_matchmaking(user)
#         print(matched_users)
#         return jsonify(matched_users)
#     else:
#         print("HI IM NOT POST")
#         user = request.args.get('user')
#         if user:
#             matched_users = matchmaker.graph_matchmaking(user)
#             response = {'matched users': matched_users}
#             return jsonify(response)
#         else:
#             return jsonify({'error': 'Missing user parameter'})

# @app.route('/feedback', methods=['POST'])
# def feedback():
#     user = request.json['user']
#     matched_user = request.json['matched_user']
#     feedback_score = request.json['feedback_score']
#     matchmaker.collect_feedback(user, matched_user, feedback_score)
#     matchmaker.adjust_weights()
#     return jsonify({'status': 'success'})

# @app.route('/addUser', methods=['POST'])
# def add_user():
#     user = request.json['user']
#     gender = request.json['gender']
#     age = int(request.json['age'])
#     interests = request.json['interests']
#     ageGroupPreference = request.json['ageGroupPreference']
#     genderPreference = request.json['genderPreference']

#     if user not in users.keys():
#         print("This is the user: ", str(user))
#         users[user] = {'gender': gender, 'age': age, 'genderPreference': genderPreference, 'interests': interests, 'vacationType': 'History', 'hotel': 'Hotel 50', 'ageGroupPreference': ageGroupPreference, 'userID': user}
#         # Change the working directory to the Backend directory
#         os.chdir(os.path.dirname(os.path.abspath(__file__)))
#         outFile = open("generate.py","w")
#         outFile.write("users = %s" % (str(users)))
#         outFile.close()
#         matchmaker.add_user_and_update_graph(user)
#         return jsonify({'status': 'success'})
#     else:
#         print("This user id is alr taken! Try another")
#         return jsonify({'status': '404'})

# if __name__ == '__main__':
#     matchmaker.build_graph()
#     app.run(host='0.0.0.0', port=5000, debug=True)

from matchmaker import Matchmaker
import pandas as pd
import os
import ast
import gspread
import time

# Get the credentials and create a client to interact with the Google Sheets API
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)
gc = gspread.service_account(filename='credentials.json')

# Open the Google Spreadsheet by its ID (the string of random letters and numbers in the URL)
spreadsheet = gc.open_by_key("10RDxyuBw5ygMn79vQA5aove-bzjDJ9mNWblUO0SK-xw")

# Select the two sheets
sheet1 = spreadsheet.get_worksheet(0)  # users data is in the first sheet
sheet2 = spreadsheet.get_worksheet(1)  # matched users will be written in the second sheet

# Load users from generate.py
with open("generate.py", "r") as infile:
    users = ast.literal_eval(infile.read().split(" = ")[1])

matchmaker = Matchmaker(users, "matchmaking_model.pth")
matchmaker.build_graph()

# get latest user info
data = sheet1.get_all_values()
last_row = data[-1]

def format_user_data(user_data):
    user_format = {}
    for k, v in user_data.items():
        if k in ['Name', 'ageGroupPreference']:
            user_format[k] = v
        elif k=='age':
            user_format[k] = int(v)
        elif k in ['gender', 'genderPreference']:
            user_format[k] = v.lower()
        elif k == 'interests':
            user_format[k] = v.lower().split(", ")

    print("THe user format is", user_format)
    return user_format

def add_user_data():
    global last_row
    # get the updated data from the first sheet
    data = sheet1.get_all_values()
    last_row_new = data[-1]

    # when a new row is added
    if last_row_new != last_row:
        last_row = last_row_new  # update last_row to the latest one
        new_user_id = len(data) - 1  # -1 because we are considering 0-based indexing
        user_key =  "user" + str(new_user_id)
        print("This is the user: ", user_key)

        if user_key not in users.keys():
            print("This is the user: ", user_key)

            # format the user data
            user_data = format_user_data(dict(zip(data[0], last_row_new)))
            
            # Add the new user to users
            users[user_key] = user_data

            # Update the generate.py file with the new user
            with open("generate.py", "w") as outfile:
                outfile.write("users = %s" % users)

            matchmaker.add_user_and_update_graph(user_key)
            
            # get the matched users
            matched_users = matchmaker.graph_matchmaking(user_key)

            print("This is the matched users ", matched_users)
        
            # Write the matched users in the second sheet
            sheet2.append_row([user_key, ','.join(matched_users)])


while True:
    add_user_data()
    time.sleep(1)
