
"""
    This is a block comment this can be started with a triple double quotes
"""

#You can write comments in python using a hash

#say = input("Enter your greeting") #this is an inline comment which is not used that much
#print(say)

x = 5
print(x)

print(type(x)) #<class 'int'>

x=0.5
print(type(x))

y = 2

z = x * y

print(z)


#Multiple assignments and multiple printing
x,y = 5, 10

print(x,y)

#swap number
x,y = 5, 10

z = x
x = y
y = z

print(x)
print(y)

#5/2 = 2.5
#5//2 = 2   -- This traucates but does not round off, the largest integer that is less than taht number
#5**2 = 25

print('it\'s a nice day')

print(0<=x<=100)