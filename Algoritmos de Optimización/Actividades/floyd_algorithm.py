# Calculo de la ruta más corta 
def floyd_algorithm(tarifas):
    n = len(tarifas)
    precios = [[]]*n
    # Copiamos la matriz tarfas a una matriz auxiliar
    for i in range(len(tarifas)):
        precios[i] = (tarifas[i])
    
    # calculo de la ruta más corta entre D[i][j] y D[i][k] + D[k][j]
    # checamos si es más rápido ir por una ruta directa o a través de un nodo intermedio
    for k in range(n):
        for i in range(n):
            for j in range(n):
                precios[i][j] = min(precios[i][j], precios[i][k] + precios[k][j])

    for i in precios:
        print(i) 

tarifas = [
           [0,5,4,3,9999,9999,9999],
           [9999,0,9999,2,3,9999,11], 
           [9999,9999, 0,1,9999,4,10],
           [9999,9999,9999, 0,5,6,9],
           [9999,9999, 9999,9999,0,9999,4],
           [9999,9999, 9999,9999,9999,0,3],
           [9999,9999,9999,9999,9999,9999,0]
          ]
floyd_algorithm(tarifas)