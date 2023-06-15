import random

tablero_4x4 = [[1,0,0,0],[0,1,0,0],[4,0,4,0],[0,0,0,0]]
tablero_5x5 = [[0,0,0,0,3],[0,0,0,0,2],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
tablero_5x5_copia = [[0,0,0,0,3],[0,0,0,0,2],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

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
    return tablero_nuevo

def mover_barcos(tablero_original):
    '''Funcion que mueve los barcos de manera aleatorio'''
    i = 0
    j = 0
    n = len(tablero_original)
    m = len(tablero_original[0])

    # tablero_nuevo = copiar_tablero(tablero_original)
    tablero_nuevo = tablero_5x5_copia

    while i < n:
        while j < m:
            # Para los barcos de 1 espacio                                     
            if tablero_original[i][j] == 1 or tablero_original[i][j] == 4:
                mover_barcos_un_espacio(tablero_original, tablero_nuevo, i, j)
            # Para los barcos de 2
            elif tablero_original[i][j] == 2:
                if i + 1 < n:
                    if tablero_original[i][j] == tablero_original[i + 1][j]: # Si ambos barcos estan intactos
                        mover_barcos_dos_espacios_verticales(tablero_original, tablero_nuevo, i, j)
                    elif tablero_original[i + 1][j] == 3: # Si la otra parte esta dañada
                        mover_barcos_dos_espacios_verticales(tablero_original, tablero_nuevo, i, j)
                    else:
                        mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j) #Significa que el barco esta de forma horizontal
                
                # Para los barcos horizontales
                elif j + 1 < m:
                    if tablero_original[i][j] == tablero_original[i][j + 1]: # Si ambos barcos estan intactos
                        mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j)
                    elif tablero_original[i][j + 1] == 3: # Si la otra parte esta dañada
                        mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j)

            elif tablero_original[i][j] == 3:
                if i + 1 < n:
                    if tablero_original[i][j] == tablero_original[i + 1][j]: # Si ambos barcos estan intactos
                        mover_barcos_dos_espacios_verticales(tablero_original, tablero_nuevo, i, j)
                    elif tablero_original[i + 1][j] == 2: # Si la otra parte esta dañada
                        mover_barcos_dos_espacios_verticales(tablero_original, tablero_nuevo, i, j)
                    else:
                        mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j) #Significa que el barco esta de forma horizontal
                
                # Para los barcos horizontales
                elif j + 1 < m:
                    if tablero_original[i][j] == tablero_original[i][j + 1]: # Si ambos barcos estan intactos
                        mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j)
                    elif tablero_original[i][j + 1] == 2: # Si la otra parte esta dañada
                        mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j)
                    
            elif tablero_original[i][j] == 5:
                if i + 1 < n:
                    if tablero_original[i][j] == tablero_original[i + 1][j]: # Si ambos barcos estan intactos
                        mover_barcos_dos_espacios_verticales(tablero_original, tablero_nuevo, i, j)
                    elif tablero_original[i + 1][j] == 6: # Si la otra parte esta dañada
                        mover_barcos_dos_espacios_verticales(tablero_original, tablero_nuevo, i, j)
                    else:
                        mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j) #Significa que el barco esta de forma horizontal
                
                # Para los barcos horizontales
                elif j + 1 < m:
                    if tablero_original[i][j] == tablero_original[i][j + 1]: # Si ambos barcos estan intactos
                        mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j)
                    elif tablero_original[i][j + 1] == 6: # Si la otra parte esta dañada
                        mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j)    
            
            elif tablero_original[i][j] == 6:
                if i + 1 < n:
                    if tablero_original[i][j] == tablero_original[i + 1][j]: # Si ambos barcos estan intactos
                        mover_barcos_dos_espacios_verticales(tablero_original, tablero_nuevo, i, j)
                    elif tablero_original[i + 1][j] == 5: # Si la otra parte esta dañada
                        mover_barcos_dos_espacios_verticales(tablero_original, tablero_nuevo, i, j)
                    else:
                        mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j) #Significa que el barco esta de forma horizontal
                
                # Para los barcos horizontales
                elif j + 1 < m:
                    if tablero_original[i][j] == tablero_original[i][j + 1]: # Si ambos barcos estan intactos
                        mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j)
                    elif tablero_original[i][j + 1] == 5: # Si la otra parte esta dañada
                        mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j)   
                    
                
            j += 1
        i +=1
        j = 0
                            
    return tablero_nuevo

