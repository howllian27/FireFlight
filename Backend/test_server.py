import requests
import time
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
