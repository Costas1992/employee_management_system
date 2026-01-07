from db import (
    create_connection, create_tables, insert_employee,
    get_all_employees, get_employee_by_id,
    update_employee, delete_employee, close_connection,
)

def print_menu():
    print("\nEmployee Management System")
    print("1. Add employee")
    print("2. List all employees")
    print("3. Get employee by ID")
    print("4. Update employee")
    print("5. Delete employee")
    print("6. Exit")
    
def promt_employee():
    return {
        "first_name": input("First name: ").strip(),
        "last_name": input("Last name: ").strip(),
        "email": input("Email: ").strip(),
        "phone": input("Phone: ").strip(),
    }

def main():
    connection = create_connection()
    if connection is None:
        return
    
    create_tables(connection)
    
    while True:
        print_menu()
        choice = input("Choose (1-6): ").strip()
        
        if choice == "1":
            employee = promt_employee()
            insert_employee(connection, employee)
            print("Employee added!")
            
        elif choice == "2":
            employees = get_all_employees(connection)
            if not employees:
                print("No employees found.")
            else:
                for e in employees:
                    print(f"{e["id"]} {e["first_name"]} {e["last_name"]} {e["email"]} {e["phone"]}")
                    
        elif choice == "3":
            employee_id = int(input("Employee ID: "))
            employee = get_employee_by_id(connection, employee_id)
            if employee:
                print(employee)
            else:
                print("Employee not found!")
                
        elif choice == "4":
            employee_id = int(input("Employee ID to update: "))
            employee = promt_employee()
            update_employee(connection, employee, employee_id)
            print("Employee updated!")
            
        elif choice == "5":
            employee_id = int(input("Employee ID to delete: "))
            delete_employee(connection, employee_id)
            print("Employee deleted!")
            
        elif choice == "6":
            break
            
        else:
            print("Please choose a number 1-6.")
            
    close_connection(connection)
    print("Bye")
  
if __name__ == "__main__":
    main()

