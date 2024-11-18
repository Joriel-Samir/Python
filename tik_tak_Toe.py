tablero = [[" "," "," "],
            [" "," "," "],
            [" "," "," "]]

jugadores = ["x","o"]

def mostrar_tablero():

    for i in tablero:
        print(i)

def insertar_elementos(fila, columna, contadora1= 0):

    while True:
        for i in range(len(tablero)):
            for j in range(len(tablero)):
                if i == fila and j == columna:
                    if tablero[i][j] != " ":
                        print(f"Tiene que estar vacia cabezon. Turno actual {jugadores[contadora1]}")
                        fila = int(input("Que fila va a escoger(0-2): "))
                        columna = int(input("Que columna va a escoger(0-2): "))
                    else:
                        tablero[i][j] = jugadores[contadora1]
                        return False
                        break

                
def identificar_ganador():
    
    if tablero[0] == ["x","x","x"] or tablero[1] == ["x","x","x"] or tablero[2] == ["x","x","x"]:
        print("Ha ganado la x")
        return False
    elif tablero[0] == ["o","o","o"] or tablero[1] == ["o","o","o"] or tablero[2] == ["o","o","o"]:
        print("Ha ganado la o")
        return False
    elif tablero[0][0] == "x" and tablero[1][1] == "x" and tablero[2][2] == "x":
        print("Ha ganado la x")
        return False
    elif tablero[0][2] == "x" and tablero[1][1] == "x" and tablero[2][0] == "x":
        print("Ha ganado la x")
        return False
    elif tablero[0][0] == "o" and tablero[1][1] == "o" and tablero[2][2] == "o":
        print("Ha ganado la o")
        return False
    elif tablero[0][2] == "o" and tablero[1][1] == "o" and tablero[2][0] == "o":
        print("Ha ganado la o")
        return False
    elif tablero[0][0] == "x" and tablero[1][0] == "x" and tablero[2][0] == "x":
        print("Ha ganado la x")
        return False
    elif tablero[0][0] == "o" and tablero[1][0] == "o" and tablero[2][0] == "o":
        print("Ha ganado la o")
        return False

def empate(empate1):
    empate1 = True
    for i in tablero:
        for j in i:
            if j == " ": 
                empate1 = False
    if empate1 == True:
        print("Hay un empate")
        return empate1
    
def juego(fila, columna,empate1): 
  contadora = 0
  while True: 
    mostrar_tablero()
    for i in range(len(jugadores)):
        if i+1 == 1:
            print("Turno de la x")
            fila = int(input("Que fila va a escoger(0-2): "))
            columna = int(input("Que columna va a escoger(0-2): "))
            while fila < 0 or fila > 2 or columna < 0 or columna > 2 :
                print("Has escogido una posicion fuera del rango ")
                fila = int(input("Que fila va a escoger(0-2): "))
                columna = int(input("Que columna va a escoger(0-2): "))
            insertar_elementos(fila, columna, contadora1 = 0)
            empate(empate1)
            if empate(empate1) == True:
                contadora = 9
                break
        elif i+1 == 2:
            print("Turno de la o")
            fila = int(input("Que fila va a escoger(0-2): "))
            columna = int(input("Que columna va a escoger(0-2): "))
            while fila < 0 or fila > 2 or columna < 0 or columna > 2 :
                print("Has escogido una posicion fuera del rango ")
                fila = int(input("Que fila va a escoger(0-2): "))
                columna = int(input("Que columna va a escoger(0-2): "))
            insertar_elementos(fila, columna, contadora1 = 1)
            empate(empate1)
            if empate(empate1) == True:
                contadora = 9
                break
    
        
    if identificar_ganador() == False:
        contadora = 9
        break
    else: 
        identificar_ganador()
        pass

juego(fila= 0, columna= 0,empate1=False)
        

