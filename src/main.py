from employee import Employee
from asset import Asset
from database import add_employee, get_all_employees, add_asset, get_all_assets, delete_asset

def show_menu_principal():
    print("\n=== IT Asset Management System ===")
    print("1. Assets")
    print("2. Employees")
    print("3. Exit")

def show_menu_asset():
    print("\n=== Asset Management ===")
    print("1. List assets")
    print("2. Add asset")
    print("3. Delete asset")
    print("4. Exit")

def show_menu_employee():
    print("\n=== Employee Management ===")
    print("1. List employees")
    print("2. Add employee")
    print("3. Exit")

def main():

    while True:
        show_menu_principal()

        option = input("Choose an option: ")
        if option == "1":
            show_menu_asset()
            option = input("Choose an option: ")

            if option == "1":
                assets = get_all_assets()
                for asset in assets:
                    asset.display_info()
            elif option == "2":
                name = input("Enter asset name: ")
                asset_type = input("Enter asset type: ")
                brand = input("Enter asset brand: ")
                serial_number = input("Enter asset serial number: ")
                status = input("Enter asset status: ")

                employees = get_all_employees()
                for employee in employees:
                    employee.display_info()

                employee_id_input = input("Enter employee ID (or leave blank if not assigned): ")
                employee_id = int(employee_id_input) if employee_id_input else None

                new_asset = Asset(
                    name=name,
                    asset_type=asset_type,
                    brand=brand,
                    serial_number=serial_number,
                    status=status,
                    employee_id=employee_id
                )
                add_asset(new_asset)
                print("Asset added.")
            elif option == "3":
                asset_id = input("Enter asset ID to delete: ")
                delete_asset(asset_id)
                print("Asset deleted.")
            elif option == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")
        elif option == "2":
            show_menu_employee()
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
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
