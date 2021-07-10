import math
import operator
import numpy as np


# tomas = [
#     [1,1,1,1,1,0,0,0,0,0],
#     [0,0,1,1,1,0,0,0,0,0],
#     [0,1,0,0,1,0,1,0,0,0],
#     [1,1,0,0,0,0,1,1,0,0],
#     [0,1,0,1,0,0,0,1,0,0],
#     [1,1,0,1,1,0,0,0,0,0],
#     [1,1,0,1,1,0,0,0,0,0],
#     [1,1,0,0,0,1,0,0,0,0],
#     [1,1,0,1,0,0,0,0,0,0],
#     [1,1,0,0,0,1,0,0,1,0],
#     [1,1,1,0,1,0,0,1,0,0],
#     [1,1,1,1,0,1,0,0,0,0],
#     [1,0,0,1,1,0,0,0,0,0],
#     [1,0,1,0,0,1,0,0,0,0],
#     [1,1,0,0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0,0,0,1],
#     [1,0,1,0,0,0,0,0,0,0],
#     [0,0,1,0,0,1,0,0,0,0],
#     [1,0,1,0,0,0,0,0,0,0],
#     [1,0,1,1,1,0,0,0,0,0],
#     [0,0,0,0,0,1,0,1,0,0],
#     [1,1,1,1,0,0,0,0,0,0],
#     [1,0,1,0,0,0,0,0,0,0],
#     [0,0,1,0,0,1,0,0,0,0],
#     [1,1,0,1,0,0,0,0,0,1],
#     [1,0,1,0,1,0,0,0,1,0],
#     [0,0,0,1,1,0,0,0,0,0],
#     [1,0,0,1,0,0,0,0,0,0],
#     [1,0,0,0,1,1,0,0,0,0],
#     [1,0,0,1,0,0,0,0,0,0]
# ]

tomas = [
[1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
 [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
 [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
 [1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
 [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0],
 [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0]
]

def get_tomas_parecidas(tomas_decimal, toma_objetivo, tomas):
    tomas_por_parecido = {}
    parecidos = []
    for i in range(toma_objetivo[0]):
        tomas_por_parecido[i] = []
        if i not in parecidos:
            parecidos.append(i)

    for i in range(len(tomas_decimal)):
        temp = tomas[toma_objetivo[2]] | tomas[tomas_decimal[i][2]]
        parecido = abs(len(tomas[toma_objetivo[2]][tomas[toma_objetivo[2]] == 1]) - len(temp[temp == 1]))
        tomas_por_parecido[parecido].append([tomas_decimal[i][2], i])

    return tomas_por_parecido, parecidos

# Primero obtener las tomas o toma con mayor numero de actores
tomas_decimal = []
tomas = np.array(tomas)

for i in range(len(tomas)):
    my_string = ''.join(map(str, tomas[i]))
    tomas_decimal.append([len(tomas[i][tomas[i] == 1]), int(my_string, 2), i])
    tomas_decimal = sorted(tomas_decimal, key=operator.itemgetter(0, 1), reverse=True)

solucion_final = {}
# Segundo paso, obtener las tomas mas parecidas para cada toma con el mayor numero de actores
maximo_tomas = 6
index_delete = []
optimo = math.ceil(len(tomas) / maximo_tomas)
costo_total = 0
dia = 0

for i in range(optimo):
    solucion_final[i] = []

while len(tomas_decimal) > 0:
    index_delete = []
    toma_solucion = tomas_decimal[0]
    solucion_parcial, llaves = get_tomas_parecidas(tomas_decimal, toma_solucion, tomas)
    index = 0
    actores = set()
    for i in range(maximo_tomas):
        while len(solucion_parcial[index]) == 0:
            index += 1

        j = solucion_parcial[index].pop(0)
        index_delete.append(j[1])
        solucion_final[dia].append(j[0])

        for i in range(len(tomas[j[0]])):
            if tomas[j[0]][i] == 1:
                actores.add(i+1)

        if index == llaves[-1]:
            break

    tomas_decimal = np.delete(tomas_decimal, tuple(index_delete), axis=0)
    costo_total += len(actores)
    print(solucion_final[dia])
    print(len(actores))
    dia += 1

print(f'El costo total sera: {costo_total}')