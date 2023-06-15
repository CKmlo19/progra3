import random
rojo = "\033[;31m"
amarillo = "\033[;33m"
azul = "\033[;34m"
cian = "\033[;36m"
blanco = "\033[;37m"
tablero5x5 = [[1,5,5,0,0],[0,4,0,1,0],[0,0,2,0,0],[0,4,2,0,0],[0,0,0,0,0]]
tablero_4x4 = [[2,2,0,0],[0,1,4,0],[0,5,0,1],[4,5,0,0]]

def iniciar_juego():
    '''Funcion que inicia el juego'''
    print("Bienvenido al intento de Battleship! xd")
    tamaño_usuario = input("Digite el tamaño que quieres que sea el tablero: ")
    jugador1 = input("Digite el nombre del jugador 1: ")
    jugador2 = input("Digite el nombre del jugador 2: ")
    jugadores = [jugador1, jugador2]
    if tamaño_usuario.isdigit() == True: # Se cambia despues, es para ver que sea un digito
        tamaño_tablero = int(tamaño_usuario)
        tablero_generado = generar_tablero(tamaño_tablero)
        if type(tablero_generado) != list:
            return "Error 02"
        else:
            return turnos(tablero_generado, jugadores)
    else:
        return "Error 01"


def generar_tablero(largo):
    '''Genera un tablero para el juego'''

    if type(largo) != int:
        return "Error01"
    elif largo < 4:
        #Colocar validación de casillas máximas
        return "Error02"
    
    i = 0
    mat = []

    while i < largo:
        j = 0
        fila = []

        while j < largo:
            fila += [0]
            j += 1
        
        mat += [fila]
        i += 1
    
    i = 0
    mat = colocar_barcos(mat, largo)

    return mat

def colocar_barcos(mat, largo):
    '''Coloca los barcos de cada jugador en el tablero'''

    if type(mat) != list or type(largo) != int:
        return "Error01"
    
    peque1 = 2
    gran1 = 1
    peque2 = 2
    gran2 = 1

    while peque1 > 0 or gran1 > 0 or peque2 > 0 or gran2 > 0:
        i = 0

        while i < largo:
            j = 0

            while j < largo:
                barco = random.randint(1, largo**2)
                casilla_libre = verificar_alrededor(mat, i, j, 0)

                if barco == 1 and mat[i][j] == 0 and peque1 > 0:
                    mat[i][j] = 1
                    peque1 -= 1

                elif barco == 2 and mat[i][j] == 0 and gran1 > 0 and casilla_libre == True:
                    mat[i][j] = 2
                    gran1 -= 1

                    pos = random.choice([-1, 1])
                    dirección = random.choice([i, j])

                    if dirección == i:
                        posi = i + pos
                        posj = j
                    else:
                        posi = i
                        posj = j + pos
                    
                    while pos + dirección < 0 or pos + dirección >= largo or mat[posi][posj] != 0:
                        pos = random.choice([-1, 1])

                        if dirección == i:
                            posi = i + pos
                            posj = j
                        else:
                            posi = i
                            posj = j + pos
                    
                    mat[posi][posj] = 2

                elif barco == 4 and mat[i][j] == 0 and peque2 > 0:
                    mat[i][j] = 4
                    peque2 -= 1

                elif barco == 5 and mat[i][j] == 0 and gran2 > 0 and casilla_libre == True:
                    mat[i][j] = 5
                    gran2 -= 1

                    pos = random.choice([-1, 1])
                    dirección = random.choice([i, j])

                    if dirección == i:
                        posi = i + pos
                        posj = j
                    else:
                        posi = i
                        posj = j + pos
                    
                    while pos + dirección < 0 or pos + dirección >= largo or mat[posi][posj] != 0:
                        pos = random.choice([-1, 1])

                        if dirección == i:
                            posi = i + pos
                            posj = j
                        else:
                            posi = i
                            posj = j + pos
                    
                    mat[posi][posj] = 5
            
                j += 1
        
            i += 1

    return mat

