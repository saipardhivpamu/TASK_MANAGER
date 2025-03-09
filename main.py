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




root = ttk.Window(themename="darkly")  
root.title("Task Tracker")
root.geometry("600x500")

header_label = ttk.Label(root, text="Task Tracker", font=("Arial", 18, "bold"))
header_label.pack(pady=10)

title_label = ttk.Label(root, text="Task Title:")
title_label.pack()
title_entry = ttk.Entry(root, width=50)
title_entry.pack()

description_label = ttk.Label(root, text="Task Description:")
description_label.pack()
description_entry = ttk.Entry(root, width=50)
description_entry.pack()


priority_label = ttk.Label(root, text="Priority:")
priority_label.pack()
priority_var = ttk.StringVar(value="Medium")
priority_menu = ttk.Combobox(root, textvariable=priority_var, values=["Low", "Medium", "High"])
priority_menu.pack()

btn_frame = ttk.Frame(root)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="Add Task", command=add_task, bootstyle=SUCCESS).grid(row=0, column=0, padx=5)
ttk.Button(btn_frame, text="Mark Complete", command=mark_complete, bootstyle=WARNING).grid(row=0, column=1, padx=5)
ttk.Button(btn_frame, text="Delete Task", command=delete_task, bootstyle=DANGER).grid(row=0, column=2, padx=5)

columns = ("ID", "Status", "Title", "Description", "Priority")
task_list = ttk.Treeview(root, columns=columns, show="headings", height=10, bootstyle="primary")
task_list.heading("ID", text="ID")
task_list.heading("Status", text="Status")
task_list.heading("Title", text="Title")
task_list.heading("Description", text="Description")
task_list.heading("Priority", text="Priority")
task_list.pack(fill="both", expand=True, pady=10)

update_task_list()


root.mainloop()
