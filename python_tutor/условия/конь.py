a = int(input())
b = int(input())
c = int(input())
d = int(input())

if abs(c-a)==1 and abs(d-b)==2:
    print('YES')
elif abs(c-a)==2 and abs(d-b)==1:
    print('YES')
else:
    print('NO')