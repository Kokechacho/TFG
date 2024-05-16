import matplotlib.pyplot as plt
import time
import numpy as np
import re

def tiempo_ejecucion(f, lista,n):
    tiempo_total = 0
    for i in range(n):
        inicio = time.time()
        resultado = f(lista)
        fin = time.time()
        tiempo_total += fin - inicio
    print("Tiempo de ejecución:", tiempo_total, "segundos")
    return tiempo_total/n


def par(l):
    for i in range(0,len(l)//2,2):
        pos_simetrica = (len(l) - 1) - i
        l[i], l[pos_simetrica] = l[pos_simetrica], l[i]
    return l

def noRepetitions(l):
    combinaciones = []
    for i in range(len(l)):
    	for j in range(i + 1, len(l)):
            combinaciones.append([l[i], l[j]])
    return combinaciones

def es_direccion_valida(correo):
    return bool(re.match(r'^[^@]+@[^@]+\.[^@]+$', correo))

def obtener_direcciones_validas(tabla):
    direcciones_validas = []
    for fila in tabla:
        for celda in fila:
            if es_direccion_valida(celda):
                direcciones_validas.append(celda)
    return direcciones_validas

tiempo_1 = []
tiempo_1q = [0,0,0,0,0.0003,0.0057,0.0685,0.6456]
for i in range(1,9):
    l = list(range((10**i)+1))
    tiempo_1.append(tiempo_ejecucion(par, l, 10))

x = np.linspace(10,10**8,8)
mejoras = [0, 0, 0, 0, 0.8750096, 0.7594908, 0.71454, 0.7358058]

fig, ax = plt.subplots()
ax.plot(x, tiempo_1, marker='o', label='Tiempo de ejecución Python')
ax.plot(x, tiempo_1q, marker='s', label='Tiempo de ejecución Q')

# Configurar los ejes
ax.set_xlabel('Número de elementos')
ax.set_ylabel('Tiempo de ejecución (s)')
ax.set_title('Eficiencia de ejecución Python-Q')

# Añadir la leyenda
ax.legend()

fig, ax2 = plt.subplots()
ax2.plot(x, mejoras, marker='o', label='Mejora relativa Python-Q')

# Configurar los ejes
ax2.set_xlabel('Número de elementos')
ax2.set_ylabel('% de mejora')
ax2.set_title('Mejora de tiempo de ejecución Python-Q')

# Añadir la leyenda
ax2.legend()

plt.show()

tiempo_2 = []
tiempo_2q = [0,0.0004,0.0357,3.4415,55.0]
for i in range(1,5):
    l = list(range((10**i)+1))
    tiempo_2.append(tiempo_ejecucion(noRepetitions, l, 10))

tiempo_2.append(10900)
x = np.linspace(10,10**5,5)
mejoras = [0, 0.92, 0.8097015, 0.7941563, 0.9949541]

fig, ax = plt.subplots()
ax.plot(x, tiempo_2, marker='o', label='Tiempo de ejecución Python')
ax.plot(x, tiempo_2q, marker='s', label='Tiempo de ejecución Q')

# Configurar los ejes
ax.set_xlabel('Número de elementos')
ax.set_ylabel('Tiempo de ejecución (s)')
ax.set_title('Eficiencia de ejecución Python-Q')

# Añadir la leyenda
ax.legend()

fig, ax2 = plt.subplots()
ax2.plot(x, mejoras, marker='o', label='Mejora relativa Python-Q')

# Configurar los ejes
ax2.set_xlabel('Número de elementos')
ax2.set_ylabel('% de mejora')
ax2.set_title('Mejora de tiempo de ejecución Python-Q')

# Añadir la leyenda
ax2.legend()

plt.show()

tabla = [
        ['usuario1@dominio.com', '@dominio.com', 'invalido'],
        ['usuario3@dominio.com', 'usu.ario4@dominio', 'usu@dominio.com'],
        ['usuari.o6@dominio.com', 'usuario@7@dominio.com', 'invalido']
    ]

nueva_tabla = []

tiempo_3 = []
tiempo_3q = [0,0,0,0.0016,0.0158,0.1590,1.5885,15.7641]
for i in range(1,8):
    while len(nueva_tabla) < (10**i):
        nueva_tabla.extend(tabla)

    nueva_tabla = nueva_tabla[:10**i]
    tiempo_3.append(tiempo_ejecucion(obtener_direcciones_validas, nueva_tabla,11))

tiempo_3.append(2050)
x = np.linspace(10,10**5,8)
mejoras = [0, 0, 0, 0.9288238, 0.9243996, 0.9228923, 0.9227399, 0.999231]

fig, ax= plt.subplots()
ax.plot(x, tiempo_3, marker='o', label='Tiempo de ejecución Python')
ax.plot(x, tiempo_3q, marker='s', label='Tiempo de ejecución Q')

# Configurar los ejes
ax.set_xlabel('Número de elementos')
ax.set_ylabel('Tiempo de ejecución (s)')
ax.set_title('Eficiencia de ejecución Python-Q')

# Añadir la leyenda
ax.legend()

fig, ax2 = plt.subplots()
ax2.plot(x, mejoras, marker='o', label='Mejora relativa Python-Q')

# Configurar los ejes
ax2.set_xlabel('Número de elementos')
ax2.set_ylabel('% de mejora')
ax2.set_title('Mejora de tiempo de ejecución Python-Q')

# Añadir la leyenda
ax2.legend()

plt.show()