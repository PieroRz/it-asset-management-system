class Employee:
    def __init__(self, first_name, last_name, employee_id=None):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def display_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"First Name: {self.get_full_name()}")

    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "first_name": self.first_name,
            "last_name": self.last_name
        }