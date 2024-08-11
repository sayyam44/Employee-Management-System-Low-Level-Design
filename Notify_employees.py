#Observer pattern to notify employees about updates.

class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

class EmployeeObserver:
    def update(self, message):
        print(f"Notification to Employee: {message}")

class HRSystem(Observable):
    def __init__(self):
        super().__init__()

    def update_attendance(self, employee):
        self.notify_observers(f"Attendance updated for {employee.name}")
