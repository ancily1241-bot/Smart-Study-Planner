# Core functions for Smart Study Planner
import json

tasks = []


def add_task(subject, topic):
    task = {
        "subject": subject,
        "topic": topic
    }

    tasks.append(task)


def view_tasks():
    return tasks


def search_task(subject):

    results = []

    for task in tasks:

        if task["subject"].lower() == subject.lower():
            results.append(task)

    return results
def delete_task(index):

    if 0 <= index < len(tasks):
        tasks.pop(index)
        return True

    return False
def save_tasks():

    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

    print("Tasks saved successfully!")


def load_tasks():

    global tasks

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

        print("Tasks loaded successfully!")

    except FileNotFoundError:
        print("No saved tasks found.")