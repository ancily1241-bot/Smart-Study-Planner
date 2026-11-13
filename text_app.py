import core

while True:

    print("\nSMART STUDY PLANNER")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Exit")
    choice = input("Enter choice: ")

    if choice == "1":

        subject = input("Enter subject: ")
        topic = input("Enter topic: ")

        core.add_task(subject, topic)

        print("Task added successfully!")

    elif choice == "2":

        tasks = core.view_tasks()

        if len(tasks) == 0:
            print("No tasks found.")

        else:
            for task in tasks:
                print(task)

    elif choice == "3":

        subject = input("Enter subject to search: ")

        results = core.search_task(subject)

        if len(results) == 0:
            print("No matching tasks found.")

        else:
            for task in results:
                print(task)

    elif choice == "4":

        tasks = core.view_tasks()

        for i, task in enumerate(tasks):
            print(i, task)

        index = int(input("Enter task number to delete: "))

        if core.delete_task(index):
            print("Task deleted successfully!")

        else:
            print("Invalid task number.")

    elif choice == "5":

        core.save_tasks()

    elif choice == "6":

        core.load_tasks()

    elif choice == "7":

        break


    else:
        print("Invalid choice")