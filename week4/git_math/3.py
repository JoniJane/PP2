import math as m
n = int(input("number of side: "))
l = float(input("the length of a side: "))
a = l /(2*(m.tan(m.radians(180/n))))
area = int((n*l*a)/2)

print("the area of the polygon is:", area)