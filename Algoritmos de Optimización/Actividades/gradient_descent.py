import numpy as np
import matplotlib.pyplot as plt
import decimal
import random
import math

# Funcion f(x)
f_x = lambda x: (3*(x[0]**4)) + (4*(x[0]**3)) - (12*(x[0]**2)) + 7
# Gradiente de la funcion f(x)
f_gradiente = lambda x: (12*(x[0]**3)) + (12*(x[0]**2)) - (24*x[0])

# Iniciamos variables donde guardaremos los valores de x, y 
resolucion = 100
rango = 2.5
x = np.linspace(-rango, rango, resolucion)
y = np.zeros(resolucion)

# Calculo f(x)
for ix, i in enumerate(x):
    y[ix] = f_x([i])

# Graficar f(x)
plt.plot(x, y)

# Tomamos un punto aleatorio de la funcion f(x) para empezar el descenso del gradiente
random_number = int(random.uniform(0, len(x)-1))
P = np.array([x[random_number], y[random_number]])
# Dibujamos en la grafica nuestro punto aleatorio
plt.plot(P[0], P[1], "o", c="black")

# Taza de aprendizaje que será multiplicada por el gradiente de la funcion f(x)
taza_aprendizaje = .001

# Descenso del gradiente
for _ in range(500):
  x_anterior = P
  P[1] = f_x(x_anterior)
  P[0] -= np.dot(taza_aprendizaje, f_gradiente(x_anterior))
  plt.plot(P[0], P[1], "o", c="red")

plt.plot(P[0], P[1], "o", c="green")
plt.show()