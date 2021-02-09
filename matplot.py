import matplotlib.pyplot as plt

m = 0.5
c = 4
x = [ i for i in range(100)]
y = [m*i + c for i in x]

plt.plot(x,y)

plt.show()
