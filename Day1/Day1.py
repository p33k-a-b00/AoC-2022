
import numpy as np
array = []
elfs = []

with open('input.txt') as f:   
    for line in f:
        if line.strip():
            array.append(int(line.strip()))
        else:
            elfs.append(array)
            array = []
    elfs.append(array)        

array = []
for elf in elfs:
    array.append(sum(elf))
array.sort()
print(array[-1])
print(sum(array[-3:]))
