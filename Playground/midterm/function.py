# def main2():
#     x = 1
#     print("Beofre the call, x is ", x)
#     increment(x)
#     print("After the call , x is", x)

# def increment(x):
#     x+=1
#     print("x inside function is", x)

# main2()


#beofre call x is 1
#inside function x is 2
#after call x is 1

#the value of args is changed into a tuple
# def sum(*args):
#     total = 0
#     for item in args:
#         total = total + item
#     return total

# print(sum(1,2,3,4))

# def sumDict(**kwargs):
#     for item in kwargs:
#         print(item, ":", kwargs[item])   
    

# sumDict(NAME='SAHIL', GPA = '3.6', MAJOR = 'CS')


# def gbTest(x):
#     #global x
#     x = 10
#     print('value of x inside function is', x)

# x =5
# gbTest(x)
# print('value of x outside function is', x)


# sum = 0
# for i in range(5):
#     sum += 1

# print(i)


# print(1,2,3,sep=', ')

# l1= [2,3,1]
# print(l1)






# l1 = [1,2,3]


# def checkGlob():
#     l2 = l1
#     l2.append(10)
#     print(l2)

# checkGlob()
# print(l1)


# x = 2


# def checkGlob():
#     x = 3
#     print(x)

# checkGlob()
# print(x)



# l1 = [25,4,86,34,82,5,82,30,7,93]

# print(l1[-1:-8:-3])

# print(l1[-4:-1:])

# print(l1[-5::])


# L1= [1,2,3,4,5]
# L2 = [5,4,1,7,8]

# L3 = L1[::]


# [L3.append(item) for item in L2 if item not in L1]
# print(L3)

# L1 = [(1,2), (3,4,1), (5,7) ,(11,23,11,1)]
# print(L1)

# L1 = [item for t in L1 for item in t]
# print(L1)

# L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

L = [[1,2,3], [4,5,6], [7,8,9]]

print([item for l in L for item in l if L[1] == l])

party = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert','Ford']


print(7//2)

print([item for item in party if party.index(item) > len(party)/2 and party.index(item) != len(party)-1])
print(party[(len(party)//2)+1:-1])

planets=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']

print([item.upper() + "!" for item in planets if len(item)>6])



coutry_codes = {'Finland':'fi', 'South Afeica':'za', 'Nepal':'np'}

print({value:key for key,value in coutry_codes.items()})

print({value:key for key,value in coutry_codes.items()})
