from employee import Employee
from database import add_employee, get_all_employees

employee = Employee(
    1,
    "Juan",
    "Perez"
)

add_employee(employee)

employees = get_all_employees()

for employee in employees:
    employee.display_info()