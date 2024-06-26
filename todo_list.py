import sys

def main():
    todo_list = load_from_text_file()
    print("=" * 35)
    print(f"{' ' * 12} TO-DO LIST")
    print("=" * 35)

    while True:
        menu(todo_list)
        save_in_text_file(todo_list)

def menu(todo_list):
    options = [
        "1. Add New Task",
        "2. Update Task",
        "3. View Tasks",
        "4. Delete Task",
        "5. Exit the program"
    ]

    for option in options:
        print(option)

    print()

    try:
        user_option = int(input("Option: "))
    except ValueError:
        print("\nPlease enter a valid option number.\n")
        return

    match user_option:
        case 1:
            add_task(todo_list)
        case 2:
            update_task(todo_list)
        case 3:
            view_task(todo_list)
        case 4:
            delete_task(todo_list)
        case 5:
            exit_program()
        case _:
            print("\nOnly choose from the given options.\n")

def add_task(todo_list):
    description = input("Enter task description: ")
    task = {"description": description, "completed": False}
    todo_list.append(task)

def update_task(todo_list):
    if not todo_list:
        print("\nNo tasks to update.\n")
        return

    try:
        update_task_id = int(input("Enter the task ID to mark as completed: "))
    except ValueError:
        print("\nPlease enter a valid task ID\n")
        return

    if 1 <= update_task_id <= len(todo_list):
        task = todo_list[update_task_id - 1]
        task["completed"] = True
        print(f"\nTask {update_task_id} has been marked as completed.\n")
    else:
        print("\nTask ID not found. Please enter a valid task ID.\n")

def view_task(todo_list):
    if not todo_list:
        print("\nNo tasks in the to-do list.")
        return

    for index, task in enumerate(todo_list, start=1):
        description = task.get("description")
        status = "Completed" if task.get("completed") else "Not completed"
        print()
        print(f"Task {index}:")
        print(f"  Description: {description}")
        print(f"  Status: {status}")
        print()

def delete_task(todo_list):
    if not todo_list:
        print("\nNo tasks to delete.\n")
        return

    try:
        delete_task_id = int(input("Enter task ID to delete the task: "))
    except ValueError:
        print("\nInvalid input. Please enter a valid task ID.\n")
        return

    if 1 <= delete_task_id <= len(todo_list):
        todo_list.pop(delete_task_id - 1)
        print(f"\nTask {delete_task_id} has been deleted.\n")
    else:
        print("\nTask ID not found. Please enter a valid task ID.\n")

def save_in_text_file(todo_list):
    with open("tasks.txt", 'w') as file:
        for index, task in enumerate(todo_list, start=1):
            description = task.get("description")
            status = "Completed" if task.get("completed") else "Not completed"
            file.write(f"Task {index}:\n")
            file.write(f"  Description: {description}\n")
            file.write(f"  Status: {status}\n\n")

def load_from_text_file():
    try:
        with open("tasks.txt", 'r') as file:
            todo_list = []
            while True:
                task_line = file.readline()
                if not task_line:
                    break
                description_line = file.readline().strip()
                status_line = file.readline().strip()

                description = description_line.split(": ")[1]
                status = status_line.split(": ")[1] == "Completed"

                todo_list.append({"description": description, "completed": status})
                file.readline()  # Skip the empty line between tasks

        return todo_list
    except FileNotFoundError:
        return []

def exit_program():
    print("\nExiting program...")
    print("All tasks have been saved in tasks.txt file.\n")
    sys.exit()

if __name__ == "__main__":
    main()
