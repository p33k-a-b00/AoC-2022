from collections import Counter
stacks = []
moves = []
answer = ""

stacks.append("QWPSZRHD")
stacks.append("VBRWQHF")
stacks.append("CVSH")
stacks.append("HFG")
stacks.append("PGJBZ")
stacks.append("QTJHWFL")
stacks.append("ZTWDLVJN")
stacks.append("DTZCJGHF")
stacks.append("WPVMBH")
print(stacks)

m = False
with open('input.txt') as f:   
    for line in f:
        if m == True:
            moves.append(line.strip().replace("move ", "").replace("from ", "").replace("to ", "").split(" "))
        if line == "\n":
            m = True
print(moves)       

for move in moves:
    ##part1
    #stacks[int(move[2])-1] += str(stacks[int(move[1])-1][-int(move[0]):][::-1])
    ##part2
    stacks[int(move[2])-1] += str(stacks[int(move[1])-1][-int(move[0]):])
    stacks[int(move[1])-1] = stacks[int(move[1])-1][:-int(move[0])]

for stack in stacks:
    answer += stack[-1:]

print(answer) 
        