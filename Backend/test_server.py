import requests
import time
import json
from multiprocessing import Process
from rest import app  # assuming your Flask app is named "app" in rest.py

def run_server():
    app.run(port=5000)

def test_server():
    # Give the server a little bit of time to start up
    time.sleep(2)

    # Send a request to the server
    response = requests.get('http://localhost:5000/match', json={'user': 'user1'})

    # Check the response
    assert response.status_code == 200
    assert 'matched_users' in response.json()

def test_match_endpoint():
    # Define the URL of your server
    url = "http://127.0.0.1:5000/match"

    # Define the data to send in the POST request
    data = {
        "user": "user1"
    }

    # Send the POST request
    response = requests.post(url, json=data)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check that the response data is as expected
    response_data = response.json()
    assert "status" in response_data
    assert response_data["status"] == "success"

if __name__ == '__main__':
    # Start the server
    server_process = Process(target=run_server)
    server_process.start()

    # Run the tests
    try:
        test_server()
    finally:
        # Stop the server
        server_process.terminate()
        server_process.join()
