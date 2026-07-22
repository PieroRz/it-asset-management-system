import sqlite3
from employee import Employee

DATABASE_PATH = "data/assets.db"

def get_connection():
    return sqlite3.connect(DATABASE_PATH)

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assets (
        asset_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        asset_type TEXT NOT NULL,
        brand TEXT NOT NULL,
        serial_number TEXT UNIQUE NOT NULL,
        status TEXT NOT NULL,
        employee_id INTEGER,
        FOREIGN KEY (employee_id)
            REFERENCES employees(employee_id)
    )
    """)

    connection.commit()
    connection.close()

def add_employee(employee):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO employees (
        employee_id,
        first_name,
        last_name
    )
    VALUES (?, ?, ?)
    """, (
        employee.employee_id,
        employee.first_name,
        employee.last_name
    ))

    connection.commit()
    connection.close()

def get_all_employees():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")

    rows = cursor.fetchall()

    employees = [
        Employee(
            row[0],
            row[1],
            row[2]
        )
        for row in rows
    ]

    connection.close()

    return employees