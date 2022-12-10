import numpy as np

def parseInput():
    output = []
    with open('input.txt') as f:   
        for line in f:
            output.append(line.strip())
    return output

def fillForest():
    grid = parseInput()
    length = len(grid[0])
    grids = np.zeros( (len(grid), length))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grids[i][j] = grid[i][j]
    grids[len(grid)-1][length-1] = grid[len(grid)-1][length-1]
    return(grids)

def findVisble(grid):
    height = int(grid.shape[0])
    length = int(grid.shape[1])
    
    visGrid =np.zeros((height, length))

    #Left -> Right
    for y in range(1,height-1):
        tallest = 0
        for x in range(1,length-1):
            if tallest < grid[y][x-1]:
                tallest = grid[y][x-1]
            if grid[y][x-1] < grid[y][x]:
                if tallest < grid[y][x]:
                    visGrid[y][x] += 1
                    tallest = grid[y][x]
    #Right -> Left
    for y in range(1,height-1)[::-1]:
        tallest = 0
        for x in range(1,length-1)[::-1]:
                if tallest < grid[y][x+1]:
                    tallest = grid[y][x+1]
                if grid[y][x+1] < grid[y][x]:
                    if tallest < grid[y][x]:
                        visGrid[y][x] += 1
                        tallest = grid[y][x]
    #Top -> Bottom
    for x in range(1,length-1):
        tallest = 0
        for y in range(1,height-1):
            if tallest < grid[y-1][x]:
                tallest = grid[y-1][x]
            if grid[y-1][x] < grid[y][x]:
                if tallest < grid[y][x]:
                    visGrid[y][x] += 1
                    tallest = grid[y][x]
    #Bottom -> Top
    for x in range(1,length-1)[::-1]:
        tallest = 0
        for y in range(1,height-1)[::-1]:
            if tallest < grid[y+1][x]:
                tallest = grid[y+1][x]
            if grid[y+1][x] < grid[y][x]:
                if tallest < grid[y][x]:
                    visGrid[y][x] += 1
                    tallest = grid[y][x]
    print(visGrid)                 
    print(len(np.nonzero(visGrid)[0]))
    print(int((grid.shape[0])*2)+(int(grid.shape[1])*2)-4)
    return(len(np.nonzero(visGrid)[0])+int((grid.shape[0])*2)+(int(grid.shape[1])*2)-4)            

def findScenicScore(grid,tree):
    height = int(grid.shape[0])
    length = int(grid.shape[1])
    lview = 0 
    rview = 0 
    uview = 0 
    dview = 0 

    for x in range(0,tree[0])[::-1]:
        if grid[tree[1]][tree[0]] <= (grid[tree[1]][x]):
            lview += 1
            break
        else:
            lview += 1
    for x in range(tree[0]+1,length):
        if grid[tree[1]][tree[0]] <= (grid[tree[1]][x]):
            rview += 1
            break
        else:
            rview += 1
    for y in range(0,tree[1])[::-1]:
        if grid[tree[1]][tree[0]] <= (grid[y][tree[0]]):
            uview += 1
            break
        else:
            uview += 1
    for y in range(tree[1]+1,height):
        if grid[tree[1]][tree[0]] <= (grid[y][tree[0]]):
            dview += 1
            break
        else:
            dview += 1

    return lview*rview*uview*dview

def findHightestScore(grid):
    height = int(grid.shape[0])
    length = int(grid.shape[1])
    best = 0

    for x in range(1,length-1):
        for y in range(1,height-1):
            #print("Finding: " + str(x) + "," + str(y))
            score = findScenicScore(grid,[x,y]) 
            #print("Score:" + str(score))
            if best < score:
                best = score
    print(best)



input = parseInput()
grid = fillForest()
edge = int((grid.shape[0])*2)+(int(grid.shape[1])*2)-4

#answerOne = findVisble(grid)
#print(answerOne)
#print(findScenicScore(grid, [2,3]))
findHightestScore(grid)
