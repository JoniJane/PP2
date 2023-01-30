n = int(input())
m = int(input())
x = int(input())
y = int(input())

print(min(x,y, min(n,m)-x, max(n,m)-y))