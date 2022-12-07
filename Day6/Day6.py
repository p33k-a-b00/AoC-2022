with open('input.txt') as f:   
    for line in f:
        if line.strip():
            datastream = line.strip()
       
print(datastream)
counter = 0
marker = ""

for c in datastream:
    marker += c
    counter += 1
    if len(marker) == 14:
        if len("".join(set(marker))) == 14:
            print(counter)
            break
        marker = marker[1:]
    