n = int(input())
a = 0
while n != 0:
    x = int(input())
    if x != 0 and n < x:
        a += 1
    n = x
print(a)