def puzzle(numheads,numlegs):
    chickens = 0
    rabbits = numheads - chickens
    while 2*chickens + 4*rabbits != numlegs:
        chickens+=1
        rabbits = numheads - chickens
    return chickens, rabbits

numheads = int(input())
numlegs = int(input())
print(puzzle(numheads,numlegs))
