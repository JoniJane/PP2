class Shape:
    def area(self):
        return 0

class Rect(Shape):
    def __init__(self):
        self.length = int(input())
        self.width = int(input())
        new_a = self.length*self.width
        print(new_a)

s = Rect()
s.area()