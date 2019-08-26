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
    def __init__(self, name, salary):
        # object attributes
        self.name = name
        self.salary = salary  # Private

    def print_details(self):
        print(self.name, self.salary)

    def net_salary(self):
        return self.salary + (self.salary * Employee.hraper / 100)


e1 = Employee("Scott", 60000)
e2 = Employee("Tom", 40000)
e3 = Employee("Tom", 40000)
print(e2 == e3)
e4 = Employee.create_trainee("Bill")
e4.print_details()

# e1.print_details()
Employee.set_hraper(40)
print(e1.net_salary())
print(e2.net_salary())

