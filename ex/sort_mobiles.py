import re

f = open("mobiles.txt", "rt")
mobiles = set()

for line in f:
    # look for name
    numbers = re.findall(r'\d+', line)
    for number in numbers:
        if len(number) == 10:
            mobiles.add(number)

f.close()
for m in sorted(mobiles):
    print(m)
