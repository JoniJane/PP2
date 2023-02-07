s = str(input())
if s.count('f')==1:
    print(-1)
elif s.count('f')>1:
    print(s.find('f', s.find('f')+1))
else:
    print(-2)