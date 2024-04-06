import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "HELLO"

# Define a route that serves static web pages

# Define a route that serves /new-password
## IT is a post request. JSON as body. Store new password as crypto hash (SHA256)
# Define a route that serves /verify-password



if __name__ == "__main__":
    app.run()