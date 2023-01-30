a = int(input())
b = int(input())
c = int(input())

if a % 2 > 0 and b % 2 > 0 and c % 2 > 0:
    print ((a + b + c) // 2 + 2)
elif a % 2 > 0 or b % 2 > 0 or c % 2 > 0:
    print ((a + b + c) // 2 + 1)
else:
    print ((a + b + c)// 2)