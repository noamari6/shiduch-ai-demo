
from flask import Flask, request, jsonify, send_from_directory
import json, os

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(".", path)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    profile = f"{data['name']}, בן/בת {data['age']} מהעיר {data['city']}."
    entry = {"name": data["name"], "age": data["age"], "city": data["city"], "profile": profile}
    with open("data.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return jsonify({"profile": profile})

if __name__ == "__main__":
    app.run(debug=True)
