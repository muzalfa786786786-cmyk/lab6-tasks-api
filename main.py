
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

TASKS = []


@app.get("/")
def home():
    return jsonify(
        service="tasks-api",
        version=os.getenv("GAE_VERSION", "local"),
        status="running"
    )


@app.post("/tasks")
def add_task():
    data = request.get_json(silent=True)

    if not isinstance(data, dict) or not data.get("title"):
        return jsonify(error="A task title is required"), 400

    task = {
        "id": len(TASKS) + 1,
        "title": data["title"]
    }

    TASKS.append(task)
    return jsonify(task=task, count=len(TASKS)), 201


@app.get("/tasks")
def list_tasks():
    return jsonify(TASKS)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )
