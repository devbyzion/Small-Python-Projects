s_name = input("Please enter your name: \n")
s_age = int(input("Please enter your age: \n"))
s_course = input("Please enter your course: \n")

student = {
    "name": s_name,
    "age": s_age,
    "course": s_course
    }

print ("Hello", student["name"])