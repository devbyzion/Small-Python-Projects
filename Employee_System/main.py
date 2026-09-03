from employee import Employee
from payroll import salary_report
from database import create_table, add_employee, get_employees, get_employee, update_employee, delete_employee

create_table()

menu = ("\n1. Add employee \n2. View all employees \n3. Find employee \n4. Update employee \n5. Delete employee \n6. Exit\n")

print("\n=== EMPLOYEE SYSTEM ===\n")


while True:
    print(menu)
    
    try:
        choice = int(input("Select an option:\n"))
    except ValueError:
        print("Please enter a valid number")
        continue
    
    if choice not in [1, 2, 3, 4, 5, 6]:
        print("Invalid Input")
        continue
         
    
    elif choice == 1:
        print("\n=== ADD EMPLOYEE ===\n")
        
        name = input("Name: ")
        position = input("Position: ")
        salary = int(input("Salary: R "))
        
        add_employee(name, position, salary)
        
        print(f"\nEmployee {name} has been created\n")
        continue
        
    elif choice == 2:
        print("\n=== All EMPLOYEES ===\n")
        
        employees = get_employees()
        if not employees:
            print("There are no employees yet")
            continue
        
        for employee in employees:
            print(f"ID: {employee[0]} \nName: {employee[1]} \nPosition: {employee[2]} \nSalary: R{employee[3]:,}\n")
        continue
    
    elif choice == 3:
        print("\n=== FIND EMPLOYEE ===\n")
        
        find = int(input("Please enter the ID of the employee \n"))
        
        employee = get_employee(find)
        
        if employee is None:
            print("Employee not found")
            continue
    
        print("\n=== EMPLOYEE FOUND ===\n")
        print(f"ID: {employee[0]} \nName: {employee[1]} \nPosition: {employee[2]} \nSalary: R{employee[3]:,}")
        continue
    
    elif choice == 4:
        print("\n=== UPDATE EMPLOYEE ===\n")
        
        id = int(input("Enter user ID: "))
        
        employee =  get_employee(id)
        
        if employee is None:
            print("Employee not found")
            continue
        print(f"ID: {employee[0]} \nName: {employee[1]} \nPosition: {employee[2]} \nSalary: R{employee[3]:,}")
        
        position = employee[2]
        salary = employee[3]
        emp_menu = ("\n1. Position \n2. Salary")
        print(emp_menu)
        choice = int(input("What would you like to update?\n"))
        
        
        if choice == 1:
            position = input("Enter new position: ")
            
            print(f"ID: {employee[0]} \nName: {employee[1]} \nPosition: {employee[2]} -- {position} \nSalary: R{employee[3]:,} -- {employee[3]:,}")
            
            confirm = input("YOU ARE ABOUT TO UPDATE AN EMPLOYEE \nARE YOU SURE? (Y/N)\n")
            
            if confirm.upper() == "Y":
                update_employee(position, salary, id)
                print(f"\nEmployee has been updated\n")
                continue
            else:
                continue
            
        elif choice == 2:
            salary = int(input("Enter new salary: "))
            print(f"ID: {employee[0]} \nName: {employee[1]} \nPosition: {employee[2]} -- {employee[2]} \nSalary: R{employee[3]:,} -- {salary:,}")
            
            confirm = input("YOU ARE ABOUT TO UPDATE AN EMPLOYEE \nARE YOU SURE? (Y/N)\n")
            if confirm.upper() == "Y":
                update_employee(position, salary, id)
                print(f"\nEmployee has been updated\n")
                continue
            else:
                continue
    
    elif choice == 5:
        print("\n=== DELETE EMPLOYEE ===\n")
        
        id = int(input("Enter user ID: "))
        
        employee = get_employee(id)
        if employee is None:
                    print("Employee not found")
                    continue
        print(f"ID: {employee[0]} \nName: {employee[1]} \nPosition: {employee[2]} \nSalary: R{employee[3]:,}")
                
        confirm = input ("\nYOU ARE ABOUT TO DELETE A EMPLOYEE\n ARE YOU SURE (Y/N)\n")
        
        if confirm.upper() == "Y":
            delete_employee(id)
            print("\nEmployee has been deleted\n")
            continue
        else: 
            continue
        
    elif choice == 6:
        print("Thank you for using our system!")
        break