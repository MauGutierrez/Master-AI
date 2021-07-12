import math
import itertools

tomas = [
    [1,1,1,1,1,0,0,0,0,0],
    [0,0,1,1,1,0,0,0,0,0],
    [0,1,0,0,1,0,1,0,0,0],
    [1,1,0,0,0,0,1,1,0,0],
    [0,1,0,1,0,0,0,1,0,0],
    [1,1,0,1,1,0,0,0,0,0],
    [1,1,0,1,1,0,0,0,0,0],
]

maximo_tomas = 6
numero_actores = len(tomas[0])

optimo = math.ceil(len(tomas) / maximo_tomas)

tomas_nuevas = []
for i in range(len(tomas)):
    tomas_nuevas.append([i, tomas[i]])

permutations_tomas = list(itertools.permutations(tomas_nuevas))

sesiones = dict()
solucion = dict()
costo_solucion = 9999

for i in range(optimo):
    sesiones[i] = 9999
    solucion[i] = 0

for i in range(len(permutations_tomas)):
    dia = 0
    sesion = 0
    actores = set()
    costo_parcial = 0
    tomas_id = []
    for j in range(len(tomas)):
        tomas_id.append(permutations_tomas[i][j][0])
        for k in range(len(permutations_tomas[i][j][1])):
            if permutations_tomas[i][j][1][k] == 1:
                actores.add(k)
        
        dia += 1
        if dia == maximo_tomas or j == len(tomas)-1:
            sesiones[sesion] = tomas_id.copy()
            costo_parcial += len(actores)
            actores.clear()
            tomas_id.clear()
            sesion += 1
            dia = 0
        
    if costo_parcial < costo_solucion:
        for i in range(len(sesiones)):
            solucion[i] = sesiones[i]

        costo_solucion = costo_parcial

print(f'costo_parcial: {costo_solucion}')
print(solucion)