def verificar_alrededor(mat, i, j, barco):
    '''Verfica alrededor de una casilla hay alguna con un valor determinado'''

    if type(mat) != list or type(i) != int or type(j) != int or type(barco) != int:
        return "Error01"

    largo = len(mat)

    if i-1 >= 0:
        if mat[i-1][j] == barco:
            return True
    if i+1 < largo:
        if mat[i+1][j] == barco:
            return True
    if j-1 >= 0:
        if mat[i][j-1] == barco:
            return True
    if j+1 < largo:
        if mat[i][j+1] == barco:
            return True
    else:
        return False

# res = generar_tablero(8)
# print(res)
# i = 0
# largo = len(res)
# while i < largo:
#     print(res[i])
#     i +=1 

# -------------------------------------------------------------------------------------------------------------------------------------

def imprimir_tablero(mat):
    '''Imprime el tablero de juego'''

    print("\033[2J\033[1;1f")

    rojo = "\033[;31m"
    amarillo = "\033[;33m"
    azul = "\033[;34m"
    cian = "\033[;36m"
    blanco = "\033[;37m"

    i = 0
    largo = len(mat)
    j = 0
    tablero = ""

    while j < largo:
        tablero += cian + "+---"

        j += 1
    
    tablero += "+\n"

    while i < largo:
        j = 0

        while j < largo:
            barco = mat[i][j]
            tablero += cian + "| "

            if barco == 1:
                tablero += azul + "o "
            elif barco == 2:
                tablero += imprimir_barco_doble(mat, i, j, [2, 3, 8, 11], azul)
            elif barco == 3 or barco == 8 or barco == 11:
                tablero += imprimir_barco_doble(mat, i, j, [2], amarillo)
            elif barco == 4:
                tablero += rojo + "o "
            elif barco == 5:
                tablero += imprimir_barco_doble(mat, i, j, [5, 6, 9, 12] , rojo)
            elif barco == 6 or barco == 9 or barco == 12:
                tablero += imprimir_barco_doble(mat, i, j, [5], amarillo)
            elif barco == 7 or barco == 10:
                tablero += amarillo + "* "
            else:
                tablero += "  "
        
            j += 1

        tablero += cian + "|\n"

        j = 0

        while j < largo:
            tablero += cian + "+---"

            j += 1
        
        tablero += "+\n"

        i += 1
    
    return tablero

def imprimir_barco_doble(mat, i, j, barcos, color):
    '''Retorna una barco doble dependiendo de la posición y el jugador'''

    if type(mat) != list or type(i) != int or type(j) != int:
        return "Error01"
    elif type(barcos) != list or type(color) != str:
        return "Error01"

    n = len(mat)
    
    for x in barcos:
        if i-1 >= 0:
            if mat[i-1][j] == x:
                return color + "v "
        if i+1 < n:
            if mat[i+1][j] == x:
                return color + "^ "
        if j-1 >= 0:
            if mat[i][j-1] == x:
                return color + "> "
        if j+1 < n:
            if mat[i][j+1] == x:
                return color + "< "
    
    return "  "
# -------------------------------------------------------------------------------------------------------------------------------------

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

    tablero_nuevo = copiar_tablero(tablero_original) # Se llama a la funcion para que mueva el tablero 
                                                    # pero tomando en cuenta dos tableros, el original y el modificado

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
# -------------------------------------------------------------------------------------------------------------------------------------
def modificar_matriz(matriz):
    numero = len(matriz)  # Número de filas/columnas de la matriz
    
    for i in range(numero):
        for j in range(numero):
            if matriz[i][j] == 8 or matriz[i][j] == 11:
                matriz[i][j] = 3
            elif matriz[i][j] == 9 or matriz[i][j] == 12:
                matriz[i][j] = 6
    
    return matriz

