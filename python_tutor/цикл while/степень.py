n = int(input())
p = 0
while 2**p <= n:
    p += 1
print(p-1, 2**(p-1))