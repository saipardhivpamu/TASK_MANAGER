import json
import os
TASK_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file safely."""
    if not os.path.exists(TASK_FILE) or os.stat(TASK_FILE).st_size == 0:
        return []
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []