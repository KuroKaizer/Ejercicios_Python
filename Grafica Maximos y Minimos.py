import matplotlib.pyplot as plt
import numpy as np

#Creamos una figura para graficar
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#Centramos sus posiciones
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

#Generamos 100 valores intermedios en -5 y 5
x = np.linspace(-5, 5, 100)

#Genera valores para y = sin(x)
y = np.sin(x)
plt.plot(x, y, 'b', label='y = sin(x)')

#Genera valores para y = cos(x)
y = np.cos(x)
plt.plot(x, y, 'c', label='y = cos(x)')

#Para agregar titulo y leyenda
plt.title("Maximos y Minimos de una Funcion")
plt.legend()
plt.show()
