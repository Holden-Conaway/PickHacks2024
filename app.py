import flask
import hashlib

app = flask.Flask(__name__)
old_password = "00000"

@app.route("/")
def index():
    return "HELLO"

# Define a route that serves static web pages

# Define a route that serves /new-password
@app.route("/new-password", methods=['POST'])
def new_password():
    new_password = flask.request.form.get('new-password')
    new_password_hash = hashlib.sha256(new_password.encode()).hexdigest()
    print(new_password_hash)


## IT is a post request. JSON as body. Store new password as crypto hash (SHA256)
# Define a route that serves /verify-password



if __name__ == "__main__":
    app.run()