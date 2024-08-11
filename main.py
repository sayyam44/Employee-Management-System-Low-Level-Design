from ThirdPartyHRSystem import ThirdPartyHRSystem
from Employee_Adapter import EmployeeAdapter
from EmployeeFactory import EmployeeFactory
from Employee_Functionalities import HRFacade
from Notify_employees import HRSystem, EmployeeObserver
from Request_Handling import LeaveRequestHandler, SalaryRequestHandler, Request
from Payroll_Calculations import FullTimePayrollStrategy, PartTimePayrollStrategy
from Employee_Benefits import HealthInsuranceDecorator, RetirementPlanDecorator
from Employee_Types import FullTimeEmployee, PartTimeEmployee
#Adapter Pattern - Employee_Adapter.py
#Facade Pattern - Employee_Functionalities.py
#Observer Pattern - Notify_employees.py
#Chain of Responsibility Pattern - Request_Handling.py
#Strategy Pattern - Payroll_Calculations.py
#Decorator Pattern - Employee_Benefits.py
#Factory Pattern - EmployeeFactory.py
#Bridge Pattern - Employee_Types.py

# Adapter Pattern
third_party_hr_system = ThirdPartyHRSystem()
employee_adapter = EmployeeAdapter(third_party_hr_system)
external_employees = employee_adapter.get_employees()

# Factory Pattern
employee_factory = EmployeeFactory()

# Facade Pattern
hr_facade = HRFacade(employee_factory)

# Adding initial employees
hr_facade.add_employee("fulltime", 1, "Alice", 28, "Manager", 60000)
hr_facade.add_employee("parttime", 2, "Bob", 22, "Intern", 20)

# Adding external employees 
for emp in external_employees:
    hr_facade.add_employee("FullTime", emp["id"], emp["name"], emp["age"], emp["designation"], 50000)

# Observer Pattern
hr_system = HRSystem()
employee_observer = EmployeeObserver()
hr_system.add_observer(employee_observer)

# Notifying employees
for employee in hr_facade.employees:
    hr_system.update_attendance(employee)

# Chain of Responsibility Pattern
leave_handler = LeaveRequestHandler()
salary_handler = SalaryRequestHandler(leave_handler)

# Automatically handle leave and salary requests for the first two employees
request1 = Request("Leave", hr_facade.employees[0])
request2 = Request("Salary", hr_facade.employees[1])
salary_handler.handle_request(request1)
salary_handler.handle_request(request2)

# Strategy Pattern
full_time_strategy = FullTimePayrollStrategy()
part_time_strategy = PartTimePayrollStrategy()

for employee in hr_facade.employees:
    try:
        if isinstance(employee, FullTimeEmployee):
            print(f"Payroll for {employee.name}: {full_time_strategy.calculate_payroll(employee)}")
        elif isinstance(employee, PartTimeEmployee):
            print(f"Payroll for {employee.name}: {part_time_strategy.calculate_payroll(employee)}")
    except Exception as e:
        print(f"Error calculating payroll for {employee.name}: {e}")

# Decorator Pattern
decorated_employee = HealthInsuranceDecorator(hr_facade.employees[0])
decorated_employee = RetirementPlanDecorator(decorated_employee)
print(decorated_employee.get_details())

# User Interaction
while True:
    try:
        print("\n1. Add Employee")
        print("2. Delete Employee")
        print("3. List Employees")
        print("4. Save to File")
        print("5. Exit")
        choice = int(input("\nEnter your choice: "))

        if choice == 1:  # Add Employee
            emp_type = input("Enter employee type (FullTime/PartTime): ")
            emp_id = int(input("Enter employee ID: "))
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            designation = input("Enter designation: ")
            salary_or_hourly = float(input("Enter salary (for FullTime) or hourly rate (for PartTime): "))
            hr_facade.add_employee(emp_type, emp_id, name, age, designation, salary_or_hourly)

        elif choice == 2:  # Delete Employee
            emp_id = int(input("Enter ID of the employee to delete: "))
            hr_facade.delete_employee(emp_id)

        elif choice == 3:  # List Employees
            for detail in hr_facade.get_employee_details():
                print(detail)

        elif choice == 4:  # Save to File
            filename = input("Enter filename to save data: ").strip()
            if not filename.endswith(".pkl"):
                filename += ".pkl"
            hr_facade.save_to_file(filename)

        elif choice == 5:  # Exit
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    except ValueError:
        print("Invalid input. Please enter the correct information.")
    except Exception as e:
        print(f"An error occurred: {e}")
