import random
import copy

tablero_4x4 = [[0,0,2,2],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def seleccionar_barcos(tablero):
    '''Funcion que mueve todos los barcos de manera aleatoria'''   
    return mover_barcos(tablero, tablero)

def mover_barcos(tablero_original):
    '''Funcion que ahora si mueve los barcos'''
    i = 0
    j = 0
    n = len(tablero_original)
    m = len(tablero_original[0])

    tablero_nuevo = copy.deepcopy(tablero_original) #No estoy seguro si se puede usar, pero esto es para que me modifique otro tablero
    while i < n:
        while j < m:
            movimiento_aleatorio = random.randint(1,1) # Esta funcion dice cuantas posiciones se movera de forma aleatoria, son entre 1 y 3
            direccion_aleatorio = random.randint(3,3) # Esta funcion dice si se movera a la derecha o izquierda, arriba o hacia abajo.  
                                                          # 0 = arriba, 1 = derecha, 2 = abajo, 3 = izquierda
                
            # Para los barcos de 1 espacio                                     
            if tablero_original[i][j] == 1 or tablero_original[i][j] == 4:
                barco = tablero_original[i][j]
                if direccion_aleatorio == 0: # Se movera arriba
                        # tablero_original_transpuesto = transpuesta(tablero_original)
                    if i - movimiento_aleatorio >= 0:
                        if tablero_original[i - movimiento_aleatorio][j] == 0 and tablero_nuevo[i - movimiento_aleatorio][j] == 0:
                            tablero_nuevo[i - movimiento_aleatorio][j] = barco
                            tablero_nuevo[i][j] = 0
                        else:
                            continue
                    else:
                        continue
                    
                elif direccion_aleatorio == 1: # Se movera a la derecha
                    if j + movimiento_aleatorio < n:
                        if tablero_original[i][j + movimiento_aleatorio] == 0 and tablero_nuevo[i][j + movimiento_aleatorio] == 0:
                            tablero_nuevo[i][j + movimiento_aleatorio] = barco
                            tablero_nuevo[i][j] = 0
                        else:
                            continue
                    else:
                        continue
                            # if j == n-1:
                            #     continue
                            # elif j + movimiento_aleatorio - 1 < n:
                            #     tablero_nuevo[i][j + movimiento_aleatorio -1 ] = barco
                            #     tablero_nuevo[i][j] = 0
                            # elif j + movimiento_aleatorio - 2 < n:
                            #     tablero_nuevo[i][j + movimiento_aleatorio - 2 ] = barco
                            #     tablero_nuevo[i][j] = 0

                elif direccion_aleatorio == 2: #Se mueve hacia abajo
                    if i + movimiento_aleatorio < m:
                        if tablero_original[i + movimiento_aleatorio][j] == 0 and tablero_nuevo[i + movimiento_aleatorio][j] == 0:
                            tablero_nuevo[i + movimiento_aleatorio][j] = barco
                            tablero_nuevo[i][j] = 0
                        else:
                            continue
                    else:
                        continue
                elif direccion_aleatorio == 3: #Se mueve hacia la izquierda
                    if j - movimiento_aleatorio >= 0:
                        if tablero_original[i][j - movimiento_aleatorio] == 0 and tablero_nuevo[i][j - movimiento_aleatorio] == 0:
                            tablero_nuevo[i][j - movimiento_aleatorio] = barco
                            tablero_nuevo[i][j] = 0
                        else:
                            continue
                    else:
                        continue

            # Para los barcos de 2
            if tablero_original[i][j] == 2 or tablero_original[i][j] == 5:
                barco_parte1 = tablero_original[i][j]
                barco_parte2 = tablero_original[i][j+1]
                if direccion_aleatorio == 0: # Se movera arriba
                    # tablero_original_transpuesto = transpuesta(tablero_original)
                    if i - movimiento_aleatorio >= 0:
                        temp = movimiento_aleatorio
                        temp1 = temp
                        if tablero_original[i - movimiento_aleatorio][j] == 0 and tablero_nuevo[i - movimiento_aleatorio][j] == 0:
                            tablero_nuevo[i - movimiento_aleatorio][j] = barco_parte1
                            tablero_nuevo[i - movimiento_aleatorio][j + 1] = barco_parte2
                            tablero_nuevo[i][j] = 0
                            tablero_nuevo[i][j + 1] = 0
                            tablero_original[i][j+1] = 0
                        else:
                            continue
                    else:
                        continue
                    
                elif direccion_aleatorio == 1: # Se movera a la derecha
                    if j + 1 + movimiento_aleatorio < n:
                        if tablero_original[i][j + 1 + movimiento_aleatorio] == 0 and tablero_nuevo[i][j + 1 + movimiento_aleatorio] == 0:
                            if movimiento_aleatorio == 1:
                                tablero_nuevo[i][j + 1 + movimiento_aleatorio] = barco_parte2
                                tablero_nuevo[i][j + movimiento_aleatorio] = barco_parte1
                                tablero_nuevo[i][j] = 0
                                tablero_original[i][j+1] = 0
                            else:
                                tablero_nuevo[i][j + 1 + movimiento_aleatorio] = barco_parte2
                                tablero_nuevo[i][j + movimiento_aleatorio] = barco_parte1
                                tablero_nuevo[i][j] = 0
                                tablero_nuevo[i][j+1] = 0
                                tablero_original[i][j+1] = 0
                        else:
                            continue
                    else:
                        continue
                            # if j == n-1:
                            #     continue
                            # elif j + movimiento_aleatorio - 1 < n:
                            #     tablero_nuevo[i][j + movimiento_aleatorio -1 ] = barco
                            #     tablero_nuevo[i][j] = 0
                            # elif j + movimiento_aleatorio - 2 < n:
                            #     tablero_nuevo[i][j + movimiento_aleatorio - 2 ] = barco
                            #     tablero_nuevo[i][j] = 0

                elif direccion_aleatorio == 2: #Se mueve hacia abajo
                    if i + movimiento_aleatorio < m:
                        if tablero_original[i + movimiento_aleatorio][j] == 0 and tablero_nuevo[i + movimiento_aleatorio][j] == 0 and tablero_nuevo[i + movimiento_aleatorio][j + 1] == 0 and tablero_nuevo[i + movimiento_aleatorio][j + 1]:
                            tablero_nuevo[i + movimiento_aleatorio][j] = barco_parte1
                            tablero_nuevo[i + movimiento_aleatorio][j + 1] = barco_parte2
                            tablero_nuevo[i][j] = 0
                            tablero_nuevo[i][j + 1] = 0
                            tablero_original[i][j+1] = 0
                        else:
                            continue
                    else:
                        continue
                elif direccion_aleatorio == 3: #Se mueve hacia la izquierda
                    if j - movimiento_aleatorio >= 0:
                        if tablero_original[i][j - movimiento_aleatorio] == 0 and tablero_nuevo[i][j - movimiento_aleatorio] == 0:
                            if movimiento_aleatorio == 1:
                                tablero_nuevo[i][j + 1 + movimiento_aleatorio] = barco_parte2
                                tablero_nuevo[i][j + movimiento_aleatorio] = barco_parte1
                                tablero_nuevo[i][j] = 0
                                tablero_original[i][j+1] = 0
                            else:
                                tablero_nuevo[i][j + 1 + movimiento_aleatorio] = barco_parte1
                                tablero_nuevo[i][j - movimiento_aleatorio] = barco_parte2
                                tablero_nuevo[i][j] = 0
                                tablero_nuevo[i][j+1] = 0
                                tablero_original[i][j+1] = 0
                            tablero_nuevo[i][j - movimiento_aleatorio] = barco_parte1
                            tablero_nuevo[i][j + 1 - movimiento_aleatorio] = barco_parte2
                            tablero_nuevo[i][j] = 0
                        else:
                            continue
                    else:
                        continue
            j += 1
        i +=1
        j = 0
                            
    return tablero_nuevo


res = mover_barcos(tablero_4x4)
print(res)