myList = [25, 4, 86 , 34, 82,5,82,30,7,93]

print(myList[-4:-1:1])

print(myList[-5:])

l1 = [1,2,3,4,5]
print("reverse")
print(l1[::-1])

l2 = [5,4,1,7,8]

print([item for item in l1 if item in l2])

L3 =[]

S = "the i am the i am the is he she her xx yy yy"

#print(S.split(" "))
print([L3.append(item) for item in S.split(" ") if item not in L3])
print(L3)