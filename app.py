import flask
import hashlib
import os

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.send_from_directory(".", "handSensorMainPage.html")
# Define a route that serves static web pages

# Route that serves static web pages
@app.route("/<path:filename>")
def static_files(filename):
    # Check if the file exists in the 'static' directory
    if os.path.exists(filename):
        return flask.send_from_directory(".", filename)
    else:
        return "File not found", 404
#Route that returns the newly updated password hash if it is different than the current password
@app.route("/new-password", methods=['POST'])
def newPassword():
    #Gets the JSON file with the passwords
    data = flask.request.json
    #Get old and new password if data if found, otherwise, return error message
    if data:
        password_attempt = data.get("password-attempt")
        new_password = data.get("new-password")
    else:
        return("Failed to retrieve JSON file")

    #Get the current password hash
    with open("passhash.txt") as fp:
        oldhash = fp.read().strip()

    #Hashes the bytes of the new password and gets the hexidecimal representation
    password_attempt_hash = hashlib.sha256(password_attempt.encode()).hexdigest()
    if password_attempt_hash == oldhash:
        new_pass_hash = hashlib.sha256(new_password.encode()).hexdigest()
        with open("passhash.txt", "w") as fp:
            fp.write(new_pass_hash)
        return flask.jsonify({ "success": True })
    else:
        return flask.jsonify({ "success": False })


## IT is a post request. JSON as body. Store new password as crypto hash (SHA256)
# Define a route that serves /verify-password
@app.route("/verify-password", methods=['POST'])
def verifyPassword():
    #Gets the JSON file with the passwords
    data = flask.request.json
    #Get attempt and actual password if data if found, otherwise, return error message
    if data:
        password_attempt = data.get("password-attempt")
    else:
        return("Failed to retrieve JSON file")

    #Reads in the password hash
    with open("passhash.txt") as ph:
        password = ph.read().strip()
    #Hash the attempt in order to compare to the hashed password
    password_attempt_hash = hashlib.sha256(password_attempt.encode()).hexdigest()
       #Returns true if the hash is the same, otherwise false
    if password_attempt_hash == password:
        return flask.jsonify({"success": True})
    else:
        return flask.jsonify({"success": False})


if __name__ == "__main__":
    app.run()
