tasks = []

def add_task(task):
    tasks.append(task)

def delete_task(task):
    if task in tasks:
        tasks.remove(task)

def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        add_task(task)
        print(f"Task '{task}' added.")
    elif choice == "2":
        task = input("Enter a task to delete: ")
        delete_task(task)
        print(f"Task '{task}' deleted.")
    elif choice == "3":
        print("Your tasks:")
        view_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose a valid option.")
