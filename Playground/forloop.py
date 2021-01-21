
"""
for i in range(0,10):  #First number is inclusive and second number is not inclusive
    print(i)

for i in range(0,10,2):  #Step 2
    print(i)

for i in range(10,0,-2):  #Negative Step 2
    print(i)

ll= [1,2,3,4,5]

for item in ll:
    print(item)



num = int(input("Enter number"))

for i in range(num):
    for j in range(num):
        print("# ", end='') #This will print in the same line
    print()
"""
num = int(input("Enter number"))
for i in range(num):
    print(" " * (num-i), end='')
    print('#' * (i+1))
    
x = int(input("Please enter a number"))
for j in range(1,x):
    print(" " *(x-j) + "#"*j)