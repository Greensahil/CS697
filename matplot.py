import matplotlib.pyplot as plt
import math

m = 0.5
c = 4
x = [ i for i in range(100)]
y = [m*i + c for i in x]

#plt.xticks(x,[i for i in range(2010,2020)])

plt.xlabel('Years')
plt.ylabel('price')

plt.plot(x,y)

y = [i**3 for i in x]
plt.plot(x,y)

y = [math.sin(i) for i in x]
plt.plot(x,y)



plt.legend(['exam','work'])

#

plt.show()
