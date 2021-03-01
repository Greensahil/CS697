
#printing in matrix form
fileName = "facebook_data.txt"

def printInMatrixForm(listOfList):
    for row in listOfList:
        print (row)

def numberOfSimilarityInTheSameIndex(list1, list2):
    sum = 0
    for i in range(len(list1)):
        if(list1[i] == 1 and list1[i] == 1):
            if list1[i] == list2[i]:
                sum += 1 
    return sum

def returnIndexWithHighestValue(list1):
    max = 0
    index = -1
    for i in range(len(list1)):
        if(list1[i] > max):
            index = i
            max = list1[i]
    return index


lengthOfSocialNetwork = 0
with open(fileName) as f:
    lengthOfSocialNetwork = int(f.readline())



#Initialize a matrix where no one is friend with anyone

matrixOfFriends = [[0 for j in range(lengthOfSocialNetwork)] for i in range(lengthOfSocialNetwork)]

#printInMatrixForm(mat)



#Initialize a matrix where no one is friend with anyone
countMatrix = [[0 for j in range(lengthOfSocialNetwork)] for i in range(lengthOfSocialNetwork)]

#Read the file
with open(fileName, 'r') as reader:
    for line in reader:
        if ' ' in line:
            matrixOfFriends[int(line.split( )[0])][int(line.split( )[1])] = 1
            matrixOfFriends[int(line.split( )[1])][int(line.split( )[0])] = 1
            #print(int(line.split( )[1]))




for i in range(len(matrixOfFriends)):
    for j in range(len(matrixOfFriends[i])):
        if(i !=j and matrixOfFriends[i][j] != 1):
            countMatrix[i][j] = numberOfSimilarityInTheSameIndex(matrixOfFriends[i], matrixOfFriends[j])


while(True):
    id = input("Enter user id in the range 0 to " + str(lengthOfSocialNetwork-1) + " (-1 to quit) : ")

    if(int(id) != -1 and id.isdigit() == False):
        print("Error: Invalid Input")
        break
    if(int(id) > lengthOfSocialNetwork-1):
        print("Error: input must be an int between 0 and ", lengthOfSocialNetwork-1)
        break
    if(int(id) == -1):
        break
    else:
        print("The suggested friend for " + id,  "is " , returnIndexWithHighestValue(countMatrix[int(id)]))


print("Goodbye!")