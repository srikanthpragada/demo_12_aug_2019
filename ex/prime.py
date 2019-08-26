import sys


def isprime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    else:
        return True


for n in sys.argv[1:]:
    if isprime(int(n)):
        print(f"{n} is prime number")
    else:
        print(f"{n} is not prime number")
