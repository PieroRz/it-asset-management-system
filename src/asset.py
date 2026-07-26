class Asset:
    def __init__(
        self,
        name,
        asset_type,
        brand,
        serial_number,
        status,
        employee_name=None,
        employee_id=None,
        asset_id=None
    ):
        self.asset_id = asset_id
        self.name = name
        self.asset_type = asset_type
        self.brand = brand
        self.serial_number = serial_number
        self.status = status
        self.employee_id = employee_id
        self.employee_name = employee_name

    def display_info(self):
        print(f"Asset ID: {self.asset_id}")
        print(f"Name: {self.name}")
        print(f"Type: {self.asset_type}")
        print(f"Brand: {self.brand}")
        print(f"Serial Number: {self.serial_number}")
        print(f"Status: {self.status}")
        print(f"Assigned to Employee: {self.employee_name}")

    def to_dict(self):
        return {
            "asset_id": self.asset_id,
            "name": self.name,
            "asset_type": self.asset_type,
            "brand": self.brand,
            "serial_number": self.serial_number,
            "status": self.status,
            "employee": self.employee.employee_name
        }