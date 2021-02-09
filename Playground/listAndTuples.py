#sequence an object that contains multiple items of data
#list is mutable can be changed in place in memory 
#tuple cannot be modified unless you are reassigining to a different place in memory

list = [1,2]

print(list)

#list is similar to array list in java
#list is dynamic and we can change the size

#list can be herttogenous
list = [1,2, 'some string', 1.34343]
print(list)

for item in range(len(list)):
    print(list[item])

print(len(list))


list2 = ['asdas','asdas']
print(list + list2)
print(list.extend(list2)) #same thing

l1 = [1,2]
print(l1*5) #[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]


for item in list:
    print(item)


print(list[-1]) #last element in the list


#since list are mutable 

list[1] = 5

#list slicing

#start index is inclusive and lst idex is not. Last one is step if -ve it starts from the right
l1[1:] #print everything from start to end of the list

print(l1[0:5:2])

#check to see if a list contains something
print(0 in l1)

#add to the end of the list
l1.append(9)




print(l1.index(9))

#insert at any point in the list
l1.insert(1,4)
l1.sort()

#Remove by value and not index
l1.remove(4)

#By index and it also returns the value that was removeed
print(l1.pop(1))

print(l1)


#list are mutable so to copy youcannot do
#l2 = l1

#method 1
#l2 =[]
#l2 = l2 + l1

#method 2
#l2=l1[::]

#method 3
#you can create a loop to copy each element

#to copy list from l1.extend() l1.append() will not work

#to square each item and create in a different 
# newList = [len(item) for item in list1]

# newList = [item for item in list1 if item < 10 ] 

#l2 = [item for item in range(1001) if 3 in str(item)]

#l2 = [item for item in years if year % 4 ==0 and year % 100! = 0]

print("Random numbers")
import random

#Both starts and stop are both inclusive
print(random.randint(0,100))

#More customixation with step. All even numbers
print(random.randint(0,100))

for i in range(10):
    print(random.randint(0,10))


rlist = [random.randint(0,10) for i in range(10)]
slist = random.sample(range(0,100),10) #unique number
print(rlist)