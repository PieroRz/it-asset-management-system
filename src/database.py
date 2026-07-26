import sqlite3
from employee import Employee
from asset import Asset

DATABASE_PATH = "data/assets.db"

def get_connection():
    return sqlite3.connect(DATABASE_PATH)

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assets (
        asset_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        first_name,
        last_name
    )
    VALUES (?, ?)
    """, (
        employee.first_name,
        employee.last_name
    ))

    employee.employee_id = cursor.lastrowid

    connection.commit()
    connection.close()

def get_all_employees():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")

    rows = cursor.fetchall()

    employees = [
        Employee(
            row[1],  # first_name
            row[2],  # last_name
            row[0]   # employee_id
        )
        for row in rows
    ]

    connection.close()

    return employees

def add_asset(asset):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO assets (
        name,
        asset_type,
        brand,
        serial_number,
        status,
        employee_id
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        asset.name,
        asset.asset_type,
        asset.brand,
        asset.serial_number,
        asset.status,
        asset.employee_id
    ))

    asset.asset_id = cursor.lastrowid

    connection.commit()
    connection.close()

def get_all_assets():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT assets.asset_id,assets.name,assets.asset_type,assets.brand,assets.serial_number,assets.status,employees.first_name || ' ' || employees.last_name AS employee_name, assets.employee_id FROM assets LEFT JOIN employees ON assets.employee_id = employees.employee_id GROUP BY assets.asset_id;")

    rows = cursor.fetchall()

    assets = [
        Asset(
            row[1],  # name
            row[2],  # asset_type
            row[3],  # brand
            row[4],  # serial_number
            row[5],  # status
            row[6],  # employee_name
            row[7],  # employee_id
            row[0]   # asset_id
        )
        for row in rows
    ]

    connection.close()

    return assets

def delete_asset(asset_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM assets WHERE asset_id = ?", (asset_id,))

    connection.commit()
    connection.close()