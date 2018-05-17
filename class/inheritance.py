class Parent:
    def can_sing(self):
        print('Sing a song')


class LuckyChild(Parent):
    pass


class UnluckyChlid:
    pass


class LuckyChild2(Parent): 
    def can_dance(self):
        print('Shuffle Dance')



father = Parent()
father.can_sing()

child = LuckyChild()
child.can_sing()

child2 = UnluckyChlid()

print(child.__dir__())
print(child2.__dir__())

child3 = LuckyChild2()
child3.can_dance()
child3.can_sing()