import numpy as np

def parseInput():
    output = []
    height = 0
    width = 0

    with open('input.txt') as f:   
        for line in f:
            line = line.strip().split()
            if line[0] == 'L' or line[0] == 'R':
                if width < int(line[1]):
                    width = int(line[1])
            else:
                if height < int(line[1]):
                    height = int(line[1])
            output.append(line)
    return [output,height+1,width+1]

input = parseInput()

grids = np.zeros((input[1], input[2]))
print(grids)
