tasks = []

while True:
    print("\n== TO-DO LIST ==")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if not tasks:
            print("No tasks available.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            num = int(input("Enter task number to remove: "))
            if 0 < num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid number!")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
