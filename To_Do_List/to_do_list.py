tasks = []
choice = 0

while choice != 4:
    print("1. Add Task, 2. View Task, 3. Remove Task, 4. Exit")
    choice = (int(input("Enter your number: ")))

    if choice == 1:
        type_task = input("What would you like to add?: ")
        tasks.append(type_task)
        print("Task added successfully")
    elif choice == 2:
        print(tasks)
    elif choice == 3:
        print(tasks)
        if len(tasks) == 0:
            print("You have no tasks to remove lol")
        elif len(tasks) >0:
            remove_task = (int(input("What number task would you like to remove?: ")))
            if remove_task > len(tasks):
                print("invalid input")
            else:
                tasks.pop(remove_task -1)
                print(tasks)
                print("Task removed successfully")

print("Thanks for using us!")