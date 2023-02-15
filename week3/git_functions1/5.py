from itertools import permutations as p

def permut(s):
    for i in list(p(s)):
        print(''.join(i))

permut(input())