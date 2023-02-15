def uniq(l):
    u = []
    for i in l: 
        if i not in u:
            u.append(i)
    return u
print(uniq((input()).split()))