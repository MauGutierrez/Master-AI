# funcion helper para detectar si hay un elemento
# en la misma fila o amenaza entre diagonales
def solucion_prometedora(solucion, etapa):
    n = etapa
    for i in range(n+1):
        # Checar amenaza entre renglones
        if solucion.count(solucion[i]) > 1:
            return False
        # Checar amenaza entre diagonales
        for j in range(i+1, n+1):
            if abs(i-j) == abs(solucion[i]- solucion[j]):
                return False
    # Si terminamos de iterar el array solucion y quiere decir que no hay amenaza
    return True

def reinas(n, solucion=[], etapa=0):
    # Inicializamos el array solucion
    if len(solucion) == 0:
        solucion = [0 for i in range(n)]
    
    # Iteramos a través del tablero
    for i in range(1, n+1):
        # Colocamos una reina en el primer lugar disponible de la fila
        solucion[etapa] = i
        # Si no hay amenaza
        if solucion_prometedora(solucion, etapa):
            # si la etapa es igual a la dimension del tablero, hemos terminado
            if etapa == n-1:
                print(solucion)
            # si no, todavía tenemos que seguir iterando con las siguientes reinas
            else:
                reinas(n, solucion, etapa+1)
        else:
            None
    # No hay solucion para cierta reina
    solucion[etapa] = 0

reinas(4)