def turnos(tablero, jugadores):
    '''Funcion que determina los turnos del juego'''
    # Cuando uno de los jugadores gane
    while True:
        jugador = 0
        cuenta1 = 0
        cuenta2 = 0
        fila1 = 0
        columna1 = 0
        fila2 = 0
        columna2 = 0
        elimina1 = 0
        elimina2 = 0
        while recorrer_tablero(tablero, jugador) == False:
            print(blanco + "Este es el tablero")
            tablero_imprimir = imprimir_tablero(tablero)
            print(tablero_imprimir)
            print(tablero)
            tablero = mover_barcos(modificar_matriz(tablero))
            if elimina1 > 0:
                tablero = retirar_incendiario(tablero, fila1, columna1)
                elimina1 -= 1
            elif elimina2 > 0:
                tablero = retirar_incendiario(tablero, fila2, columna2)
                elimina2 -= 1

            if cuenta1 > 0:
                tablero = disparo_incendiario_2(tablero, fila1, columna1)[0]
                cuenta1 -= 1
                elimina1 += 1
            elif cuenta2 > 0:
                tablero = disparo_incendiario_2(tablero, fila2, columna2)[0]
                cuenta2 -= 1
                elimina2 += 1
            print(blanco + f"Es el turno de {jugadores[jugador]}")
            disparo = input("Seleccione el tipo de disparo: ")
            if disparo == '1':
                disparar_1 = disparo_1(tablero, jugador)
                tablero = disparar_1
                if jugador == 0:
                    jugador += 1
                else:
                    jugador -= 1
            elif disparo == '2':
                disparar_araña = disparo_araña(tablero, jugador)
                tablero = disparar_araña
                if jugador == 0:
                    jugador += 1
                else:
                    jugador -= 1
            elif disparo == '3':
                disparar_incendiario = disparo_incendiario(tablero, jugador)
                tablero = disparar_incendiario[0]
                if jugador == 0:
                    fila1 = disparar_incendiario[1]
                    columna1 = disparar_incendiario[2]
                    cuenta1 += 1
                    jugador += 1
                else:
                    fila2 = disparar_incendiario[1]
                    columna2 = disparar_incendiario[2]
                    cuenta2 += 1
                    jugador -= 1     
            else:
                print("Numero invalido, selecciona un numero adecuado!")
                break
        print(tablero)
        return f"El jugador {jugadores[jugador]} ha ganado!"
                
                
def condicion_victoria(cantidad_barcos):
    '''Funcion que determina la condicion de victoria'''
    if cantidad_barcos == 0:
        return True
    else:
        return False

def recorrer_tablero(tablero, jugador_actual):
    '''Funcion que recorre el tablero para determinar el ganador'''
    filas = len(tablero)
    columnas = len(tablero[0])
    barcos_jugador_1 = 0
    barcos_jugador_2 = 0
    for i in range(filas):
        for j in range(columnas):
            if tablero[i][j] == 1 or tablero[i][j] == 2:
                barcos_jugador_1+=1
            elif tablero[i][j] == 4 or tablero[i][j] == 5:
                barcos_jugador_2+=1
    if jugador_actual == 0:
        return condicion_victoria(barcos_jugador_1)
    elif jugador_actual == 1:
        return condicion_victoria(barcos_jugador_2)




# -------------------------------------------------------------------------------------------------------------------------------------

def es_entero(texto):
    if len(texto) == 0:
        return False

    if texto[0] == "-":
        texto = texto[1:]

    for elem in texto:
        if ("0" <= elem <= "9") == False:
            return False

    return True

