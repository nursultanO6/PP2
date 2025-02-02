def solve(numheads, numlegs):
    rabbit = (numlegs - 2 * numheads) // 2
    chicken = numheads - rabbit
    print (rabbit)
    print(chicken)
numheads = 35
numlegs = 94
solve(numheads, numlegs)