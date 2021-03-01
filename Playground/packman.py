fileName = "init_grid.txt"
glbPackManFace = ""
S = True

def printInMatrixForm(listOfList):
    print("Grid Looks Like:")
    for row in listOfList:
        print ('  '.join(map(str, row)))

def placeItemsInTheGrid(posX, posY, item):
    grid[posX][posY] = item

def returnglbPackManFaceBasedOnDirection(direction):
    if direction =="S"  or (direction == "L" and glbPackManFace == "<") or (direction == "L" and glbPackManFace == ">"):
        return "V"
    elif direction =="N" or (direction == "R" and glbPackManFace == ">") or (direction == "R" and glbPackManFace == "<"):
        return "^"
    elif (direction == "R" and glbPackManFace == "V") :
        return "<"
    elif  direction =="E"  or ( direction == "R"):
        return ">"
    elif direction =="W"  or (direction == "L"):
        return "<"
#Read the file to get the number of rows and column
lines = ""
with open(fileName) as f:
    lines = f.readlines()

firstLine = lines[0]
numberOfRows = int(firstLine.split( )[0])
numberOfColumns = int(firstLine.split( )[1])



#setup and print grid
grid = [["." for j in range(numberOfColumns)] for i in range(numberOfRows)]


#place pacman
secondLine = lines[1]
packManPosX = int(secondLine.split( )[0])
packManPosY = int(secondLine.split( )[1])


#packman face
thirdLine = lines[2].replace(" ", "")
thirdLine = "".join(thirdLine.split())
glbPackManFace = returnglbPackManFaceBasedOnDirection(str(thirdLine))

glbCurrentPackManPosition = [packManPosX,packManPosY]
placeItemsInTheGrid(packManPosX,packManPosY,glbPackManFace)



numberOfObstacles = int(lines[3].split( )[0])




for i in range(len(lines)):
    if(i>3 and i <= numberOfObstacles+3):
        currentLine = lines[i]
        placeItemsInTheGrid(int(currentLine.split( )[0]),int(currentLine.split( )[1]), "x")
        

numberOfItemsOnTheGrid = int(lines[4+numberOfObstacles].split( )[0])

for i in range(len(lines)):
    if(i > 4 + numberOfObstacles):
        currentLine = lines[i]
        placeItemsInTheGrid(int(currentLine.split( )[0]),int(currentLine.split( )[1]), "o")




print("-----Welcome to Pacman-----")
print("     L:   Turn Left ")
print("     R:   Turn Right ")
print("     [x]:   Move x number of steps ")
print("     C:   Consume Item ")
print("     P:   Place Item ")
print("     S:   Show/Hide Path ")
print("     Q:   Quit ")


printInMatrixForm(grid)

