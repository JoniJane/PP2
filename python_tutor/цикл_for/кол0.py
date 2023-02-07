n = int(input())
sum = 0
for x in range(1, n+1):
    if int(input()) == 0:
        sum += 1
print(sum)