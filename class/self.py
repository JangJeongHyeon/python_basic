class Foo:
    def func1():
        print("function 1 is called")
    def func2(self):
        print(id(self))
        print("function 2 is called")
    def func3(self):
        print(self.__str__)



""" self is instance of class """
foo = Foo()
foo.func2()
print(id(foo))
Foo.func1()
f3 = Foo()
print(f3)
print(id(f3))
print(Foo.func3(f3))