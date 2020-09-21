import matplotlib.pyplot as plt

x = [1, 3]
y = [4, 4]
plt.plot(x, y)

#plt.show()
x = [1, 3]
y = [4, 6]
plt.plot(x, y)

#plt.show()

y = [4, 6]
plt.title("My first Graph with Matplotlib")
tituloX = "Eje X"
tituloY = "Eje Y"

plt.xlabel(tituloX)

plt.ylabel(tituloY)
x = [1, 3, 2, 5]
y = [4, 6, 6, 5]
x1 = [2, 1, 3, 4]
y2 = [5,4,8, 3]


plt.bar(x,y)
plt.bar(x1, y2)

plt.show()