def disparo_1(matriz, turno):
    fila = input("Ingrese el número de fila: ")
    columna = input("Ingrese el número de columna: ")

    if es_entero(fila) == False or es_entero(columna) == False:
        print("Haz puesto una cordenada que invalida, porfavor vuelve a intentarlo")
        return disparo_1(matriz, turno)
    
    fila = int(fila) - 1
    columna = int(columna) - 1

    if fila >= len(matriz) or columna >= len(matriz[0]):
        print("Haz puesto una cordenada que no existe, porfavor vuelve a intentarlo")
        return disparo_1(matriz, turno)
    elif fila < 0 or columna < 0:
        print("Haz puesto una cordenada que no existe, porfavor vuelve a intentarlo")
        return disparo_1(matriz, turno)
    else: 
        disparo = matriz[fila][columna]
        if turno == 0:
            if disparo == 1:
                matriz[fila][columna] = 0
                print("Le has dado a un barco tuyo!")
            elif disparo == 4:
                matriz[fila][columna] = 0
                print("Le has dado a un barco rival!")
            elif disparo == 2:
                matriz[fila][columna] = 3
                print("Le has dado a un barco tuyo!")
            elif disparo == 5:
                matriz[fila][columna] = 6
                print("Le has dado a un barco rival!")
            else:
                print("No le has dado a ningún barco.")
        elif turno == 1:
            if disparo == 1:
                matriz[fila][columna] = 0
                print("Le has dado a un barco rival!")
            elif disparo == 4:
                matriz[fila][columna] = 0
                print("Le has dado a un barco tuyo!")
            elif disparo == 2:
                matriz[fila][columna] = 3
                print("Le has dado a un barco rival!")
            elif disparo == 5:
                matriz[fila][columna] = 6
                print("Le has dado a un barco tuyo!")
            else:
                print("No le has dado a ningún barco.")

    return matriz

# -------------------------------------------------------------------------------------------------------------------------------------

def es_entero(texto):
    if len(texto) == 0:
        return False

    if texto[0] == "-":
        texto = texto[1:]

    for elem in texto:
        if ("0" <= elem <= "9") == False:
            return False

    return True

def disparo_araña(matriz, turno):
    fila = input("Ingrese el número de fila: ")
    columna = input("Ingrese el número de columna: ")

    if es_entero(fila) == False or es_entero(columna) == False:
        print("Has puesto una coordenada inválida, por favor vuelve a intentarlo.")
        return disparo_araña(matriz, turno)

    fila = int(fila) - 1
    columna = int(columna) - 1

    if fila >= len(matriz) or columna >= len(matriz[0]):
        print("Has puesto una coordenada que no existe, por favor vuelve a intentarlo.")
        return disparo_araña(matriz, turno)
    elif fila < 0 or columna < 0:
        print("Has puesto una coordenada que no existe, por favor vuelve a intentarlo.")
        return disparo_araña(matriz, turno)

    disparo = matriz[fila][columna]
    acierto = False

    if turno == 0:
        if disparo == 1 or disparo == 4:
            if disparo == 1:
                print("Le has dado a un barco tuyo en el centro!")
            else:
                print("Le has dado a un barco rival en el centro!")
            matriz[fila][columna] = 0
            acierto = True
        elif disparo == 2:
            matriz[fila][columna] = 3
            print("Le has dado a un barco tuyo en el centro!")
            acierto = True
        elif disparo == 5:
            matriz[fila][columna] = 6
            print("Le has dado a un barco rival en el centro!")
            acierto = True
    else:
        if disparo == 1 or disparo == 4:
            if disparo == 1:
                print("Le has dado a un barco rival en el centro!")
            else:
                print("Le has dado a un barco tuyo en el centro!")
            matriz[fila][columna] = 0
            acierto = True
        elif disparo == 2:
            matriz[fila][columna] = 3
            print("Le has dado a un barco rival en el centro!")
            acierto = True
        elif disparo == 5:
            matriz[fila][columna] = 6
            print("Le has dado a un barco tuyo en el centro!")
            acierto = True

    # Disparar en las casillas en diagonal
    # df es diagonal fila y dc es diagonal columna
    for df, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if 0 <= fila + df < len(matriz) and 0 <= columna + dc < len(matriz[0]):
            if turno == 0:
                if matriz[fila + df][columna + dc] == 1 or matriz[fila + df][columna + dc] == 4:
                    if matriz[fila + df][columna + dc] == 1:
                        print("Le has dado a un barco tuyo en la diagonal!")
                    else:
                        print("Le has dado a un barco rival en la diagonal!")
                    matriz[fila + df][columna + dc] = 0
                    acierto = True
                elif matriz[fila + df][columna + dc] == 5:
                    matriz[fila + df][columna + dc] = 6
                    print("Le has dado a un barco rival en la diagonal!")
                    acierto = True
                elif matriz[fila + df][columna + dc] == 2:
                    matriz[fila + df][columna + dc] = 3
                    print("Le has dado a un barco tuyo en la diagonal!")
                    acierto = True
            else:
                if matriz[fila + df][columna + dc] == 1 or matriz[fila + df][columna + dc] == 4:
                    if matriz[fila + df][columna + dc] == 1:
                        print("Le has dado a un barco rival en la diagonal!")
                    else:
                        print("Le has dado a un barco tuyo en la diagonal!")
                    matriz[fila + df][columna + dc] = 0
                    acierto = True
                elif matriz[fila + df][columna + dc] == 5:
                    matriz[fila + df][columna + dc] = 6
                    print("Le has dado a un barco tuyo en la diagonal!")
                    acierto = True
                elif matriz[fila + df][columna + dc] == 2:
                    matriz[fila + df][columna + dc] = 3
                    print("Le has dado a un barco rival en la diagonal!")
                    acierto = True

    if not acierto:
        print("No le has dado a ningún barco.")

    return matriz

