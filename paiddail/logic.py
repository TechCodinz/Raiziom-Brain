# ✅ Paiddail logic for mission handling

missions = [
    {"id": 1, "task": "Invite 5 people to Paiddail", "reward": 100},
    {"id": 2, "task": "Share app on social media", "reward": 50},
    {"id": 3, "task": "Complete profile setup", "reward": 30}
]

user_logs = []

def get_missions():
    return missions

def log_task(data):
    user_logs.append(data)
    return {"message": "Task logged", "data": data}

def get_user_data():
    return {
        "logs": user_logs,
        "total_earned": sum(log["reward"] for log in user_logs if "reward" in log)
    }
