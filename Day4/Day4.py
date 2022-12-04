from collections import Counter
array = []
answer1 = 0
answer2 = 0

with open('input.txt') as f:   
    for line in f:
        if line.strip():
            array.append(line.strip().split(','))
       
print(array)

for pair in array:
    section1 = list(range(int(pair[0].split('-')[0]),int(pair[0].split('-')[1])+1))
    section2 = list(range(int(pair[1].split('-')[0]),int(pair[1].split('-')[1])+1))
    c = Counter(section1)

    output = []

    for n in section2:
        if c[n]>0:
            output.append(n)
            c[n]-=1
    if output == section2:
        answer1 += 1
    elif output == section1:
        answer1 += 1

    if len(output) != 0:
        answer2 +=1
    
print(answer1)
print(answer2)