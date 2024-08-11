#Factory pattern.

from Employee_Types import FullTimeEmployee, PartTimeEmployee

class EmployeeFactory:
    def create_full_time_employee(self, emp_id, name, age, designation, salary):
        return FullTimeEmployee(emp_id, name, age, designation, salary)
    
    def create_part_time_employee(self, emp_id, name, age, designation, hourly_rate):
        return PartTimeEmployee(emp_id, name, age, designation, hourly_rate)
    
    def create_employee(self, employee_type, emp_id, name, age, designation, salary_or_hourly):
        if employee_type.lower() == "fulltime":
            return self.create_full_time_employee(emp_id, name, age, designation, salary_or_hourly)
        elif employee_type.lower() == "parttime":
            return self.create_part_time_employee(emp_id, name, age, designation, salary_or_hourly)
        else:
            raise ValueError("Invalid employee type")
