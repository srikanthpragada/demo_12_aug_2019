def swap(n1, n2):
    n1, n2 = n2, n1
    print('Swap function : ', n1, n2)


def removefirst(lst):
    lst.remove(lst[0])


a = 10
b = 20

swap(a, b)
print(a, b)

l = [1, 2, 3, 4, 5]
removefirst(l)
print(l)
