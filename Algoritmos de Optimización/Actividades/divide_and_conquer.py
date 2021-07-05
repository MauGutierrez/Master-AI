# Resolvemos recursivamente el problema
def torres_hanoi(n, torre_inicio, torre_aux, torre_final):
    # caso base cuando solo tenemos que mover una pieza
    if n == 1:
        print(f'Mover {torre_inicio} a {torre_final}')
    else:
        # Queremos mover a la torre auxiliar
        torres_hanoi(n-1, torre_inicio, torre_final, torre_aux)
        print(f'Mover {torre_inicio} a {torre_final}')
        # Queremos mover desde la torre auxiliar 
        torres_hanoi(n-1, torre_aux, torre_inicio, torre_final)

# torres_hanoi(3, 1, 2, 3)
torres_hanoi(4, 1, 2, 3)