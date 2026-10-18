
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "AWS CI/CD Pipeline is working!"


@app.route("/health")
def health():
    return jsonify(status="UP"), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
