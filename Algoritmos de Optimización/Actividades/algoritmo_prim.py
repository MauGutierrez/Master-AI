def get_vertices(nodo, grafo):
    hijos = []
    for i in range(nodo, len(grafo)):
        if i != nodo:
            if grafo[nodo][i] == 0:
                hijos.append({
                    's': i,
                    'vertices': [None, 9999]
                })
            else:
                hijos.append({
                    's': i,
                    'vertices': [nodo, grafo[nodo][i]]
                })

    return hijos

def update_vertices(vertices, nodo_solucion, grafo, nodos_visitados):
    if len(vertices) == 0:
        return vertices

    index = 0
    for i in range(vertices[0]['s'], len(grafo)):
        if grafo[i] > 0 and i not in nodos_visitados and grafo[i] < vertices[index]['vertices'][1]:
            vertices[index]['vertices'] = [nodo_solucion['s'], grafo[i]]
        index += 1

    return vertices

def algoritmo_prim(grafo):
    # Ae recibe una lista donde tenemos el nodo y las aristas
    # Obtenemos para el nodo actual el siguiente nodo que tenga la menor distancia
    # Una vez que hayamos encontrado el nodo con menor distancia
    # metemos este nodo a la lista final y continuamos iterando
    
    # Variable donde guardaremos la solucion final 
    solucion_final = []

    # Obtenemos todos los nodos y las distancias
    vertices = get_vertices(0, grafo)

    nodos_visitados = set()

    nodos_visitados.add(0)

    # Iteramos por toda la lista 
    for i in range(len(grafo)-1):
        # Iteramos nuevamente por toda la lista para encontrar el nodo con menor distancia
        nodo_menor_distancia = min(vertices, key= lambda x: x['vertices'][1])
        
        nodos_visitados.add(nodo_menor_distancia['s'])

        # Sacamos de la lista de nodos al nodo con menor distancia para ya no considerarlo
        for i in range(len(vertices)):
            if vertices[i]['s'] == nodo_menor_distancia['s']:
                vertices.pop(i)
                break
        
        # Metemos el nodo con menor distancia a la lista de soluciones
        solucion_final.append(nodo_menor_distancia)
        # Hacemos el update de las distancias
        vertices = update_vertices(vertices, nodo_menor_distancia, grafo[nodo_menor_distancia['s']], nodos_visitados)

    return solucion_final

grafo = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

print(algoritmo_prim(grafo))
