sum = 0
cnt = 0
n = int(input())
while n != 0:
    sum += n
    cnt += 1
    n = int(input())
print(sum / cnt)