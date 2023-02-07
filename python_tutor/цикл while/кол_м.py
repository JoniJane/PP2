m = 0
cnt = 0
n = -1
while n != 0:
    n = int(input())
    if n > m:
        m, cnt = n, 1
    elif n == m:
        cnt += 1        
print(cnt)
