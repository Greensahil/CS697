

# listOfWords = []




# inp = input("Enter a Word")

# listOfWords = inp.split(" ")

# dictOfWords = {'q':1,'w':1,'e':1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1, 'p':1, 'a':2,'s':2,'d':2,
#                 'f':2,'g':2,'h':2,'j':2,'k':2,'l':2,'z':3,'x':3,'c':3,'v':3,'b':3, 'n':3,'m':3}


# def isTypeable(inp):
#     currentVal = 0
#     for key in dictOfWords:
#         if(key in inp):
#             if(currentVal == 0):
#                 currentVal = dictOfWords[key]
#             else:
#                 if(currentVal != dictOfWords[key]):
#                     return False
#     return True
        
# outputList = []
# for item in listOfWords:
#     if(isTypeable(item)):
#         outputList.append(item)


# outputStr = ""

# for item in outputList:
#     outputStr = outputStr + " " + item

# print(outputStr)

import matplotlib.pyplot as plt

x = [1,2,3]
y=[1,1,1]
plt.plot(x,y)

plt.xlabel('asdas')
plt.ylabel('adas')

plt.show()

l1 = [1,4,5,6]
labels = ['asda','asdsa','asdas','ads']
plt.pie(l1,labels=labels)


labels = ['asda','asdsa','asdas','ads']

plt.show()
