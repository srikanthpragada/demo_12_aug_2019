v1 = 1  # Global variable


def f1():
    global v1
    v1 = 0
    v2 = 10  # enclosing

    def f2():
        nonlocal v2
        v2 = 100
        v3 = 20  # Local variable
        print(v1, v2, v3)

    f2()  # call f2()
    print(v1, v2)


f1()
