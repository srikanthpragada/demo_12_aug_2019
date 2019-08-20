# Name and multiple phones numbers

persons = {}

while True:
    name = input("Enter name [end to stop] :")
    if name == "end":
        break

    phone = input("Enter mobile number       :")
    if name in persons:
        persons[name].add(phone)  # add new phone to existing set
    else:
        persons[name] = {phone}   # add new entry to dict

for name, phones in sorted(persons.items()):
    print(f"{name:15}  { ','.join(phones) }")
