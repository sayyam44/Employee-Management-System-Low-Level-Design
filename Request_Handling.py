#Chain of Responsibility pattern to handle different types of requests.

class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        raise NotImplementedError("Subclasses should implement this method")

class LeaveRequestHandler(Handler):
    def handle_request(self, request):
        if request.type == "Leave":
            print(f"Handling leave request for {request.employee.name}")
        elif self.successor:
            self.successor.handle_request(request)

class SalaryRequestHandler(Handler):
    def handle_request(self, request):
        if request.type == "Salary":
            print(f"Handling salary request for {request.employee.name}")
        elif self.successor:
            self.successor.handle_request(request)

class Request:
    def __init__(self, request_type, employee):
        self.type = request_type
        self.employee = employee
