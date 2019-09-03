import json

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return "{0}-{1}".format(self.name, self.email);


p = Person("Abc","abc@gmail.com")
jsonstr = json.dumps(p.__dict__)
print(jsonstr)
p2 = json.loads(jsonstr)
print(type(p2), p2)

