#Multidimensional array
import numpy as np

A = np.array([1,2,3,4])


print(A)
print(type(A))


A = np.array([1,2,3,4])
B = np.arange(0,110,2)
C = np.zeros(10)


print(A)
print(B)
print(C)


# print([2 for item in range(0,10)])

# print([item for item in [item3 for item3 in range(1,11)] in range(1,10)])


A = np.arange(1,13).reshape(3,4)




A =A[A>5]
A = A[A<10]

print(A)