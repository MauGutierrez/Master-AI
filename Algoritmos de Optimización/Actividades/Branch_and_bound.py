

costes = [[11, 12, 18, 40],
          [14, 15, 13, 22],
          [11, 17, 19, 23],
          [17, 14, 20, 28]]

costes_2 = [[9, 2, 7, 8],
            [6, 4, 3, 7],
            [5, 8, 1, 8],
            [7, 6, 9, 4]
           ]

# Calculo del valor esperado
def get_valor(s, costes):
  valor = 0
  for i in range(len(s)):
    valor += costes[s[i]][i]
  return valor

def get_cota_inferior(s, costes):
  valor = 0
  for i in range(len(s)):
    valor += costes[i][s[i]]
  
  for i in range(len(s), len(costes)):
    valor += min([ costes[j][i] for j in range(len(s), len(costes)) ])

  return valor

def get_cota_superior(s, costes):
  valor = 0
  for i in range(len(s)):
    valor += costes[i][s[i]]
  
  for i in range(len(s), len(costes)):
    valor += max([ costes[j][i] for j in range(len(s), len(costes)) ])
  
  return valor

def get_hijos(nodo, n):
  hijos = []
  for i in range(n):
    if i not in nodo:
      hijos.append({'s': nodo + (i,)})
  
  return hijos

def branch_and_bound(costes):
  dimension = len(costes)
  mejor_solucion = tuple(i for i in range(len(costes)))
  cota_superior = get_cota_superior(mejor_solucion, costes)

  nodos = []
  nodos.append({'s': (), 'cota_inferior': get_cota_inferior((), costes)})

  while len(nodos) > 0:
    # Obtener nodo prometedor como el nodo con menor valor de cota inferior
    # Ya que puede regresar varios mínimos, escogemos el primer mínimo pues este fue el primer minimo por orden
    # agregado
    nodo_prometedor = [min(nodos, key= lambda x: x['cota_inferior'])][0]['s']
    # obtener hijos del nodo prometedor y calcular la cota inferior de los hijos
    hijos = [{'s': x['s'], 'cota_inferior': get_cota_inferior(x['s'], costes)} for x in get_hijos(nodo_prometedor, dimension)]
    # checamos a ver si hay algun nodo que ya tenga una dimension igual a la matriz de costes
    nodo_final = [x for x in hijos if len(x['s']) == dimension]
    # si nodo final existe, ya hemos alcanzado una solucion.
    if len(nodo_final) > 0:
      # Si la actual cota superior es mayor
      # al valor de la cota inferior del nodo prometedor, actualizar cota superior
      if nodo_final[0]['cota_inferior'] < cota_superior:
        # actualizar mejor solucion
        mejor_solucion = nodo_final
        # actualizar cota sperior
        cota_superior = nodo_final[0]['cota_inferior']
        
    # podar los hijos que tengan un valor mayor a la cota superior
    hijos = [ x for x in hijos if x['cota_inferior'] < cota_superior ]
    # actualizar la lista de nodos con los hijos
    nodos.extend(hijos)
    # quitar el nodo prometedor de la lista de nodos
    nodos = [x for x in nodos if x['s'] != nodo_prometedor]
  
  print(f'La mejor solucion es: {mejor_solucion}')

branch_and_bound(costes)
branch_and_bound(costes_2)
