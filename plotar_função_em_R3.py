import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Cria uma grade de valores para x, y e z
u = np.linspace(-1, 1, 100)
v = np.linspace(0, 2*np.pi, 100)
U, V = np.meshgrid(u, v)

# Define a equação do hiperboloide
a = 1
b = 1
c = 1
X = a * np.cosh(U) * np.cos(V)
Y = b * np.cosh(U) * np.sin(V)
Z = c * np.sinh(U)

# Plota o hiperboloide
ax.plot_surface(X, Y, Z,  rstride=1, cstride=1, cmap='viridis')

# Configura os rótulos dos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()