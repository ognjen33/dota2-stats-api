from flask import Flask
import json

app = Flask(__name__)


@app.route("/")
def all_orders():
    message = "HELLO"
    return json.dumps(message)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
