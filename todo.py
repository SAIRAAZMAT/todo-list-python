my_tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        task = input("Enter the task you want to add: ")
        my_tasks.append(task)
        print(f"'{task}' has been added to your list!")

    elif choice == "2":
        if len(my_tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(my_tasks):
                print(f"{index + 1}. {task}")

    elif choice == "3":
        print("Goodbye! Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")