from math import sqrt

class Point:
    def __init__(self):
        self.x1 = int(input('First x: '))
        self.y1 = int(input('First y: '))
    
    def show(self):
        print(self.x1, self.y1)
    
    def move(self):
        self.x2 = int(input('Second x: '))
        self.y2 = int(input('Second y: '))
    
    def dist(self):
        print(sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2))

p = Point()
p.move()
p.dist()
