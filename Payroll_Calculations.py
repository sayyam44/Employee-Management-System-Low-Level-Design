#Strategy pattern for calculating payroll.

class PayrollStrategy:
    def calculate_payroll(self, employee):
        raise NotImplementedError("Subclasses should implement this method")

class FullTimePayrollStrategy(PayrollStrategy):
    def calculate_payroll(self, employee):
        return employee.salary

class PartTimePayrollStrategy(PayrollStrategy):
    def calculate_payroll(self, employee):
        return employee.hourly_rate * 160  # Assume 160 working hours per month
