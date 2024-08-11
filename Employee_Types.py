#Bridge pattern to separate abstraction from implementation.

class Employee:
    def __init__(self, emp_id, name, age, designation):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.designation = designation

    def get_details(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Designation: {self.designation}"

class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, age, designation, salary):
        super().__init__(emp_id, name, age, designation)
        self.salary = salary

    def get_details(self):
        try:
            return f"{super().get_details()}, Salary: {self.salary}"
        except Exception as e:
            print(f"Error getting details for FullTimeEmployee: {e}")
            return "Error getting details"

class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, age, designation, hourly_rate):
        super().__init__(emp_id, name, age, designation)
        self.hourly_rate = hourly_rate

    def get_details(self):
        try:
            return f"{super().get_details()}, Hourly Rate: {self.hourly_rate}"
        except Exception as e:
            print(f"Error getting details for PartTimeEmployee: {e}")
            return "Error getting details"
