import random

tablero_4x4 = [[2,2,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
tablero_5x5 = [[3,0,1,0,0],[2,0,0,0,0],[4,0,0,0,1],[4,0,0,0,0],[0,0,0,5,5]]

def copiar_tablero(tablero):
    '''Esta funcion se llama primero y lo que hace es que me copia el tablero para asi modificar el nuevo''' 
    filas = len(tablero)
    columna = len(tablero[0])
    nueva_fila = []
    tablero_nuevo = []
    for i in range(filas):
        for j in range(columna):
            nueva_fila += [tablero[i][j]]
        tablero_nuevo +=[nueva_fila]
        nueva_fila = []
    return mover_barcos(tablero, tablero_nuevo)

def mover_barcos(tablero_original, tablero_nuevo, i=0, j=0):
    '''Funcion que mueve los barcos de manera aleatorio'''
    n = len(tablero_original)
    m = len(tablero_original[0])

    # tablero_nuevo = copy.deepcopy(tablero_original) # Esto lo voy a cambiar mas adelante
    while i < n:
        while j < m:
            barco = tablero_original[i][j]
            movimiento_aleatorio = random.randint(1,3) # Esta funcion dice cuantas posiciones se movera de forma aleatoria, son entre 1 y 3
            direccion_aleatorio = random.randint(0,3) # Esta funcion dice si se movera a la derecha o izquierda, arriba o hacia abajo.  
                                                          # 0 = arriba, 1 = derecha, 2 = abajo, 3 = izquierda
            # Para los barcos de 1 espacio                                     
            if tablero_original[i][j] == 1 or tablero_original[i][j] == 4:
                return mover_barcos_un_espacio(tablero_original, tablero_nuevo, i, j, movimiento_aleatorio, direccion_aleatorio)
            # Para los barcos de 2
            elif tablero_original[i][j] == 2 or tablero_original[i][j] == 5 or tablero_original[i][j] == 3 or tablero_original[i][j] == 6:
                
                # Para los barcos verticales
                if i + 1 < n:
                    if tablero_original[i][j] == tablero_original[i + 1][j]: # Si ambos barcos estan intactos
                        return mover_barcos_dos_espacios_verticales(tablero_original, tablero_nuevo, i, j, movimiento_aleatorio, direccion_aleatorio)
                    elif tablero_original[i + 1][j] == barco + 1: # Si la otra parte esta dañada
                        return mover_barcos_dos_espacios_verticales(tablero_original, tablero_nuevo, i, j, movimiento_aleatorio, direccion_aleatorio)
                    elif tablero_original[i + 1][j] == barco - 1: # Si la parte actual esta dañada pero la siguiente no
                        return mover_barcos_dos_espacios_verticales(tablero_original, tablero_nuevo, i, j, movimiento_aleatorio, direccion_aleatorio)
                
                # Para los barcos horizontales
                elif j + 1 < m:
                    if tablero_original[i][j] == tablero_original[i][j + 1]: # Si ambos barcos estan intactos
                        return mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j, movimiento_aleatorio, direccion_aleatorio)
                    elif tablero_original[i][j + 1] == barco + 1: # Si la otra parte esta dañada
                        return mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j, movimiento_aleatorio, direccion_aleatorio)
                    elif tablero_original[i][j + 1] == barco - 1: # Si la parte actual esta dañada pero la siguiente no
                        return mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j, movimiento_aleatorio, direccion_aleatorio)
                
            j += 1
        i +=1
        j = 0
                            
    return tablero_nuevo

