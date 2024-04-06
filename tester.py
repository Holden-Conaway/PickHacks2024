import requests
import json

BASE_URL = "http://localhost:5000"

new_password_data = {
    "new-password": "new_password123",
    "old-password": "old_password_hash"
}

verify_password_data = {
    "password-attempt": "new_password123",
    "password-hash": "stored_password_hash"
}

def test_new_password_route():
    url = BASE_URL + "/new-password"
    response = requests.post(url, json=new_password_data)
    print("Response from /new-password route:")
    print(response.json())

# Function to send a POST request to /verify-password route
def test_verify_password_route():
    url = BASE_URL + "/verify-password"
    response = requests.post(url, json=verify_password_data)
    print("Response from /verify-password route:")
    print(response.json())

# Call the functions to test the routes
if __name__ == "__main__":
    test_new_password_route()
    test_verify_password_route()