# -------------------------------------------------------------------------------------------------------------------------------------

def es_entero(texto):
    if len(texto) == 0:
        return False

    if texto[0] == "-":
        texto = texto[1:]

    for elem in texto:
        if ("0" <= elem <= "9") == False:
            return False

    return True

def disparo_incendiario(matriz, turno):
    fila = input("Ingrese el número de fila: ")
    columna = input("Ingrese el número de columna: ")

    if es_entero(fila) == False or es_entero(columna) == False:
        print("Has puesto una coordenada inválida, por favor vuelve a intentarlo.")
        return disparo_incendiario(matriz, turno)

    fila = int(fila) - 1
    columna = int(columna) - 1

    if fila >= len(matriz) or columna >= len(matriz[0]):
        print("Has puesto una coordenada que no existe, por favor vuelve a intentarlo.")
        return disparo_incendiario(matriz, turno)
    elif fila < 0 or columna < 0:
        print("Has puesto una coordenada que no existe, por favor vuelve a intentarlo.")
        return disparo_incendiario(matriz, turno)
    
    disparo = matriz[fila][columna]
    acierto = False

    if turno == 0:
        if disparo == 1 or disparo == 4:
            if disparo == 1:
                print("Le has dado a un barco tuyo en el centro!")
            else:
                print("Le has dado a un barco rival en el centro!")
            matriz[fila][columna] = 7
            acierto = True
        elif disparo == 0:
            matriz[fila][columna] = 7
        elif disparo == 5:
            matriz[fila][columna] = 9
            print("Le has dado a un barco rival en el centro!")
            acierto = True
        elif disparo == 2:
            matriz[fila][columna] = 8
            print("Le has dado a un barco tuyo en el centro!")
            acierto = True
    else:
        if disparo == 1 or disparo == 4:
            if disparo == 1:
                print("Le has dado a un barco rival en el centro!")
            else:
                print("Le has dado a un barco tuyo en el centro!")
            matriz[fila][columna] = 7
            acierto = True
        elif disparo == 0:
            matriz[fila][columna] = 7
        elif disparo == 5:
            matriz[fila][columna] = 9
            print("Le has dado a un barco tuyo en el centro!")
            acierto = True
        elif disparo == 2:
            matriz[fila][columna] = 8
            print("Le has dado a un barco rival en el centro!")
            acierto = True

    # Disparar en las casillas en forma de cruz
    for fila_cr, columna_cr in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        fila_cruz = fila + fila_cr
        columna_cruz = columna + columna_cr
        if 0 <= fila_cruz < len(matriz) and 0 <= columna_cruz < len(matriz[0]):
            if turno == 0:
                if matriz[fila_cruz][columna_cruz] == 1 or matriz[fila_cruz][columna_cruz] == 4:
                    if matriz[fila_cruz][columna_cruz] == 1:
                        print("Le has dado a un barco tuyo!")
                    else:
                        print("Le has dado a un barco rival!")
                    acierto = True
                    matriz[fila_cruz][columna_cruz] = 7
                elif matriz[fila_cruz][columna_cruz] == 0:
                    matriz[fila_cruz][columna_cruz] = 7
                elif matriz[fila_cruz][columna_cruz] == 5:
                    matriz[fila_cruz][columna_cruz] = 9
                    print("Le has dado a un barco rival!")
                    acierto = True
                elif matriz[fila_cruz][columna_cruz] == 2:
                    matriz[fila_cruz][columna_cruz] = 8
                    print("Le has dado a un barco tuyo!")
                    acierto = True
            else:
                if matriz[fila_cruz][columna_cruz] == 1 or matriz[fila_cruz][columna_cruz] == 4:
                    if matriz[fila_cruz][columna_cruz] == 1:
                        print("Le has dado a un barco rival!")
                    else:
                        print("Le has dado a un barco tuyo!")
                    matriz[fila_cruz][columna_cruz] = 7
                    acierto = True
                elif matriz[fila_cruz][columna_cruz] == 0:
                    matriz[fila_cruz][columna_cruz] = 7
                elif matriz[fila_cruz][columna_cruz] == 5:
                    matriz[fila_cruz][columna_cruz] = 9
                    print("Le has dado a un barco tuyo!")
                    acierto = True
                elif matriz[fila_cruz][columna_cruz] == 2:
                    matriz[fila_cruz][columna_cruz] = 8
                    print("Le has dado a un barco rival!")
                    acierto = True

    if not acierto:
        print("No le has dado a ningún barco.")

    return [matriz, fila, columna]