def mover_barcos_un_espacio(tablero_original, tablero_nuevo, i, j, movimiento_aleatorio, direccion_aleatorio):
    '''Dividir esto en dos funciones'''
    n = len(tablero_original)
    m = len(tablero_original[0])
    barco = tablero_original[i][j]
    if direccion_aleatorio == 0: # Se movera arriba
        if i - movimiento_aleatorio >= 0:
            if tablero_nuevo[i - movimiento_aleatorio][j] == 0:
                tablero_nuevo[i - movimiento_aleatorio][j] = barco
                tablero_nuevo[i][j] = 0
                return mover_barcos(tablero_original, tablero_nuevo, i, j + 1)
            else:
                return mover_barcos(tablero_original, tablero_nuevo, i, j)
        else:
            return mover_barcos(tablero_original, tablero_nuevo, i, j)
    elif direccion_aleatorio == 1: # Se movera a la derecha
        if j + movimiento_aleatorio < n:
            if tablero_nuevo[i][j + movimiento_aleatorio] == 0:
                tablero_nuevo[i][j + movimiento_aleatorio] = barco
                tablero_nuevo[i][j] = 0
                return mover_barcos(tablero_original, tablero_nuevo, i, j + 1)
            else:
                return mover_barcos(tablero_original, tablero_nuevo, i, j)
        else:
            return mover_barcos(tablero_original, tablero_nuevo, i, j)
    elif direccion_aleatorio == 2: #Se mueve hacia abajo
        if i + movimiento_aleatorio < m:
            if tablero_nuevo[i + movimiento_aleatorio][j] == 0:
                tablero_nuevo[i + movimiento_aleatorio][j] = barco
                tablero_nuevo[i][j] = 0
                return mover_barcos(tablero_original, tablero_nuevo, i, j + 1)
            else:
                return mover_barcos(tablero_original, tablero_nuevo, i, j)
        else:
            return mover_barcos(tablero_original, tablero_nuevo, i, j)
    elif direccion_aleatorio == 3: #Se mueve hacia la izquierda
        if j - movimiento_aleatorio >= 0:
            if tablero_nuevo[i][j - movimiento_aleatorio] == 0:
                tablero_nuevo[i][j - movimiento_aleatorio] = barco
                tablero_nuevo[i][j] = 0
                return mover_barcos(tablero_original, tablero_nuevo, i, j + 1)
            else:
                return mover_barcos(tablero_original, tablero_nuevo, i, j)
        else:
            return mover_barcos(tablero_original, tablero_nuevo, i, j)
        
def mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j, movimiento_aleatorio, direccion_aleatorio):
    '''Funcion que mueve los barcos pero solo los de dos espacios'''
    n = len(tablero_original)
    m = len(tablero_original[0])
    barco = tablero_original[i][j]
    if direccion_aleatorio == 0: # Se movera arriba
        if i - movimiento_aleatorio >= 0:
            if tablero_nuevo[i - movimiento_aleatorio][j] == 0 and tablero_nuevo[i - movimiento_aleatorio][j + 1] == 0:
                tablero_nuevo[i - movimiento_aleatorio][j] = barco
                tablero_nuevo[i - movimiento_aleatorio][j + 1] = tablero_nuevo[i][j + 1]
                tablero_nuevo[i][j] = 0
                tablero_nuevo[i][j + 1] = 0
                tablero_original[i][j+1] = 0
                return mover_barcos(tablero_original, tablero_nuevo, i, j + 1)
            else:
                return mover_barcos(tablero_original, tablero_nuevo, i, j)
        else:
            return mover_barcos(tablero_original, tablero_nuevo, i, j)
                        
    elif direccion_aleatorio == 1: # Se movera a la derecha
        if j + 1 + movimiento_aleatorio < n: 
            if movimiento_aleatorio == 1: # Primero hay que saber si se mueve 1 espacio o no para no borrar una parte del barco
                if tablero_nuevo[i][j + 1 + movimiento_aleatorio] == 0:
                    tablero_nuevo[i][j + 1 + movimiento_aleatorio] = tablero_nuevo[i][j + 1]
                    tablero_nuevo[i][j + movimiento_aleatorio] = barco
                    tablero_nuevo[i][j] = 0
                    tablero_original[i][j+1] = 0
                    return mover_barcos(tablero_original, tablero_nuevo, i, j + 1)
                else:
                    return mover_barcos(tablero_original, tablero_nuevo, i, j)
            else: # Si el movimiento es de 2 o tres
                if tablero_nuevo[i][j + movimiento_aleatorio] == 0 and tablero_nuevo[i][j + 1 + movimiento_aleatorio] == 0: # Ver si ambos espacios estan ocupados
                    tablero_nuevo[i][j + 1 + movimiento_aleatorio] = tablero_nuevo[i][j + 1]
                    tablero_nuevo[i][j + movimiento_aleatorio] = barco
                    tablero_nuevo[i][j] = 0
                    tablero_nuevo[i][j + 1] = 0 
                    tablero_original[i][j + 1] = 0
                    return mover_barcos(tablero_original, tablero_nuevo, i, j + 1)
                else:
                    return mover_barcos(tablero_original, tablero_nuevo, i, j)
        else:
            return mover_barcos(tablero_original, tablero_nuevo, i, j)

    elif direccion_aleatorio == 2: #Se mueve hacia abajo
        if i + movimiento_aleatorio < m:
            if tablero_nuevo[i + movimiento_aleatorio][j] == 0 and tablero_nuevo[i + movimiento_aleatorio][j + 1] == 0:
                tablero_nuevo[i + movimiento_aleatorio][j] = barco
                tablero_nuevo[i + movimiento_aleatorio][j + 1] = tablero_nuevo[i][j + 1]
                tablero_nuevo[i][j] = 0
                tablero_nuevo[i][j + 1] = 0
                tablero_original[i][j+1] = 0
                return mover_barcos(tablero_original, tablero_nuevo, i, j + 1)
            else:
                return mover_barcos(tablero_original, tablero_nuevo, i, j)
        else:
            return mover_barcos(tablero_original, tablero_nuevo, i, j)
    elif direccion_aleatorio == 3: #Se mueve hacia la izquierda
        if j - movimiento_aleatorio >= 0:
            if movimiento_aleatorio == 1: # Primero hay que saber si se mueve 1 espacio o no para no borrar una parte del barco
                if tablero_nuevo[i][j - movimiento_aleatorio] == 0:
                    tablero_nuevo[i][j - movimiento_aleatorio] = barco
                    tablero_nuevo[i][j + 1 - movimiento_aleatorio] = tablero_nuevo[i][j + 1]
                    tablero_nuevo[i][j + 1] = 0
                    tablero_original[i][j+1] = 0
                    return mover_barcos(tablero_original, tablero_nuevo, i, j + 1)
                else:
                    return mover_barcos(tablero_original, tablero_nuevo, i, j)
            else: # Si el movimiento es de 2 o 3
                if tablero_nuevo[i][j - movimiento_aleatorio] == 0 and tablero_nuevo[i][j + 1 - movimiento_aleatorio] == 0: # Ver si ambos espacios estan ocupados
                    tablero_nuevo[i][j - movimiento_aleatorio] = barco
                    tablero_nuevo[i][j + 1 - movimiento_aleatorio] = tablero_nuevo[i][j + 1]
                    tablero_nuevo[i][j] = 0
                    tablero_nuevo[i][j + 1] = 0 
                    tablero_original[i][j + 1] = 0
                    return mover_barcos(tablero_original, tablero_nuevo, i, j + 1)
                else:
                    return mover_barcos(tablero_original, tablero_nuevo, i, j)
        else:
            return mover_barcos(tablero_original, tablero_nuevo, i, j)
        
