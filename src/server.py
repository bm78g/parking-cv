# I forgot I set up the REST API for EventBridge to
# trigger the CV computation via an API call, so reinstating this

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health", methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "message": "Application is running"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)