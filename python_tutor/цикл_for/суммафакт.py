n = int(input())
fact = 1
sum = 0
for x in range(1, n+1):
    fact*=x
    sum += fact
print(sum)