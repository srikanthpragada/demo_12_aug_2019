# To calculate sum of factors for the given number

num = int(input("Enter a number :"))
sum = 0
for i in range(1, num // 2 + 1):
    if num % i == 0:
        sum += i

print("Sum of factors :", sum)
