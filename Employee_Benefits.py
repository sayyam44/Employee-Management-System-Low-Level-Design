# Decorator pattern to add benefits to employees.

class EmployeeDecorator:
    def __init__(self, employee):
        self._employee = employee

    def get_details(self):
        return self._employee.get_details()

class HealthInsuranceDecorator(EmployeeDecorator):
    def get_details(self):
        return f"{super().get_details()}, Health Insurance: Included"

class RetirementPlanDecorator(EmployeeDecorator):
    def get_details(self):
        return f"{super().get_details()}, Retirement Plan: Included"
