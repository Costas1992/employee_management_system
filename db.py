import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def create_connection():
    """ connect to the database """
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        # CREATE DATABASE IF MISSING
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        cursor.close()
        
        # CONNECT TO THE DB
        connection.database = DB_CONFIG['database']
        return connection
    
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

def create_tables(connection):
    """ create employees table."""
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            phone VARCHAR(50) NOT NULL
        )
    ''')
    connection.commit()
    cursor.close()
    
def insert_employee(connection, employee):
    """Add a new employee."""
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO employees (first_name, last_name, email, phone)
        VALUES (%s, %s, %s, %s)
    ''', (employee["first_name"], employee["last_name"], employee["email"], employee["phone"]))
    connection.commit()
    cursor.close()
    
def get_all_employees(connection):
    """List all employees."""
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    cursor.close()
    return rows

def get_employee_by_id(connection, employee_id):
    """Get employee by id."""
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees WHERE id = %s", (employee_id,))
    row = cursor.fetchone()
    cursor.close()
    return row

def update_employee(connection, employee, update_employee):
    """Update employee by info."""
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE employees
        SET first_name = %s, last_name = %s, email = %s, phone = %s
        WHERE id = %s
    ''', (
        update_employee["first_name"],
        update_employee["last_name"],
        update_employee["email"],
        update_employee["phone"],
        employee_id
    ))
    connection.commit()
    cursor.close()
    
def delete_employee(connection, employee_id):
    """Delete employee by id."""
    cursor = connection.cursor(dictionary=True)
    cursor.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
    connection.commit()
    cursor.close()
    
def close_connection(connection):
    """Close database connection."""
    if connection:
        connection.close()