def mover_barcos_dos_espacios_verticales(tablero_original, tablero_nuevo, i, j, movimiento_aleatorio, direccion_aleatorio):
    '''Funcion que mueve los barcos que estan de forma vertical'''
    n = len(tablero_original)
    m = len(tablero_original[0])
    barco = tablero_original[i][j]
    if direccion_aleatorio == 0: # Se movera arriba
        if i - movimiento_aleatorio >= 0:
            if movimiento_aleatorio == 1:
                if tablero_nuevo[i - movimiento_aleatorio][j] == 0:
                    tablero_nuevo[i - movimiento_aleatorio][j] = barco
                    tablero_nuevo[i + 1 - movimiento_aleatorio][j] = tablero_nuevo[i + 1][j]
                    tablero_nuevo[i + 1][j] = 0
                    tablero_original[i + 1][j] = 0
                    return mover_barcos(tablero_original, tablero_nuevo, i, j + 1)
                else:
                    return mover_barcos(tablero_original, tablero_nuevo, i, j)
            else:
                if tablero_nuevo[i - movimiento_aleatorio][j] == 0 and tablero_nuevo[i + 1 - movimiento_aleatorio][j] == 0:
                    tablero_nuevo[i - movimiento_aleatorio][j] = barco
                    tablero_nuevo[i + 1 - movimiento_aleatorio][j] = tablero_nuevo[i + 1][j]
                    tablero_nuevo[i][j] = 0
                    tablero_nuevo[i + 1][j] = 0
                    tablero_original[i + 1][j] = 0
                    return mover_barcos(tablero_original, tablero_nuevo, i, j + 1)
                else:
                    return mover_barcos(tablero_original, tablero_nuevo, i, j)
        else:
            return mover_barcos(tablero_original, tablero_nuevo, i, j)
                        
    elif direccion_aleatorio == 1: # Se movera a la derecha
        if j + movimiento_aleatorio < n:
            if tablero_nuevo[i][j + movimiento_aleatorio] == 0 and tablero_nuevo[i + 1][j + movimiento_aleatorio] == 0:
                tablero_nuevo[i][j + movimiento_aleatorio] = barco
                tablero_nuevo[i + 1][j + movimiento_aleatorio] = tablero_nuevo[i + 1][j]
                tablero_nuevo[i][j] = 0
                tablero_nuevo[i + 1][j] =0
                tablero_original[i + 1][j] =0
                return mover_barcos(tablero_original, tablero_nuevo, i, j + 1)
            else:
                return mover_barcos(tablero_original, tablero_nuevo, i, j)
        else:
            return mover_barcos(tablero_original, tablero_nuevo, i, j)

    elif direccion_aleatorio == 2: #Se mueve hacia abajo
        if i + 1 + movimiento_aleatorio < m:
            if movimiento_aleatorio == 1:
                if tablero_nuevo[i + 1 + movimiento_aleatorio][j] == 0:
                    tablero_nuevo[i + 1 + movimiento_aleatorio][j] = tablero_nuevo[i + 1][j]
                    tablero_nuevo[i + movimiento_aleatorio][j] = tablero_nuevo[i][j]
                    tablero_nuevo[i][j] = 0
                    tablero_original[i + 1][j] = 0
                    return mover_barcos(tablero_original, tablero_nuevo, i, j + 1)
                else:
                    return mover_barcos(tablero_original, tablero_nuevo, i, j)
            else:
                if tablero_nuevo[i + movimiento_aleatorio][j] == 0 and tablero_nuevo[i + 1 + movimiento_aleatorio][j] == 0:
                    tablero_nuevo[i + 1 + movimiento_aleatorio][j] = tablero_nuevo[i + 1][j]
                    tablero_nuevo[i + movimiento_aleatorio][j] = barco
                    tablero_nuevo[i][j] = 0
                    tablero_nuevo[i + 1][j] = 0
                    tablero_original[i + 1][j] = 0
                    return mover_barcos(tablero_original, tablero_nuevo, i, j + 1)
                else:
                    return mover_barcos(tablero_original, tablero_nuevo, i, j)
        else:
            return mover_barcos(tablero_original, tablero_nuevo, i, j)
    elif direccion_aleatorio == 3: #Se mueve hacia la izquierda
        if j - movimiento_aleatorio >= 0:
            if tablero_nuevo[i][j - movimiento_aleatorio] == 0 and tablero_nuevo[i + 1][j - movimiento_aleatorio] == 0:
                tablero_nuevo[i][j - movimiento_aleatorio] = barco
                tablero_nuevo[i + 1][j - movimiento_aleatorio] = tablero_nuevo[i + 1][j]
                tablero_nuevo[i][j] = 0
                tablero_nuevo[i + 1][j] =0
                tablero_original[i + 1][j] =0
                return mover_barcos(tablero_original, tablero_nuevo, i, j + 1)
            else:
                return mover_barcos(tablero_original, tablero_nuevo, i, j)
        else:
            return mover_barcos(tablero_original, tablero_nuevo, i, j)

res = copiar_tablero(tablero_5x5)
print(res)