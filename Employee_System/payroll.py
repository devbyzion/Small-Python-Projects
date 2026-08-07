def calculate_bonus(salary):
    return salary * 0.10

def calculate_tax(salary):
    return salary * 0.20

def calculate_net_salary(salary):
    return salary + calculate_bonus(salary) - calculate_tax(salary)

def salary_report(salary):
    return (f"Salary: {salary} \nBonus: {calculate_bonus(salary)} \nTax: {calculate_tax(salary)} \nNet Salary: {calculate_net_salary(salary)}")