import re

f = open("persons.txt", "rt")
persons = {}

for line in f:
    # look for name
    m = re.search('[A-Za-z ]+', line)
    if m is None:
        continue

    name = m.group().strip(" ")

    # Look for mobile number
    m = re.search(r'\d+', line)
    if m is None:
        continue

    persons[name] = m.group()

f.close()
for n, m in sorted(persons.items()):
    print(f"{n:15} {m}")
