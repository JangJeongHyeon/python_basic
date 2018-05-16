class Stock:
    market = "kospi"


if(__name__ == '__main__'):


    # When class is define namespace is generated as class name
    # All of method and variable info is save in namespace as dictionary

    print('='*30)
    print(dir())
    print('='*30)
    print(Stock.__dict__)
    print('='*30)

    # Instance is have own namespace
    s1 = Stock()
    s2 = Stock()

    print(dir())
    print('='*30)
    print(id(s1))
    print('='*30)
    print(id(s2))
    print('='*30)
    print(s1.__dict__) # it will be return empty namespace
    print('='*30)
    print(s2.__dict__)
    print('='*30)

    # assign value on the instance variable.
    s1.market = 'Kosdaq'

    # add variable in the namespace
    print(s1.__dict__)

    # check variable
    print(s1.market)
    print(s2.market)

    # if namespace is empty then they connect to class namespace