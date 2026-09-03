import sqlite3

def create_table():
    connection = sqlite3.connect("Employee_System/database/employee.db")
    cursor = connection.cursor()

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
    connection = sqlite3.connect("Employee_System/database/employee.db")
    cursor = connection.cursor()
    
    cursor.execute("""
                INSERT INTO employees(name, position, salary)
                VALUES (?, ?, ?);
                   """, 
                (name, position, salary)
    )
    
    connection.commit()
    connection.close()
    
def get_employees():
    connection = sqlite3.connect("Employee_System/database/employee.db")
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    connection.close()
    return employees

def get_employee(id):
    connection = sqlite3.connect("Employee_System/database/employee.db")
    cursor = connection.cursor()
    
    cursor.execute("""
                   SELECT * FROM employees 
                   WHERE id = ?""",
                   (id,)
    )
    
    employee = cursor.fetchone()
    connection.close()
    return employee

def update_employee(position, salary, id):
    connection = sqlite3.connect("Employee_System/database/employee.db")
    cursor = connection.cursor()
    
    cursor.execute("""
                   UPDATE employees
                   SET position = ?, salary = ?
                   WHERE id = ?""",
                   (position, salary, id)
    )
    
    connection.commit()
    connection.close()
    
def delete_employee(id):
    connection = sqlite3.connect("Employee_System/database/employee.db")
    cursor = connection.cursor()
    
    cursor.execute("""
                   DELETE FROM employees
                   WHERE id = ?""",
                   (id,)
    )
    
    connection.commit()
    connection.close()