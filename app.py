from flask import Flask, jsonify, request
from datetime import datetime
from paiddail.logic import get_missions, log_task, get_user_data

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "message": "Raiziom Brain V3 is Active",
        "apps_managed": ["paiddail"]
    })

@app.route("/paiddail/missions", methods=["GET"])
def list_missions():
    return jsonify(get_missions())

@app.route("/paiddail/log", methods=["POST"])
def log_user_task():
    data = request.json
    return jsonify(log_task(data))

@app.route("/paiddail/data", methods=["GET"])
def user_summary():
    return jsonify(get_user_data())

# Render requirement
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
