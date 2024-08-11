# Adapter pattern .
#Adapter Pattern - Employee_Adapter.py
#Factory Pattern - EmployeeFactory.py
#Facade Pattern - Employee_Functionalities.py
#Observer Pattern - Notify_employees.py
#Strategy Pattern - Payroll_Calculations.py
#Decorator Pattern - Employee_Benefits.py
#Chain of Responsibility Pattern - Request_Handling.py
#Bridge Pattern - Employee_Types.py
from ThirdPartyHRSystem import ThirdPartyHRSystem

class EmployeeAdapter:
    def __init__(self, third_party_hr_system):
        self.third_party_hr_system = third_party_hr_system

    def get_employees(self):
        employees = self.third_party_hr_system.get_employee_details()
        # Convert third-party employee details to our internal format
        return [{"id": emp["id"], "name": emp["name"], "age": emp["age"], "designation": emp["designation"]} for emp in employees]
