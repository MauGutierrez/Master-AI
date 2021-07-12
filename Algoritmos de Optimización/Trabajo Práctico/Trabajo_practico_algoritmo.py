import math
import operator
import numpy as np


tomas = [
    [1,1,1,1,1,0,0,0,0,0],
    [0,0,1,1,1,0,0,0,0,0],
    [0,1,0,0,1,0,1,0,0,0],
    [1,1,0,0,0,0,1,1,0,0],
    [0,1,0,1,0,0,0,1,0,0],
    [1,1,0,1,1,0,0,0,0,0],
    [1,1,0,1,1,0,0,0,0,0],
    [1,1,0,0,0,1,0,0,0,0],
    [1,1,0,1,0,0,0,0,0,0],
    [1,1,0,0,0,1,0,0,1,0],
    [1,1,1,0,1,0,0,1,0,0],
    [1,1,1,1,0,1,0,0,0,0],
    [1,0,0,1,1,0,0,0,0,0],
    [1,0,1,0,0,1,0,0,0,0],
    [1,1,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,0,1],
    [1,0,1,0,0,0,0,0,0,0],
    [0,0,1,0,0,1,0,0,0,0],
    [1,0,1,0,0,0,0,0,0,0],
    [1,0,1,1,1,0,0,0,0,0],
    [0,0,0,0,0,1,0,1,0,0],
    [1,1,1,1,0,0,0,0,0,0],
    [1,0,1,0,0,0,0,0,0,0],
    [0,0,1,0,0,1,0,0,0,0],
    [1,1,0,1,0,0,0,0,0,1],
    [1,0,1,0,1,0,0,0,1,0],
    [0,0,0,1,1,0,0,0,0,0],
    [1,0,0,1,0,0,0,0,0,0],
    [1,0,0,0,1,1,0,0,0,0],
    [1,0,0,1,0,0,0,0,0,0]
]


def get_tomas_parecidas(tomas_decimal, toma_objetivo, tomas):
    """
    Obtener las tomas parecidas para cada toma objetivo
    
    tomas_decimal:  array que contiene las tomas ordenadas por numero de actores y valor decimal de la toma.
                    [numero de actores en la toma, valor de la toma en decimal, indice en el array tomas original]               

    toma_objetivo:  toma con el mayor numero de actores que usaremos para comparar con las demas tomas
                    [numero de actores en la toma, valor de la toma en decimal, indice en el array tomas original]

    tomas:  matriz que contiene todas las tomas originales representadas en una matriz de 1's y 0's

    """

    # Diccionario para guardar las tomas por parecido ordenadas de mayor a menor
    tomas_por_parecido = {}
    parecidos = []

    # iteramos a traves de la toma objetivo como tantos actores tenga
    # Con esto determinaremos los niveles de coincidencia por toma objetivo
    # Supongamos el siguiente ejemplo de toma objetivo: 11110000
    # diremos que la toma objetivo podra tener niveles de coincidencia de 0, 1, 2, 3
    for i in range(toma_objetivo[0]):
        tomas_por_parecido[i] = []
        if i not in parecidos:
            parecidos.append(i)

    # Iteramos como tantas tomas haya en el array de tomas representadas en valor decimal
    for i in range(len(tomas_decimal)):
        # Hacemos la operacion logica OR entre la toma objetivo y cada toma del array
        # para determinar los todos actores involucrados entre la toma objetivo y una toma
        temp = tomas[toma_objetivo[2]] | tomas[tomas_decimal[i][2]]
        # para determinar el nivel de coincidencia hacemos una resta de los actores involucrados
        # entre la toma objetivo y cada una de las otras tomas
        parecido = abs(len(tomas[toma_objetivo[2]][tomas[toma_objetivo[2]] == 1]) - len(temp[temp == 1]))
        # guardamos la toma en el diccionario dependiendo de su nivel de coincidencia con la toma objetivo
        tomas_por_parecido[parecido].append([tomas_decimal[i][2], i])
    
    return tomas_por_parecido, parecidos

def get_tomas_planificadas(tomas):
    """
    Obtener la planificacion de las tomas para optimizar el costo total
    """

    tomas_decimal = []
    tomas = np.array(tomas)

    # Convertimos las tomas a su valor decimal, y la ordenamos de mayor a menor.
    # Regresamos un array con la siguiente estructura: 
    # [cantidad de 1's en la toma, toma convertida de binario a decimal, indice original de la toma]
    for i in range(len(tomas)):
        my_string = ''.join(map(str, tomas[i]))
        tomas_decimal.append([len(tomas[i][tomas[i] == 1]), int(my_string, 2), i])
    
    tomas_decimal = sorted(tomas_decimal, key=operator.itemgetter(0, 1), reverse=True)

    
    solucion_final = {}
    maximo_tomas = 6
    index_delete = []
    optimo = math.ceil(len(tomas) / maximo_tomas)
    costo_total = 0
    dia = 0

    # Inicializar el diccionario que tendra la solucion final
    # El diccionario tendra como llave el optimo numero de dias para cubrir todas las tomas
    for i in range(optimo):
        solucion_final[i] = []

    # Iteramos mientras haya tomas en el array secundario tomas decimal
    while len(tomas_decimal) > 0:
        index_delete = []

        # La toma solucion sera la toma con el mayor numero de actores por cada iteracion
        toma_solucion = tomas_decimal[0]
        # Obtenemos las tomas que son parecidas para cada toma solucion en forma de un diccionario
        # Este diccionario vendra ordenado de mayor coincidencia a menor coincidencia
        solucion_parcial, llaves = get_tomas_parecidas(tomas_decimal, toma_solucion, tomas)
        index = 0
        actores = set()
        # Iteramos hasta el maxim de tomas permitido por dia
        for i in range(maximo_tomas):
            while (index in llaves) and (len(solucion_parcial[index]) == 0):
                index += 1

            # Sacamos cada toma de mayor a menor coincidencia
            # En caso de que ya no se puedan obtener más tomas y hayamos llegado al final del diccionario de coincidencias,
            # quiere decir que ya terminamos este ciclo. Esto nos ayuda cuando en la ultima sesion el numero de tomas no es igual que las demás
            try:
                j = solucion_parcial[index].pop(0)
            except:
                break

            # Guardamos los indices que seran eliminados del array que contiene las tomas convertidas a valor decimal
            index_delete.append(j[1])
            # Guardamos cada toma en el diccionario que contiene la solucion final
            solucion_final[dia].append(j[0])

            # Iteramos a traves de cada toma para obtener los actores involucrados por cada toma
            for i in range(len(tomas[j[0]])):
                if tomas[j[0]][i] == 1:
                    actores.add(i+1)
    
        
        # Eliminamos las tomas que ya han sido utilizadas para la solucion parcial pues ya no sera consideradas
        tomas_decimal = np.delete(tomas_decimal, tuple(index_delete), axis=0)
        # Calculamos el costo total contando el numero de actores por cada sesion
        costo_total += len(actores)
        print(solucion_final[dia])
        print(len(actores))
        dia += 1

    print(f'El costo total sera: {costo_total}')

get_tomas_planificadas(tomas)