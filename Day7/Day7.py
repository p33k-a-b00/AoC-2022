class Directory:
    def __init__(self, name):
        self.name = name
        self.size = 0 
        self.files = []
        self.directories = {}
    
    def printFiles(self):
        for file in self.files:
            print(file.name + " " + file.size)

    def returnFolderSizes(self):
        foldersize = 0
        for file in self.files:
            foldersize += int(file.size)
        return foldersize
    
    def printStructure(self):
        print(self.name + " " + str(self.size))
        self.printFiles()
        for dir in self.directories:
            print(self.directories[dir].name + " " + str(self.directories[dir].size))
            self.directories[dir].printFiles()
            self.directories[dir].printStructure()

    def printAnswerOne(self):
        answer = 0
        for dir in self.directories:
            if self.directories[dir].size <= 100000:
                answer += self.directories[dir].size
                #print(self.directories[dir].size)
        print(answer)
    
    def printAnswerTwo(self):
        unused = 70000000
        needed = 0
        potential = []
        answer = 0
        unused -= self.returnFolderSizes()
        for dir in self.directories:
            unused -= self.directories[dir].returnFolderSizes()
        needed = 30000000 - unused
        for dir in self.directories:
            if self.directories[dir].size >= needed:
                potential.append(self.directories[dir].size)
        print(min(potential))

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size 

input = [] 

with open('input.txt') as f:   
    for line in f:
        if line.strip():
            input.append(line.strip())
       
print(input[1:])

cwd = "/"
currentDir = Directory(cwd)

for line in input[1:]:
    #print(cwd)
    if line == "$ cd ..":
        #print(cwd)
        cwd = cwd[:cwd[:-1].rfind("/")] + "/"
    if line[0:5] == "$ cd " and line[5:7] != "..":
        cwd += line[5:] + "/"
    if line[0:4] == "dir ":
        dir = Directory(cwd + line[4:]+ "/")
        #print(cwd + line[4:] + "/")
        currentDir.directories[dir.name] = dir
        #print(currentDir.directories) 
    if line[0].isnumeric():
        file = line.split(" ")
        f = File(file[1],file[0])
        #print(cwd)
        if cwd == "/":
            currentDir.files.append(f)
            currentDir.size += int(file[0])
        else:
            currentDir.directories[cwd].files.append(f)
            parents = cwd
            while parents != "/":
                #print(parents)
                #print(currentDir.directories[parents].size)
                #print(file[0])
                currentDir.directories[parents].size += int(file[0])
                parents = parents[:parents[:-1].rfind("/")] + "/"
            


#currentDir.printFiles()
#currentDir.printStructure()
#currentDir.printAnswerOne()
currentDir.printAnswerTwo()