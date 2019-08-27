class Employee:
    # class attributes
    hraper = 30

    # Static method or class method
    @staticmethod
    def set_hraper(value):
        Employee.hraper = value

    @classmethod
    def create_trainee(cls, name):
        e = cls(name, 0)
        return e

    # Constructor
    def __init__(self, name, salary=0):
        # object attributes
        self.name = name
        self.salary = salary  # Private

    def print_details(self):
        print(self.name, self.salary)

    @property
    def net_salary(self):
        return self.salary + (self.salary * Employee.hraper / 100)

    def __eq__(self, other):
        return self.name == other.name and self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __str__(self):
        return f"{self.name} - {self.salary}"

    def __int__(self):
        return self.salary


e2 = Employee("Tom", 50000)
print(e2)
print(e2.net_salary)
