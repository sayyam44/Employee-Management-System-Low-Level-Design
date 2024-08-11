#Facade pattern.
import pickle
from EmployeeFactory import EmployeeFactory

class HRFacade:
    def __init__(self, employee_factory):
        self.employee_factory = employee_factory
        self.employees = []

    def add_employee(self, employee_type, emp_id, *args):
        try:
            # Check if employee with this ID already exists
            if self.find_employee(emp_id):
                print(f"Error: Employee with ID {emp_id} already exists.")
                return
            
            # Create and add new employee
            employee = self.employee_factory.create_employee(employee_type, emp_id, *args)
            self.employees.append(employee)
            print("Employee added successfully.")
        except ValueError as e:
            print(f"Error creating employee: {e}")

    def get_employee_details(self):
        try:
            return [employee.get_details() for employee in self.employees]
        except Exception as e:
            print(f"Error getting employee details: {e}")
            return []

    def find_employee(self, emp_id):
        try:
            return next((employee for employee in self.employees if employee.emp_id == emp_id), None)
        except Exception as e:
            print(f"Error finding employee: {e}")
            return None

    def delete_employee(self, emp_id):
        try:
            employee_to_delete = self.find_employee(emp_id)
            if employee_to_delete:
                self.employees.remove(employee_to_delete)
                print(f"Employee with ID {emp_id} has been deleted.")
            else:
                print(f"Error: Employee with ID {emp_id} does not exist.")
        except Exception as e:
            print(f"Error deleting employee: {e}")

    def save_to_file(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.employees, file)
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving data: {e}")
