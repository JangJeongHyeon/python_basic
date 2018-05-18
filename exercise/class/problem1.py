class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x
    
    def sety(self, y):
        self.y = y
    
    def get(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


if(__name__ == '__main__'):

    point = Point(0,0)
    print(point.get())
    point.move(1,-1)
    print(point.get())
    point.setx(10)
    print(point.get())
    point.sety(20)
    print(point.get())