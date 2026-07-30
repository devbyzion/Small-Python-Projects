def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


while True:

    try:
        first_num = (int(input("Enter your first number: ")))
    except ValueError:
        print("Please enter a number")
        continue
        
    operation = input("Enter operation: ")
    if operation not in ["+", "-", "*", "/"]:
        print("Invalid operation")
        continue
    try:
        second_num = (int(input("Enter your second number: ")))
    except ValueError:
        print("Please enter a number")
        continue

    if operation == "+":
        answer = add(first_num, second_num)
    elif operation == "-":
        answer = subtract(first_num, second_num)
    elif operation == "*":
        answer = multiply(first_num, second_num)
    else: 
        if second_num == 0:
            print("Cannot divide by zero")
            continue
        answer = divide(first_num, second_num)

    print("Answer:", answer)