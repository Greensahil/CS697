#Matrix with rows and columns visually
import random

#2 columns and 5 rows
mat = [random.randint(0,100) for i in range(2) for j in range(5)]

print(mat)
#len(mat[0])   -- length of column

for row in mat:
    print(row)


#for i in range(len(mat[0])):
 #   colsum = 0
 #   for j in range(len(mat[j])):
  #     colsum += mat[j][i]
     
    



def raggedToSquare(raggedList):
    #r = len(raggedList)
    #for row in raggedlist:
     #   print(row)

    #rows
    maxLengthOfColumn = 0
    largest = max([max(row) for row in mat])
    smallest = min([min(row) for row in mat])
    maxcolumns = max([len(row) for row in mat])
    print(largest,smallest)

    for row in mat:
        row.extend([random.randint(smallest,largest) for i in range(maxcolumns - len(row))])
    return mat

raggedlist = [[1,2,3], [4,5],[7]]
mat = raggedToSquare(raggedlist)


for row in mat:
    print(row)


    #for (row in raggedList):
     #   if(len(item) > maxLengthOfColumn):
      #      maxLengthOfColumn = len(item)

       # if(largestValue < max(row)):
        #    largestValue = max(row)    



    #for(i in range(len(raggedList))):

     #   currentitem = raggedList[i]

      #  if(len(currentitem) < maxLengthOfColumn):
       #     numberOfitemsToPush = maxLengthOfColumn - len(currentitem)
        #    raggedList[i].append(random.randint(0,10) * numberOfitemsToPush)

    

         




