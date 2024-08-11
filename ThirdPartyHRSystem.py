#external system integration (adapter pattern).

class ThirdPartyHRSystem:
    def get_employee_details(self):
        # Simulate getting employee details from a third-party system
        return [{"id": 3, "name": "John Doe", "age": 30, "designation": "Developer"}]
