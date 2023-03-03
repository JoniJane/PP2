def even_numbers():
    x = int(input())
    for i in range(0, x+1):
        if i==x and i%2==0:
            yield i
        elif i%2==0:
            yield i
            yield ','
        
print(*even_numbers())