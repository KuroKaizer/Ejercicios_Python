import matplotlib.pyplot as plt 
import pandas as pd 
#Cargamos nuestra dataset
df = pd.read_csv('stocks.csv')
#Obtenemos las ventas de cada empresa
appl = df['APPL'].values
ibm = df['IBM'].values
csco = df['CSCO'].values
msft = df['MSFT'].values
#Graficamos las ventas con colores
plt.plot(appl, color='blue', label='APPL')
plt.plot(ibm, color='green', label='IBM')
plt.plot(csco, color='red', label='CSCO')
plt.plot(msft, color='magenta', label='MSFT')
#Agregamos una leyenda para los datos
plt.legend(loc='upper left')
plt.xticks(rotation=60)
#Mostramos la grafica
plt.show()