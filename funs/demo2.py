def add(n1, n2):
    return n1 + n2


def mul(n1, n2):
    return n1 * n2


def process(n1, n2, opfun):
    print(opfun(n1, n2))


process(10, 20, mul)

process(10, 20, lambda a, b: a + b)
