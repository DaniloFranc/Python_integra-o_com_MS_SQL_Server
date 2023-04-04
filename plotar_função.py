import math
import matplotlib.pyplot as plt

x_values = []
y_values = []

for i in range(0, 360):
    x = round((3*math.cos(math.radians(i)) + 3*math.cos(math.radians(i))**2), 6)
    y = round((3*math.sin(math.radians(i)) + 3*math.cos(math.radians(i))*math.sin(math.radians(i))), 6)
    x_values.append(x)
    y_values.append(y)

plt.plot(x_values, y_values)
plt.title("Cardioid Function")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()