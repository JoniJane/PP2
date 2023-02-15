def solve(numheads, numlegs):
    r = (numlegs - 2*numheads)//2
    c = numheads - r
    print(r,  "rabbits and", c, "chickens")

solve(int(input()) , int(input()))