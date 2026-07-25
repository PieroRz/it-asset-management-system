from employee import Employee
from database import add_employee, get_all_employees, create_tables

def show_menu():
    print("\n=== IT Asset Management System ===")
    print("1. List employees")
    print("2. Add employee")
    print("3. Exit")

def main():

    while True:
        show_menu()

        option = input("Choose an option: ")
        if option == "1":
            employees = get_all_employees()
            for employee in employees:
                employee.display_info()

        elif option == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            new_employee = Employee(first_name, last_name)
            add_employee(new_employee)
            print("Employee added.")
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
