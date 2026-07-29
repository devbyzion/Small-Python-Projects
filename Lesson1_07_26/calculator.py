first_num = (int(input("Enter your first number: ")))
operation = input("Enter type of operation: ")
second_num = (int(input("Enter your second number: ")))
if operation == "+":
    print(first_num, operation, second_num, "=", first_num + second_num)
elif operation == "-":
    print(first_num, operation, second_num, "=", first_num - second_num)
elif operation == "*":
    print(first_num, operation, second_num, "=", first_num * second_num)
elif operation == "/":
    if second_num == 0:
        print("Cannot divide by zero")
    else:
        print(first_num, operation, second_num, "=", first_num / second_num)
else: 
    print("Invalid operation")

