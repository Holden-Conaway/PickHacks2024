import flask
import hashlib

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "HELLO"

# Define a route that serves static web pages

#Route that returns the newly updated password hash if it is different than the current password
@app.route("/new-password", methods=['POST'])
def newPassword():
    #Gets the JSON file with the passwords
    data = flask.request.json
    #Get old and new password if data if found, otherwise, return error message
    if data:
        new_password = data.get("new-password")
        old_password_hash = data.get("old-password")
    else:
        return("Failed to retrieve JSON file")
    
    #Hashes the bytes of the new password and gets the hexidecimal representation 
    new_password_hash = hashlib.sha256(new_password.encode()).hexdigest()
    
    #If the old password is used, do not set the new password
    if old_password_hash == new_password_hash:
        return("You can't reuse a previous password")
    else:
        return new_password_hash


## IT is a post request. JSON as body. Store new password as crypto hash (SHA256)
# Define a route that serves /verify-password
@app.route("/verify-password", methods=['POST'])
def verifyPassword():
    #Gets the JSON file with the passwords
    data = flask.request.json
    #Get attempt and actual password if data if found, otherwise, return error message
    if data:
        password_attempt = data.get("password-attempt")
        password = data.get("password")
    else:
        return("Failed to retrieve JSON file")

    #Hash the attempt in order to compare to the hashed password
    password_attempt_hash = hashlib.sha256(password_attempt.encode()).hexdigest()
    
    #Returns true if the hash is the same, otherwise false
    if password_attempt_hash == password:
        return True
    else:
        return False


if __name__ == "__main__":
    app.run()