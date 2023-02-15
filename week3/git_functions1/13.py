from random import randint as r
myNumb = r(1,20) 

print('Hello! What is your name?')
name = input()
print(f'Well, {name}, I am thinking of a number between 1 and 20. \nTake a guess.')
yourNumb = int(input())

cnt = 0
while yourNumb!=myNumb:
    cnt+=1
    if myNumb>yourNumb:
        print('Your guess is too high.\nTake a guess.')
        yourNumb = int(input())
    else:
        print('Your guess is too low.\nTake a guess.')
        yourNumb = int(input())
else:
    cnt+=1
    print(f'Good job, {name}! You guessed my number in {cnt} guesses!')