x, z, i = 0, 0, 0
y =1
n = int(input())
while x <= n:
    x = y + z
    y,z = x,y
    i += 1
if (n == z):
    print(i)
else:
    print(-1)