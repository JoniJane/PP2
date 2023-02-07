a = int(input())
b = int(input())
if b > a:
    for x in range(a, b + 1):
        print(x)
else:
    for x in range(a, b - 1, -1):
        print(x)