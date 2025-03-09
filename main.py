import json
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
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
def mark_complete():

    selected_item = task_list.selection()
    if not selected_item:
        messagebox.showerror("Error", "No task selected!")
        return

    task_id = task_list.item(selected_item, "values")[0]
    tasks = load_tasks()
    for task in tasks:
        if str(task["id"]) == task_id:
            task["completed"] = True
    save_tasks(tasks)
    update_task_list()