# To-Do List Application (Command-Line)

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in your To-Do List.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("\nEnter the new task: ")
    tasks.append(task)
    print(f"Task '{task}' added to your To-Do List.")

def update_task(tasks):
    if not tasks:
        print("\nNo tasks available to update.")
        return
    view_tasks(tasks)
    task_num = int(input("\nEnter the task number you want to update: "))
    if 0 < task_num <= len(tasks):
        new_task = input("Enter the updated task: ")
        tasks[task_num - 1] = new_task
        print(f"Task {task_num} updated.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    if not tasks:
        print("\nNo tasks available to delete.")
        return
    view_tasks(tasks)
    task_num = int(input("\nEnter the task number you want to delete: "))
    if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' deleted from your To-Do List.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid option! Please choose a valid number (1-5).")

if __name__ == "__main__":
    main()
