import tkinter as tk
import core

window = tk.Tk()
window.configure(bg="#EAF4FC")

window.title("Smart Study Planner - Student Task Management System")
window.geometry("800x600")

# Title
title_label = tk.Label(
    window,
    text="SMART STUDY PLANNER",
    font=("Arial", 22, "bold"),
    bg="#EAF4FC",
    fg="#003366"
)


title_label.pack(pady=10)
subtitle_label = tk.Label(
    window,
    text="Student Task Management System",
    font=("Arial", 10),
    bg="#EAF4FC"
)

subtitle_label.pack(pady=5)

# Subject
subject_label = tk.Label(window, text="Subject Name")
subject_label.pack()

subject_entry = tk.Entry(window, width=30)
subject_entry.pack()

# Topic
topic_label = tk.Label(window, text="Study Topic")
topic_label.pack()

topic_entry = tk.Entry(window,width=30)
topic_entry.pack()

task_number_label = tk.Label(
    window,
    text="Task Number"
)
task_number_label.pack()

task_number_entry = tk.Entry(window,width=30)
task_number_entry.pack(pady=10)

# Add Task Function
def add_task_gui():

    subject = subject_entry.get()
    topic = topic_entry.get()

    core.add_task(subject, topic)

    result_label.config(text="Student task Added Successfully!")


# Button
add_button = tk.Button(
    window,
    text="Add Task",
    command=add_task_gui,
    width=15,
    bg="#4CAF50",
    fg="white"
)

add_button.pack(pady=8)


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
    command=view_tasks_gui,
    width=15,
    bg="#2196F3",
    fg="white"
)

view_button.pack(pady=10)

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
    command=save_tasks_gui,
    width=15,
    bg="#673AB7",
    fg="white"
)

save_button.pack(pady=8)

load_button = tk.Button(
    window,
    text="Load Tasks",
    command=load_tasks_gui,
    width=15,
    bg="#009688",
    fg="white"

)

load_button.pack(pady=8)

search_button = tk.Button(
    window,
    text="Search Task",
    command=search_tasks_gui,
    width=15,
   bg="#FF9800",
    fg="white"

)

search_button.pack(pady=8)
delete_button = tk.Button(
    window,
    text="Delete Task",
    command=delete_task_gui,
    width=15,
    bg="#F44336",
    fg="white"
)

delete_button.pack(pady=8)

# Task Display Area
task_text = tk.Text(
    window,
    height=15,
    width=70
)

task_text.pack(pady=15)

# Result Label
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()