s = str(input())
t = len(s)//2 + len(s)%2
print(s[t:]+ s[:t])