def disparo_incendiario_2(matriz, fila, columna):
    # Disparar en las casillas dentro del rango 3x3 alrededor del punto de disparo
    for i in range(fila-1, fila+2):
        for j in range(columna-1, columna+2):
            if 0 <= i < len(matriz) and 0 <= j < len(matriz[0]):
                num_barco = matriz[i][j]
                if num_barco == 1 or num_barco == 4 or num_barco == 7:
                    matriz[i][j] = 10
                elif num_barco == 0:
                    matriz[i][j] = 10
                elif num_barco == 2 or num_barco == 3 or num_barco == 8:
                    matriz[i][j] = 11
                elif num_barco == 5 or num_barco == 6 or num_barco == 9:
                    matriz[i][j] = 12
                else:
                    # No es un número correspondiente a barcos, dejarlo igual
                    matriz[i][j] = num_barco
                    
    print("El fuego se extiende...")

    return [matriz, fila, columna]


def retirar_incendiario(matriz, fila, columna):
    # Devolver el estado incendiario a su estado normal
    for i in range(fila - 1, fila + 2):
        for j in range(columna - 1, columna + 2):
            if 0 <= i < len(matriz) and 0 <= j < len(matriz[0]):
                num_barco = matriz[i][j]
                if num_barco == 10:
                    matriz[i][j] = 0
                elif num_barco == 11:
                    matriz[i][j] = 3
                elif num_barco == 12:
                    matriz[i][j] = 6

    return matriz

res = iniciar_juego()
print(res)

# guardo = disparo_incendiario(tablero, 0)

# print(guardo)

# res = disparo_incendiario_2(guardo[0], guardo[1], guardo[2])
# print (res[0]) 

# res_v2 = retirar_incendiario(res[0], res[1], res[2])
# print(res_v2)