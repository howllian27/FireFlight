from matchmaker import Matchmaker
from geopy.geocoders import Nominatim
import pandas as pd
import os
import ast
import gspread
import time
import json
import requests

# Get the credentials and create a client to interact with the Google Sheets API
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)
gc = gspread.service_account(filename='credentials.json')

# Open the Google Spreadsheet by its ID (the string of random letters and numbers in the URL)
spreadsheet = gc.open_by_key("10RDxyuBw5ygMn79vQA5aove-bzjDJ9mNWblUO0SK-xw")

# Initialise the 3 sheets
sheet1 = spreadsheet.get_worksheet(0)  # users data is in the first sheet
sheet2 = spreadsheet.get_worksheet(2)  # matched users will be written in the second sheet
sheet3 = spreadsheet.get_worksheet(3) # attractions

# Load users from generate.py
with open("generate.py", "r") as infile:
    users = ast.literal_eval(infile.read().split(" = ")[1])

matchmaker = Matchmaker(users, "matchmaking_model.pth")
matchmaker.build_graph()

# get latest user info
data = sheet1.get_all_values()
last_row = data[-1]

# format user data for DB
def format_user_data(user_data):
    user_format = {}
    for k, v in user_data.items():
        if k in ['name', 'ageGroupPreference', 'bio', 'hotel']:
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
    while True:
        try:
            data = sheet1.get_all_values()
            last_row_new = data[-1]
            break
        except:
            time.sleep(2)

    # when a new row is added
    if last_row_new != last_row:
        # Get the total number of rows
        while True:
            try:
                num_rows = len(sheet2.get_all_values())
                # Delete rows from 2 to the end
                if num_rows > 1:
                    sheet2.delete_rows(2, num_rows)
                break
            except:
                continue

        # Get the total number of rows
        while True:
            try:
                num_rows = len(sheet3.get_all_values())
                print("The no. of rows is ", num_rows)
                if num_rows > 1:
                    # Delete rows from 2 to the end
                    sheet3.delete_rows(2, num_rows)
                    print("Sheet3 ROWS DELETED")
                break
            except:
                continue

        last_row = last_row_new  # update last_row to the latest one
        new_user_id = len(data) - 1  # -1 because we are considering 0-based indexing
        user_key =  "user" + str(new_user_id)
        print("This is the user: ", user_key)

        if user_key not in users.keys():
            print("This is the user: ", user_key)

            # format the user data
            user_data = format_user_data(dict(zip(data[0], last_row_new)))
            attractions_interests = []
            attractions_interests.append(user_data["interests"])
            
            # Add the new user to users
            users[user_key] = user_data
            hotel = users[user_key]['hotel']
            print(hotel)

            # Update the generate.py file with the new user
            with open("generate.py", "w") as outfile:
                outfile.write("users = %s" % users)

            matchmaker.add_user_and_update_graph(user_key)
            
            # get the matched users
            matched_users = matchmaker.graph_matchmaking(user_key)

            final_matched_users = [match[0] for match in matched_users]

            print("This is the matched users ", final_matched_users)
        
            # Write the matched users in the second sheet
            # Get a list of all names, ages, and interests
            names = [f"{users[user]['name']} ({users[user]['age']})" for user in final_matched_users]
            interests = [', '.join(users[user]['interests']).title() for user in final_matched_users]

            attractions_interests.append(users[user_key]['interests'])

            for user in final_matched_users:
                attractions_interests.append(users[user]['interests'])

            interest_query = []

            if len(attractions_interests[0]) <= 2:
                interest_query.append(' '.join(attractions_interests[0]))
            else:
                for num in range(1,len(attractions_interests)):
                    interest_query += list(set(attractions_interests[0]) & set(attractions_interests[num]))

            print("The interest query is: ", interest_query)
            # Write them to the sheet
            print("Names list is ", names)
            sheet2.append_row(names)
            print("Interests list is ", interests)
            sheet2.append_row(interests)

            if len(interest_query)>3:
                interest_query = interest_query[:3]
            
            count = 0
            while count <= 3:
                try:
                    if count == 3:
                        add_attractions(["food"], hotel)
                        break
                    add_attractions(interest_query, hotel)
                    count += 1
                    break
                except:
                    time.sleep(2)

