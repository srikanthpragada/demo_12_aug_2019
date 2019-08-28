class A:
    def process(self):
        print("process() in A")


class B(A):
    def process(self):
        print("process() in B")


class C(B):
    pass

cobj = C()
cobj.process()

