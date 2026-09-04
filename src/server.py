# I forgot I set up the REST API for EventBridge to
# trigger the CV computation via an API call, so reinstating this

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)