import sqlite3
from employee import Employee

def get_connection():
    connection = sqlite3.connect("Employee_System/database/employee.db")
    cursor = connection.cursor()
    return connection, cursor

def create_table():
    connection, cursor = get_connection()

    cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT,
                position TEXT,
                salary INTEGER
                );"""
    )
    
    connection.commit()
    connection.close()  

def add_employee(name, position, salary):
    connection, cursor = get_connection()
    
    cursor.execute("""
                INSERT INTO employees(name, position, salary)
                VALUES (?, ?, ?);
                   """, 
                (name, position, salary)
    )
    
    connection.commit()
    employee_id = cursor.lastrowid
    connection.close()
    return employee_id
    
def get_employees():
    connection,cursor = get_connection()
    
    cursor.execute("SELECT * FROM employees")
    
    rows = cursor.fetchall()
    employees = []
    
    for row in rows:
        employees.append(Employee(
            row[0],
            row[1],
            row[2],
            row[3]
            )
        )
        
    connection.close()
    return employees

def get_employee(id):
    connection,cursor = get_connection()
    
    cursor.execute("""
                   SELECT * FROM employees 
                   WHERE id = ?""",
                   (id,)
    )
    
    row = cursor.fetchone()
    connection.close()
    
    if row is not None:
        employee = Employee(
            row[0],
            row[1],
            row[2],
            row[3]
        )
    else:
        return None
    return employee

def update_employee(position, salary, id):
    connection,cursor = get_connection()
    
    cursor.execute("""
                   UPDATE employees
                   SET position = ?, salary = ?
                   WHERE id = ?""",
                   (position, salary, id)
    )
    
    connection.commit()
    connection.close()
    
def delete_employee(id):
    connection,cursor = get_connection()
    
    cursor.execute("""
                   DELETE FROM employees
                   WHERE id = ?""",
                   (id,)
    )
    
    connection.commit()
    connection.close()
    
   