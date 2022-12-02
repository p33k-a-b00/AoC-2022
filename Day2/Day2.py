import numpy as np
array = []
elfs = []

with open('input.txt') as f:   
    for line in f:
        if line.strip():
            array.append(line.strip())
       
elf = {"A":"Rock",
       "B":"Paper",
       "C":"Scissors"
    }
self = {"X":"Rock",
       "Y":"Paper",
       "Z":"Scissors"
    }

score = 0

for round in array:
    if elf[round[0]] == "Rock":
        if self[round[2]] == "Rock":
            score += 4
        if self[round[2]] == "Paper":
            score += 8
        if self[round[2]] == "Scissors":
            score += 3
    if elf[round[0]] == "Paper":
        if self[round[2]] == "Rock":
            score += 1
        if self[round[2]] == "Paper":
            score += 5
        if self[round[2]] == "Scissors":
            score += 9
    if elf[round[0]] == "Scissors":
        if self[round[2]] == "Rock":
            score += 7
        if self[round[2]] == "Paper":
            score += 2
        if self[round[2]] == "Scissors":
            score += 6

print(score)
score = 0    
self = {"X":"Lose",
       "Y":"Draw",
       "Z":"Win"
    }
for round in array:
    if elf[round[0]] == "Rock":
        if self[round[2]] == "Win":
            score += 8
        if self[round[2]] == "Lose":
            score += 3
        if self[round[2]] == "Draw":
            score += 4
            print(score)
    if elf[round[0]] == "Paper":
        if self[round[2]] == "Win":
            score += 9
        if self[round[2]] == "Lose":
            score += 1
            print(score)
        if self[round[2]] == "Draw":
            score += 5
    if elf[round[0]] == "Scissors":
        if self[round[2]] == "Win":
            score += 7
            print(score)
        if self[round[2]] == "Lose":
            score += 2
        if self[round[2]] == "Draw":
            score += 6

print(score)