while(True):
    inp = input("Enter Input")

    if(inp == "W"):
        break
    elif(inp == "S"):
        S = not S
    elif(inp == "L"):
        glbPackManFace = returnglbPackManFaceBasedOnDirection("L")
        if(grid[glbCurrentPackManPosition[0]][glbCurrentPackManPosition[1]] == "@"):
            placeItemsInTheGrid(glbCurrentPackManPosition[0],glbCurrentPackManPosition[1],"@")
        else:
            placeItemsInTheGrid(glbCurrentPackManPosition[0],glbCurrentPackManPosition[1],glbPackManFace)        
    elif(inp == "R"):
        glbPackManFace = returnglbPackManFaceBasedOnDirection("R")
        placeItemsInTheGrid(glbCurrentPackManPosition[0],glbCurrentPackManPosition[1],glbPackManFace)
    elif(inp == "P"):
        placeItemsInTheGrid(glbCurrentPackManPosition[0],glbCurrentPackManPosition[1],"@")
    elif(inp.isdigit() == True):
        if(glbPackManFace == "<"):
            blnObstace = False
            blnOffGrid = False
            tempGlbCurrentPackManPosition = glbCurrentPackManPosition
            for item in range(int(inp)):
                if(tempGlbCurrentPackManPosition[1]-1 < 0):
                    blnOffGrid = True
                    print("Invalid move. Enter again")
                    continue                
                if(grid[tempGlbCurrentPackManPosition[0]][tempGlbCurrentPackManPosition[1]-1] == "x"):
                    blnObstace = True
                    print("Invalid move. Enter again")
                tempGlbCurrentPackManPosition = [tempGlbCurrentPackManPosition[0],tempGlbCurrentPackManPosition[1]-1]
            if(not blnObstace and not blnOffGrid):
                for item in range(int(inp)):                
                        if(grid[glbCurrentPackManPosition[0]][glbCurrentPackManPosition[1]-1] != "x"):
                            if(grid[glbCurrentPackManPosition[0]][glbCurrentPackManPosition[1]] == "@"):
                                 placeItemsInTheGrid(glbCurrentPackManPosition[0],glbCurrentPackManPosition[1],"o")
                            else:
                                placeItemsInTheGrid(glbCurrentPackManPosition[0],glbCurrentPackManPosition[1]," " if S else ".")
                            placeItemsInTheGrid(glbCurrentPackManPosition[0],glbCurrentPackManPosition[1]-1,glbPackManFace)
                            glbCurrentPackManPosition = [glbCurrentPackManPosition[0],glbCurrentPackManPosition[1]-1]
        elif(glbPackManFace == ">"):
            blnObstace = False
            blnOffGrid = False
            tempGlbCurrentPackManPosition = glbCurrentPackManPosition
            for item in range(int(inp)):
                if(tempGlbCurrentPackManPosition[1]+1 > len(grid[0])-1):
                    blnOffGrid = True
                    print("Invalid move. Enter again")
                    continue                
                if(grid[tempGlbCurrentPackManPosition[0]][tempGlbCurrentPackManPosition[1]+1] == "x"):
                    blnObstace = True
                    print("Invalid move. Enter again")
                tempGlbCurrentPackManPosition = [tempGlbCurrentPackManPosition[0],tempGlbCurrentPackManPosition[1]+1]
            if(not blnObstace and not blnOffGrid):
                for item in range(int(inp)):                
                        if(grid[glbCurrentPackManPosition[0]][glbCurrentPackManPosition[1]+1] != "x"):
                            if(grid[glbCurrentPackManPosition[0]][glbCurrentPackManPosition[1]] == "@"):
                                 placeItemsInTheGrid(glbCurrentPackManPosition[0],glbCurrentPackManPosition[1],"o")
                            else:
                                placeItemsInTheGrid(glbCurrentPackManPosition[0],glbCurrentPackManPosition[1]," " if S else ".")
                            
                            placeItemsInTheGrid(glbCurrentPackManPosition[0],glbCurrentPackManPosition[1]+1,glbPackManFace)
                            glbCurrentPackManPosition = [glbCurrentPackManPosition[0],glbCurrentPackManPosition[1]+1]
        elif(glbPackManFace == "V"):
            blnObstace = False
            blnOffGrid = False
            tempGlbCurrentPackManPosition = glbCurrentPackManPosition
            for item in range(int(inp)):
                if(tempGlbCurrentPackManPosition[0]+1 > len(grid)-1):
                    blnOffGrid = True
                    print("Invalid move. Enter again")
                    continue                
                if(grid[tempGlbCurrentPackManPosition[0]+1][tempGlbCurrentPackManPosition[1]] == "x"):
                    blnObstace = True
                    print("Invalid move. Enter again")
                tempGlbCurrentPackManPosition = [tempGlbCurrentPackManPosition[0]+1,tempGlbCurrentPackManPosition[1]]
            if(not blnObstace and not blnOffGrid):
                for item in range(int(inp)):                
                        if(grid[glbCurrentPackManPosition[0]+1][glbCurrentPackManPosition[1]] != "x"):
                            if(grid[glbCurrentPackManPosition[0]][glbCurrentPackManPosition[1]] == "@"):
                                 placeItemsInTheGrid(glbCurrentPackManPosition[0],glbCurrentPackManPosition[1],"o")
                            else:
                                placeItemsInTheGrid(glbCurrentPackManPosition[0],glbCurrentPackManPosition[1]," " if S else ".")
                            placeItemsInTheGrid(glbCurrentPackManPosition[0]+1,glbCurrentPackManPosition[1],glbPackManFace)
                            glbCurrentPackManPosition = [glbCurrentPackManPosition[0]+1,glbCurrentPackManPosition[1]]
        elif(glbPackManFace == "^"):
            blnObstace = False
            blnOffGrid = False
            tempGlbCurrentPackManPosition = glbCurrentPackManPosition
            for item in range(int(inp)):
                if(tempGlbCurrentPackManPosition[0]-1 < 0):
                    blnOffGrid = True
                    print("Invalid move. Enter again")
                    continue                
                if(grid[tempGlbCurrentPackManPosition[0]-1][tempGlbCurrentPackManPosition[1]] == "x"):
                    blnObstace = True
                    print("Invalid move. Enter again")
                tempGlbCurrentPackManPosition = [tempGlbCurrentPackManPosition[0]-1,tempGlbCurrentPackManPosition[1]]
            if(not blnObstace and not blnOffGrid):
                for item in range(int(inp)):                
                        if(grid[glbCurrentPackManPosition[0]-1][glbCurrentPackManPosition[1]] != "x"):
                            if(grid[glbCurrentPackManPosition[0]][glbCurrentPackManPosition[1]] == "@"):
                                 placeItemsInTheGrid(glbCurrentPackManPosition[0],glbCurrentPackManPosition[1],"o")
                            else:
                                placeItemsInTheGrid(glbCurrentPackManPosition[0],glbCurrentPackManPosition[1]," " if S else ".")
                            placeItemsInTheGrid(glbCurrentPackManPosition[0]-1,glbCurrentPackManPosition[1],glbPackManFace)
                            glbCurrentPackManPosition = [glbCurrentPackManPosition[0]-1,glbCurrentPackManPosition[1]]        
        
    printInMatrixForm(grid)
