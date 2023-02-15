def histogram(s):
    for i in s:
        print('*'*i)

s = list(map(int, input().split()))
histogram(s)