def add_attractions(interest_query, destination):
    # details required for attractions
    print(interest_query)
    query = set(interest_query)
    print("The query is ", query)
    location = get_coordinates(destination)
    print("the location is ", location)
    API_KEY = 'AIzaSyBZnCWJ53IDmXJMCvj4EzLxKDN3gB_20O4'
    endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    details_url = "https://maps.googleapis.com/maps/api/place/details/json"
    photo_url = "https://maps.googleapis.com/maps/api/place/photo"
    places = []


    count = 0
    while places == []:
        if count == 1:
            query = "food"
        params = {
            'location': location,
            'keyword': query,
            'key': API_KEY,
            'rankby': 'distance'
        }

        res = requests.get(endpoint_url, params=params)
        results =  json.loads(res.content)
        places.extend(results['results'])
        while "next_page_token" in results:
            params['pagetoken'] = results['next_page_token'],
            time.sleep(2)  # add delay before next request
            res = requests.get(endpoint_url, params=params)
            results = json.loads(res.content)
            places.extend(results['results'])
        count+=1

    closest_places = places[:10]
    names_list = []
    ratings_list = []
    address_list = []
    summary_list = []
    price_level_list = []
    opening_hrs_list = []

    for place in closest_places:
        place_id = place['place_id']
        details_params = {
            'place_id': place_id,
            'fields': 'name,rating,formatted_address,opening_hours,editorial_summary,price_level,photos',
            'key': API_KEY
        }
        res = requests.get(details_url, params=details_params)
        result = json.loads(res.content)
        if result['status'] == 'OK':
            details = result['result']
            name = details.get('name', 'No name provided')
            rating = details.get('rating', 'No rating provided')
            address = details.get('formatted_address', 'No address provided')
            summary = details.get('editorial_summary', {'overview': 'No summary provided'}).get('overview', 'No summary provided')
            opening_hours = details.get('opening_hours', {}).get('weekday_text', ['No opening hours provided'])
            price_level_num = details.get('price_level', 'No price level provided')
            if isinstance(price_level_num, int):
                price_levels = ['Free', 'Inexpensive', 'Moderate', 'Expensive', 'Very Expensive']
                price_level = price_levels[price_level_num] if price_level_num < len(price_levels) else 'Unknown price level'
            else:
                price_level = 'No price level provided'
            photos = details.get('photos', [])
            if photos:
                photo_reference = photos[0]['photo_reference']
                photo_params = {
                    'maxwidth': '400',
                    'photoreference': photo_reference,
                    'key': API_KEY
                }
                photo_request_url = requests.get(photo_url, params=photo_params).url

            names_list.append(name)
            ratings_list.append(f"Rating: {rating}/5")
            address_list.append(address)
            summary_list.append(summary)
            price_level_list.append(price_level)
            opening_hrs_list.append('\n'.join(opening_hours))
    
    sheet3.append_row(names_list)
    sheet3.append_row(ratings_list)
    sheet3.append_row(address_list)
    sheet3.append_row(summary_list)
    sheet3.append_row(price_level_list)
    sheet3.append_row(opening_hrs_list)

def get_coordinates(location):
    geolocator = Nominatim(user_agent="my-app")
    location_data = geolocator.geocode(location)
    
    if location_data:
        latitude = location_data.latitude
        longitude = location_data.longitude
        print(f"Coordinates for '{location}':")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        return f"{latitude}, {longitude}"
    else:
        print(f"Coordinates not found for '{location}'")
        return "1.2838, 103.8591"

while True:
    add_user_data()
    time.sleep(2)