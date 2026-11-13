import tkinter as tk
import core

window = tk.Tk()

window.title("Smart Study Planner")
window.geometry("500x400")

# Title
title_label = tk.Label(
    window,
    text="Smart Study Planner",
    font=("Arial", 18)
)

title_label.pack(pady=10)

# Subject
subject_label = tk.Label(window, text="Subject")
subject_label.pack()

subject_entry = tk.Entry(window)
subject_entry.pack()

# Topic
topic_label = tk.Label(window, text="Topic")
topic_label.pack()

topic_entry = tk.Entry(window)
topic_entry.pack()

task_number_label = tk.Label(
    window,
    text="Task Number"
)
task_number_label.pack()

task_number_entry = tk.Entry(window)
task_number_entry.pack()

# Add Task Function
def add_task_gui():

    subject = subject_entry.get()
    topic = topic_entry.get()

    core.add_task(subject, topic)

    result_label.config(text="Task Added Successfully!")


# Button
add_button = tk.Button(
    window,
    text="Add Task",
    command=add_task_gui
)

add_button.pack(pady=10)

# View Tasks Function
def view_tasks_gui():

    tasks = core.view_tasks()

    task_text.delete("1.0", tk.END)

    for i, task in enumerate(tasks):

        task_text.insert(
        tk.END,
        f"{i} - {task['subject']} - {task['topic']}\n"
    )

# View Button
view_button = tk.Button(
    window,
    text="View Tasks",
    command=view_tasks_gui
)

view_button.pack(pady=5)

def save_tasks_gui():

    core.save_tasks()

    result_label.config(
        text="Tasks Saved Successfully!"
    )


def load_tasks_gui():

    core.load_tasks()

    result_label.config(
        text="Tasks Loaded Successfully!"
    )
def search_tasks_gui():

    subject = subject_entry.get()

    results = core.search_task(subject)

    task_text.delete("1.0", tk.END)

    if len(results) == 0:

        task_text.insert(
            tk.END,
            "No matching tasks found."
        )

    else:

        for task in results:

            task_text.insert(
                tk.END,
                f"{task['subject']} - {task['topic']}\n"
            )
def delete_task_gui():

    index = int(task_number_entry.get())

    if core.delete_task(index):

        result_label.config(
            text="Task deleted successfully!"
        )

    else:

        result_label.config(
            text="Invalid task number."
        )

save_button = tk.Button(
    window,
    text="Save Tasks",
    command=save_tasks_gui
)

save_button.pack(pady=5)

load_button = tk.Button(
    window,
    text="Load Tasks",
    command=load_tasks_gui
)

load_button.pack(pady=5)

search_button = tk.Button(
    window,
    text="Search Task",
    command=search_tasks_gui
)

search_button.pack(pady=5)
delete_button = tk.Button(
    window,
    text="Delete Task",
    command=delete_task_gui
)

delete_button.pack(pady=5)

# Task Display Area
task_text = tk.Text(
    window,
    height=8,
    width=40
)

task_text.pack()

# Result Label
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()