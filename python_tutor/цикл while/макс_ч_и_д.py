n = int(input())
max, max2 = 0, 0
while n!=0:
    m = int(input())
    if m == n:
        max += 1
        if max > max2:
            max2 = max
    else:
        max =0
    n = m
print(max2 + 1)
