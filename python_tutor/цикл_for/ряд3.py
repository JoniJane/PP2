a = int(input())
b = int(input())
for x in range(a-(a+1)%2 , b+(b+1)%2-1, -2):
        print(x)