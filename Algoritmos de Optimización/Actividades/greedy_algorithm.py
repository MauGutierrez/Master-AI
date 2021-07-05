def cambio_monedas(cantidad, sistema_monetario):
    n = len(sistema_monetario)
    solucion = [0]*n
    valor_acumulado = 0
    # Calculamos la cantidad de monedas necesarias por moneda del sistema monetario
    for i in range(n):
        monedas = int((cantidad-valor_acumulado)/sistema_monetario[i])
        solucion[i] = monedas
        valor_acumulado += monedas * sistema_monetario[i]
        # si la cantidad acumulada es igual a la cantidad terminamos el problema
        if valor_acumulado == cantidad:
            return solucion

    return solucion

print(cambio_monedas(48, [25, 10, 5, 1]))