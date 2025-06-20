from flask import Flask, render_template, jsonify
import json
import requests

app = Flask(__name__)

# Load memory
with open("memory.json", "r") as f:
    memory = json.load(f)

@app.route("/")
def home():
    return render_template("home.html", memory=memory)

@app.route("/apps")
def apps():
    return render_template("apps.html", apps=memory.get("active_apps", []))

@app.route("/missions")
def missions():
    try:
        r = requests.get("https://raiziom-brain.onrender.com/paiddail/missions")
        print("STATUS:", r.status_code)
        print("RAW TEXT:", r.text)

        data = r.json()
        if isinstance(data, dict) and "missions" in data:
            missions = data["missions"]
        elif isinstance(data, list):
            missions = data
        else:
            missions = [{"task": "Unexpected data format", "reward": 0}]
    except Exception as e:
        print("ERROR:", e)
        missions = [{"task": "Error loading missions", "reward": 0}]
    return render_template("missions.html", missions=missions)

@app.route("/console")
def console():
    return render_template("console.html")

@app.route("/settings")
def settings():
    return render_template("settings.html", memory=memory)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
