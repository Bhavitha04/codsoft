tasks = []

while True:
    choice = input("1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit\nEnter your choice: ")
    
    if choice == 'a':
        tasks.append(input("Enter task: "))
    elif choice == 'b':
        task = input("Enter task to remove: ")
        tasks.remove(task) if task in tasks else print("Task not found.")
    elif choice == 'c':
        print("\n".join(tasks) if tasks else "No tasks yet.")
    elif choice == 'd':
        break
    else:
        print("Invalid choice.")