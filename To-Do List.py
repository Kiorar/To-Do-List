import os

TASK_FILE = "tasks.txt"


def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            for line in file:
                tasks.append(line.strip())  # Remove new line characters
        print(f"Loaded {len(tasks)} tasks from {TASK_FILE}\n")
    else:
        print(f"No existing tasks found. Creating a new To-Do List.\n")

# Function to save tasks to the file
def save_tasks():
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')  # Write each task on a new line
    print(f"Tasks saved to {TASK_FILE}.\n")

tasks = []

def show_tasks():
    if not tasks:
        print("Your To-Do List is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print()

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.\n")


def remove_task():
    try:
        show_tasks()
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    load_tasks() 
    while True:
        print("To-Do List Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Save and Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            save_tasks() 
            print("Closing the To-Do List.")
            break
        else:
            print("Please select a option (1-4).\n")

if __name__ == "__main__":
    main()
