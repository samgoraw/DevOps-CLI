# todo.py

tasks = []

def add_task(task):
    tasks.append(task)
    return f"Task '{task}' added!"

def list_tasks():
    if not tasks:
        return "No tasks yet."
    return "\n".join([f"{i+1}. {t}" for i, t in enumerate(tasks)])

def remove_task(index):
    try:
        task = tasks.pop(index - 1)
        return f"Task '{task}' removed!"
    except IndexError:
        return "Invalid task number."

if __name__ == "__main__":
    while True:
        print("\n--- To-Do App ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            t = input("Enter task: ")
            print(add_task(t))
        elif choice == "2":
            print(list_tasks())
        elif choice == "3":
            num = int(input("Task number: "))
            print(remove_task(num))
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
