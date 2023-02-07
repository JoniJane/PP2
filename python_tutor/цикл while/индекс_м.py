max, len = 0, 0
n, i = -1, -1
while n != 0:
    n = int(input())
    if n > max:
        max = n
        i = len
    len += 1
print(i)