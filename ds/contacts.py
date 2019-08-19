persons = {}

while True:
    name = input("Enter name  [end to stop] :")
    if name == "end":
        break

    phone = input("Enter mobile number       :")
    persons[name] = phone

for name, phone in sorted(persons.items()):
    print(f"{name:15}  {phone}")
