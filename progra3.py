import random

tablero_4x4 = [[1,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def transpuesta(M):
    '''Funcion que retorna la transpuesta de la matriz'''
    i = 0
    j = 0
    n = len(M)
    m = len(M[0])
    nueva_fila = []
    matriz_resultado = []
    while i < m:
        while j < n:
            nueva_fila += [M[j][i]]
            j += 1
        matriz_resultado += [nueva_fila]
        nueva_fila = []
        i += 1
        j = 0
    return matriz_resultado


def seleccionar_barcos(tablero, i=0, j=0):
    '''Funcion que mueve todos los barcos de manera aleatoria'''
    n = len(tablero)
    m = len(tablero[0])
    while i < n:
        while j < m:
            if 0 < tablero[i][j] < 7:
                return mover_barcos(tablero, tablero[i][j], i, j)
            j +=1
        i +=1
        j = 0
    return tablero

def mover_barcos(tablero, barco, pos_fila, pos_columna):
    '''Funcion que ahora si mueve los barcos'''
    n = len(tablero)
    m = len(tablero[0])
    filas_columnas_aleatorio = random.randint(0,0) #Esta otra dice si se mueve de forma horizontal o vertical
    direccion_aleatorio = random.randint(0,1) # Esta funcion dice si se movera a la derecha o izquierda, arriba o hacia abajo
    movimiento_aleatorio = random.randint(0,3) # Esta funcion dice cuantas posiciones se movera de forma aleatoria

    if filas_columnas_aleatorio == 0: # Si es 0, se mueve horizontalmente

        if direccion_aleatorio == 0: # 0 indice que se movera a la derecha
            if pos_columna + movimiento_aleatorio < n: # Si la posicion es valida
                if tablero[pos_fila][pos_columna + movimiento_aleatorio] == 0: # Si en la casilla en la que se movera esta vacia
                    tablero[pos_fila][pos_columna + movimiento_aleatorio] = barco
                    tablero[pos_fila][pos_columna] = 0
                    return seleccionar_barcos(tablero, pos_fila, pos_columna + 1)
                else:
                    print("Casilla ocupada")
                    return mover_barcos(tablero, barco, pos_fila, pos_columna)
            else:
                print("La casilla se paso")
                return mover_barcos(tablero, barco, pos_fila, pos_columna)
        elif direccion_aleatorio == 1:
            if pos_columna + movimiento_aleatorio < n: # Si la posicion es valida
                if tablero[pos_fila][pos_columna - movimiento_aleatorio] == 0: # Si en la casilla en la que se movera esta vacia
                    tablero[pos_fila][pos_columna - movimiento_aleatorio] = barco
                    tablero[pos_fila][pos_columna] = 0
                    return seleccionar_barcos(tablero, pos_fila, pos_columna + 1)
                else:
                    print("Casilla ocupada")
                    return mover_barcos(tablero, barco, pos_fila, pos_columna)
            else:
                print("La casilla se paso")
                return mover_barcos(tablero, barco, pos_fila, pos_columna)

# print(mover_barcos(tablero_4x4))
print(seleccionar_barcos(tablero_4x4))