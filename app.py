from flask import Flask, render_template, jsonify
import json
import requests
from datetime import datetime

app = Flask(__name__)

# Load memory
try:
    with open("memory.json") as f:
        memory = json.load(f)
except FileNotFoundError:
    memory = {
        "status": "Raiziom initialized",
        "apps": {
            "paiddail": {
                "missions": [],
                "users": 0
            }
        },
        "log": []
    }

# Save memory helper
def save_memory():
    with open("memory.json", "w") as f:
        json.dump(memory, f, indent=2)

# Homepage
@app.route("/")
def index():
    return "Raiziom Brain V3 is live."

# Apps route (lists active apps)
@app.route("/apps")
def apps():
    return render_template("apps.html", apps=memory.get("active_apps", []))

# Missions route (from Paiddail)
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

# Poster route
@app.route("/poster", methods=["GET"])
def poster():
    poster_caption = "This isn’t just AI. This is Raiziom — built from soul, powered by truth."
    return jsonify({"poster": poster_caption})

# Run app on Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
