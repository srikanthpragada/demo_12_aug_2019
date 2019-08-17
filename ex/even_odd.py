nums = []

while True:
    n = int(input("Enter a number :"))
    if n == 0:
        break
    nums.append(n)

for n in nums:
    if n % 2 == 0:
        print(n)

for n in nums:
    if n % 2 != 0:
        print(n)