def mover_barcos_un_espacio(tablero_original, tablero_nuevo, i, j):
    '''Dividir esto en dos funciones'''
    n = len(tablero_original)
    m = len(tablero_original[0])
    barco = tablero_original[i][j]
    while tablero_nuevo[i][j] != 0:
        movimiento_aleatorio = random.randint(1,3) # Esta funcion dice cuantas posiciones se movera de forma aleatoria, son entre 1 y 3
        direccion_aleatorio = random.randint(0,3) # Esta funcion dice si se movera a la derecha o izquierda, arriba o hacia abajo.  
                                                          # 0 = arriba, 1 = derecha, 2 = abajo, 3 = izquierda
        if direccion_aleatorio == 0: # Se movera arriba
            if i - movimiento_aleatorio >= 0:
                if tablero_nuevo[i - movimiento_aleatorio][j] == 0:
                    tablero_nuevo[i - movimiento_aleatorio][j] = barco
                    tablero_nuevo[i][j] = 0

        elif direccion_aleatorio == 1: # Se movera a la derecha
            if j + movimiento_aleatorio < n:
                if tablero_nuevo[i][j + movimiento_aleatorio] == 0:
                    tablero_nuevo[i][j + movimiento_aleatorio] = barco
                    tablero_nuevo[i][j] = 0

        elif direccion_aleatorio == 2: #Se mueve hacia abajo
            if i + movimiento_aleatorio < m:
                if tablero_nuevo[i + movimiento_aleatorio][j] == 0:
                    tablero_nuevo[i + movimiento_aleatorio][j] = barco
                    tablero_nuevo[i][j] = 0

        elif direccion_aleatorio == 3: #Se mueve hacia la izquierda
            if j - movimiento_aleatorio >= 0:
                if tablero_nuevo[i][j - movimiento_aleatorio] == 0:
                    tablero_nuevo[i][j - movimiento_aleatorio] = barco
                    tablero_nuevo[i][j] = 0
        
def mover_barcos_dos_espacios_horizontales(tablero_original, tablero_nuevo, i, j):
    '''Funcion que mueve los barcos pero solo los de dos espacios'''
    n = len(tablero_original)
    m = len(tablero_original[0])
    barco = tablero_original[i][j]
    while tablero_nuevo[i][j] != 0:
        movimiento_aleatorio = random.randint(1,3) # Esta funcion dice cuantas posiciones se movera de forma aleatoria, son entre 1 y 3
        direccion_aleatorio = random.randint(0,3) # Esta funcion dice si se movera a la derecha o izquierda, arriba o hacia abajo.  
                                                          # 0 = arriba, 1 = derecha, 2 = abajo, 3 = izquierda
    
        if direccion_aleatorio == 0: # Se movera arriba
            if i - movimiento_aleatorio >= 0:
                if tablero_nuevo[i - movimiento_aleatorio][j] == 0 and tablero_nuevo[i - movimiento_aleatorio][j + 1] == 0:
                    tablero_nuevo[i - movimiento_aleatorio][j] = barco
                    tablero_nuevo[i - movimiento_aleatorio][j + 1] = tablero_nuevo[i][j + 1]
                    tablero_nuevo[i][j] = 0
                    tablero_nuevo[i][j + 1] = 0
                    tablero_original[i][j+1] = 0
                            
        elif direccion_aleatorio == 1: # Se movera a la derecha
            if j + 1 + movimiento_aleatorio < n: 
                if movimiento_aleatorio == 1: # Primero hay que saber si se mueve 1 espacio o no para no borrar una parte del barco
                    if tablero_nuevo[i][j + 1 + movimiento_aleatorio] == 0:
                        tablero_nuevo[i][j + 1 + movimiento_aleatorio] = tablero_nuevo[i][j + 1]
                        tablero_nuevo[i][j + movimiento_aleatorio] = barco
                        tablero_nuevo[i][j] = 0
                        tablero_original[i][j+1] = 0

                else: # Si el movimiento es de 2 o tres
                    if tablero_nuevo[i][j + movimiento_aleatorio] == 0 and tablero_nuevo[i][j + 1 + movimiento_aleatorio] == 0: # Ver si ambos espacios estan ocupados
                        tablero_nuevo[i][j + 1 + movimiento_aleatorio] = tablero_nuevo[i][j + 1]
                        tablero_nuevo[i][j + movimiento_aleatorio] = barco
                        tablero_nuevo[i][j] = 0
                        tablero_nuevo[i][j + 1] = 0 
                        tablero_original[i][j + 1] = 0

        elif direccion_aleatorio == 2: #Se mueve hacia abajo
            if i + movimiento_aleatorio < m:
                if tablero_nuevo[i + movimiento_aleatorio][j] == 0 and tablero_nuevo[i + movimiento_aleatorio][j + 1] == 0:
                    tablero_nuevo[i + movimiento_aleatorio][j] = barco
                    tablero_nuevo[i + movimiento_aleatorio][j + 1] = tablero_nuevo[i][j + 1]
                    tablero_nuevo[i][j] = 0
                    tablero_nuevo[i][j + 1] = 0
                    tablero_original[i][j+1] = 0
        
        elif direccion_aleatorio == 3: #Se mueve hacia la izquierda
            if j - movimiento_aleatorio >= 0:
                if movimiento_aleatorio == 1: # Primero hay que saber si se mueve 1 espacio o no para no borrar una parte del barco
                    if tablero_nuevo[i][j - movimiento_aleatorio] == 0:
                        tablero_nuevo[i][j - movimiento_aleatorio] = barco
                        tablero_nuevo[i][j + 1 - movimiento_aleatorio] = tablero_nuevo[i][j + 1]
                        tablero_nuevo[i][j + 1] = 0
                        tablero_original[i][j+1] = 0

                else: # Si el movimiento es de 2 o 3
                    if tablero_nuevo[i][j - movimiento_aleatorio] == 0 and tablero_nuevo[i][j + 1 - movimiento_aleatorio] == 0: # Ver si ambos espacios estan ocupados
                        tablero_nuevo[i][j - movimiento_aleatorio] = barco
                        tablero_nuevo[i][j + 1 - movimiento_aleatorio] = tablero_nuevo[i][j + 1]
                        tablero_nuevo[i][j] = 0
                        tablero_nuevo[i][j + 1] = 0 
                        tablero_original[i][j + 1] = 0
        
