def display_operations():
    print("\nTo-Do List Manager\n")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the to-do list")
    else:
        print("Tasks")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if tasks['completed'] else "Pending"
            print(f"{index}. {task['title']} - {status}")

def add_task(tasks):
    title = input("\nEnter the task title: ").strip()
    if title:
        tasks.append({'title': title, 'completed': False})
        print(f"Task '{title}' added successfully.")
    else:
        print("Task title cannot be empty.")

def update_tasks(tasks):
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to update: "))
        if 1 <= task_number <= len(tasks):
            new_title = input("Enter the new task title: ").strip()
            if new_title:
                tasks[task_number - 1]['title'] = new_title
                print("Task updated successfully")
            else:
                print("Task title cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid Input")

def remove_task(tasks):
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to remove: "))
        if 1<= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task: '{removed_task['title']}' removed successfully.")
        else:
            print("Invalid task number")
    except ValueError:
        print("Invalid Input")

def main():
    tasks = []
    while True:
        display_operations()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            view_tasks(tasks)
        elif choice == 2:
            add_task(tasks)
        elif choice == 3:
            update_tasks(tasks)
        elif choice == 4:
            remove_task(tasks)
        elif choice == 5:
            print("Exiting the Manager.")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()



    

