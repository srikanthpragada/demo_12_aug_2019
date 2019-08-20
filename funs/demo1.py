def add(n1, n2=0):
    return n1 + n2


def wish(*names):
    print(type(names))


wish("Abc","Xyz")

print(add(10, 20))
print(add(n2=10, n1=10))
print(add(10))
print(add('abc', 'xyz'))
