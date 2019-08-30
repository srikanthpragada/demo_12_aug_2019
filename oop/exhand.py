try:
    num = int(input("Enter a number :"))
    if 10 % num == 0:
        print("10 is divisible by ", num)
    else:
        print("10 is not divisible by ", num)
except ValueError as ex:
    print("Sorry! Invalid number!")
except ZeroDivisionError as ex:
    print("Sorry! Number cannot be zero!")
finally:
    pass
