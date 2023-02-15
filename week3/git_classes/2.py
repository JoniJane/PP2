class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self):
        self.length = int(input())
        new_a = self.length**2
        print(new_a)

s = Square()
s.area()