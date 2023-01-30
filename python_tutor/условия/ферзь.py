a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == c or b == d or abs(c-a)==abs(d-b):
    print('YES')
else:
    print('NO')