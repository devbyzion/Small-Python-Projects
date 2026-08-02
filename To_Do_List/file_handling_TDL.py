choice = 0

while True:
    print("To-Do List!")
    print("\n1. Add a taks.\n","2. View tasks.\n","3. Delete all tasks. \n","4. Exit\n")

#try is there for some error handling, user inputs str instead of int gives error
    try: 
        choice = int(input("Choose a number: \n"))
    except ValueError:
        print("Please choose a number")
        continue

    if choice == 1:
        file = open("Tasks.txt", "a")
        task_add = input("What task would you like to add?: \n")
        file.write(task_add + "\n")
        print("Task added successfully")
        file.close()
        continue

    elif choice == 2:
        print("Here is your tasks for the day!\n")
        file = open("Tasks.txt", "r")
        content = file.read()
        print(content)
        file.close()
        continue
    
    elif choice == 3:
        d_all = input("Would you like to delete all tasks?: Y/N \n")
        if d_all.upper() == "N":
            continue
        
        elif d_all.upper() == "Y": 
            file = open("Tasks.txt", "w")
            file.write("")
            print("All tasks has been deleted!")
            file.close()
            continue
    
    
    elif choice == 4:
        print("Thank you for using us!!!!")

    else:
        print("Invalid choice")
        continue
    
    break    

