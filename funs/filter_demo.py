nums = [10, 11, 15, 20, 55]
enums = []

for n in nums:
    if n % 2 == 0:
        enums.append(n)


def iseven(n):
    print(n)
    return n % 2 == 0


enums = filter(iseven, nums)
for n in enums:
    print(n, end = ' ')


enums = filter(lambda n : n % 2 == 0, nums)

