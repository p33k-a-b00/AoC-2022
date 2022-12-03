prio = {chr(i+96):i for i in range(1,27)}
prio2 = {chr(i+38):i for i in range(27,53)}
priority = {**prio,**prio2}
print(priority)
array = []
answer = 0

with open('input.txt') as f:   
    for line in f:
        if line.strip():
            array.append(line.strip())
       
print(array)

for bag in array:
    comp1 = bag[:int((len(bag)/2))]
    comp2 = bag[int((len(bag)/2)):]
    for c in comp1:
        if comp2.find(c) != -1:
            answer += priority[c]
            break
print(answer)

answer = 0

for i in range(0, len(array), 3):
    for c in array[i]:
        if array[i+1].find(c) != -1:
            if array[i+2].find(c) != -1:
                answer += priority[c]
                break
print(answer)