def mover_barcos_dos_espacios_verticales(tablero_original, tablero_nuevo, i, j):
    '''Funcion que mueve los barcos que estan de forma vertical'''
    n = len(tablero_original)
    m = len(tablero_original[0])
    barco = tablero_original[i][j]
    while tablero_nuevo[i][j] != 0:
        movimiento_aleatorio = random.randint(1,3) # Esta funcion dice cuantas posiciones se movera de forma aleatoria, son entre 1 y 3
        direccion_aleatorio = random.randint(0,3) # Esta funcion dice si se movera a la derecha o izquierda, arriba o hacia abajo.  
                                                          # 0 = arriba, 1 = derecha, 2 = abajo, 3 = izquierda
        if direccion_aleatorio == 0: # Se movera arriba
            if i - movimiento_aleatorio >= 0:
                if movimiento_aleatorio == 1:
                    if tablero_nuevo[i - movimiento_aleatorio][j] == 0:
                        tablero_nuevo[i - movimiento_aleatorio][j] = barco
                        tablero_nuevo[i + 1 - movimiento_aleatorio][j] = tablero_nuevo[i + 1][j]
                        tablero_nuevo[i + 1][j] = 0
                        tablero_original[i + 1][j] = 0
                else:
                    if tablero_nuevo[i - movimiento_aleatorio][j] == 0 and tablero_nuevo[i + 1 - movimiento_aleatorio][j] == 0:
                        tablero_nuevo[i - movimiento_aleatorio][j] = barco
                        tablero_nuevo[i + 1 - movimiento_aleatorio][j] = tablero_nuevo[i + 1][j]
                        tablero_nuevo[i][j] = 0
                        tablero_nuevo[i + 1][j] = 0
                        tablero_original[i + 1][j] = 0
                            
        elif direccion_aleatorio == 1: # Se movera a la derecha
            if j + movimiento_aleatorio < n:
                if tablero_nuevo[i][j + movimiento_aleatorio] == 0 and tablero_nuevo[i + 1][j + movimiento_aleatorio] == 0:
                    tablero_nuevo[i][j + movimiento_aleatorio] = barco
                    tablero_nuevo[i + 1][j + movimiento_aleatorio] = tablero_nuevo[i + 1][j]
                    tablero_nuevo[i][j] = 0
                    tablero_nuevo[i + 1][j] =0
                    tablero_original[i + 1][j] =0
    
        elif direccion_aleatorio == 2: #Se mueve hacia abajo
            if i + 1 + movimiento_aleatorio < m:
                if movimiento_aleatorio == 1:
                    if tablero_nuevo[i + 1 + movimiento_aleatorio][j] == 0:
                        tablero_nuevo[i + 1 + movimiento_aleatorio][j] = tablero_nuevo[i + 1][j]
                        tablero_nuevo[i + movimiento_aleatorio][j] = tablero_nuevo[i][j]
                        tablero_nuevo[i][j] = 0
                        tablero_original[i + 1][j] = 0
                else:
                    if tablero_nuevo[i + movimiento_aleatorio][j] == 0 and tablero_nuevo[i + 1 + movimiento_aleatorio][j] == 0:
                        tablero_nuevo[i + 1 + movimiento_aleatorio][j] = tablero_nuevo[i + 1][j]
                        tablero_nuevo[i + movimiento_aleatorio][j] = barco
                        tablero_nuevo[i][j] = 0
                        tablero_nuevo[i + 1][j] = 0
                        tablero_original[i + 1][j] = 0
        
        elif direccion_aleatorio == 3: #Se mueve hacia la izquierda
            if j - movimiento_aleatorio >= 0:
                if tablero_nuevo[i][j - movimiento_aleatorio] == 0 and tablero_nuevo[i + 1][j - movimiento_aleatorio] == 0:
                    tablero_nuevo[i][j - movimiento_aleatorio] = barco
                    tablero_nuevo[i + 1][j - movimiento_aleatorio] = tablero_nuevo[i + 1][j]
                    tablero_nuevo[i][j] = 0
                    tablero_nuevo[i + 1][j] =0
                    tablero_original[i + 1][j] =0

res = mover_barcos(tablero_5x5)
print(res)