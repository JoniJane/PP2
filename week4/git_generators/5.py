def numbers():
    x = int(input())
    for i in range(x, 0-1, -1):
        yield i

print(*numbers())