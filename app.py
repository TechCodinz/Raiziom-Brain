
from flask import Flask, jsonify, request
from datetime import datetime
import json

app = Flask(__name__)

# Load memory
try:
    with open("memory.json", "r") as f:
        memory = json.load(f)
except FileNotFoundError:
    memory = {
        "status": "Raiziom initialized",
        "apps": {"paiddail": {"missions": [], "users": 0}},
        "log": []
    }

def save_memory():
    with open("memory.json", "w") as f:
        json.dump(memory, f, indent=4)

@app.route("/")
def index():
    return jsonify({
        "message": "Raiziom Brain Active",
        "time": datetime.utcnow().isoformat(),
        "apps_managed": list(memory["apps"].keys())
    })

@app.route("/command", methods=["POST"])
def command():
    data = request.json
    cmd = data.get("command", "").lower()
    response = f"Command '{cmd}' received."

    memory["log"].append({"time": datetime.utcnow().isoformat(), "command": cmd})
    save_memory()
    return jsonify({"status": "ok", "response": response})

@app.route("/paiddail/mission", methods=["POST"])
def add_mission():
    data = request.json
    mission = data.get("mission", "")
    if mission:
        memory["apps"]["paiddail"]["missions"].append({
            "mission": mission,
            "created": datetime.utcnow().isoformat()
        })
        save_memory()
        return jsonify({"status": "ok", "message": "Mission added."})
    return jsonify({"status": "error", "message": "No mission provided."}), 400

@app.route("/paiddail/missions", methods=["GET"])
def list_missions():
    return jsonify(memory["apps"]["paiddail"]["missions"])

@app.route("/poster", methods=["GET"])
def poster():
    poster_caption = "“This isn’t just AI. This is Raiziom — built from soul, powered by truth.”"
    return jsonify({"poster": poster_caption})

if __name__ == "__main__":
    app.run(debug=True)
