n = int(input())
sumn = 0
sumx = n
for x in range(1, n):
    sumn += int(input())
    sumx += x
print(sumx - sumn)