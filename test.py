


class A():
    def __init__(self, number):
        self._number = number

a = A(10)
print(a._number)
a._number = 12
print(a._number)

