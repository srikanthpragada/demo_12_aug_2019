import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"


p = Person("Abc", 30)
s = json.dumps(p.__dict__)
print(s)  # Json
d = json.loads(s)
print(d)  # Dict
