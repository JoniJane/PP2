def even_numbers():
    x = int(input())
    for i in range(0, x+1,):
        if i%4==0 or i%3==0:
            yield i
        
print(*even_numbers())