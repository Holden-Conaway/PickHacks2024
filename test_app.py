import requests
import hashlib

HOST = "http://localhost:5000"

def test_new_password():
    old_hash = hashlib.sha256("password123".encode()).hexdigest()
    with open("passhash.txt", 'w') as ph:
        ph.write(old_hash)
    req = requests.post(HOST + "/new-password", json={"password-attempt": "password123", "new-password": "123password"})
    with open("passhash.txt") as ph:
        new_hash = ph.read()

    print(f"Old hash: {old_hash}")
    print(f"New hash: {new_hash}")

def test_verify_password():
    req = requests.post(HOST + "/verify-password", json={"password-attempt": "123password"})
    print(req.text)

if __name__ == "__main__":
    test_new_password()
    test_verify_password()
