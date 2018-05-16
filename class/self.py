class Foo:
    def func1():
        print("function 1 is called")
    def func2(self):
        print(id(self))
        print("function 2 is called")


""" self is instance of class """
foo = Foo()
foo.func2()
print(id(foo))
Foo.func1()
