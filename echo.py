from flask import Flask, request

app = Flask(__name__)


@app.route("/app", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def echo():
    data = request.get_data(as_text=True)
    return data or "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
