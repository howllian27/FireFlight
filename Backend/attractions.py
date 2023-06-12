import requests

query = "coffee"
location = "47.606,-122.349358"
API_KEY = 'AIzaSyBZnCWJ53IDmXJMCvj4EzLxKDN3gB_20O4'  # replace with your actual API key
endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
details_url = "https://maps.googleapis.com/maps/api/place/details/json"
photo_url = "https://maps.googleapis.com/maps/api/place/photo"
places = []

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

for place in places:
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
        summary = details.get('editorial_summary', {'overview': 'No summary provided'})
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
            webbrowser.open(photo_request_url)
        print(f"Name: {name}\nRating: {rating}\nAddress: {address}")
        print(f"Summary: {summary['overview']}")
        print(f"Price Level: {price_level}")
        print("Opening Hours:")
        for opening_hour in opening_hours:
            print(opening_hour)
        print("\n")
