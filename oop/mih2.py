class A:
    def process(self):
        print("process() in A")


class B(A):
    pass


class C(A):
    def process(self):
        print("process() in C")


class D(B, C):
    pass


print(D.mro())
cobj = D()
cobj.process()
