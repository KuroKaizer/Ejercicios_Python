#Importamos matplotlib y numpy
import matplotlib as plt 
import numpy as np 
#Generamos 100 valores intermedios entre 0 y 2 
x = np.linspace(0, 2, 100)
#Generamos una graficas en base a X con los valores intermedios obtenidos
plt.plot(x, x, label='Lineal')

#Agregamos etiquetas y mostramos la grafica
plt.xlabel('Eje X')
plt.ylabel('Eje Y') 
plt.title("Funciones Matematicas")
plt.legend()
plt.show()