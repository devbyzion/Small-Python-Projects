from employee import Employee
# from payroll import calculate_bonus
# from payroll import calculate_tax
# from payroll import calculate_net_salary
from payroll import salary_report

emp = Employee("Zion", 30000)

# bonus = calculate_bonus(emp.salary)
# tax = calculate_tax(emp.salary)
# net = calculate_net_salary(emp.salary)

salary_rep = salary_report(emp.salary)
print(emp.display_info())

print(salary_rep)