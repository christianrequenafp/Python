import random

def menu():
    while True:
        print('Bienvenido a una Gameroom en Python!')
        print("1. Adivina el numero")
        print("2. Piedra papel o tijera")
        print("3. El ahorcado")
        print("4. Sal del juego")

        opcion = input("Selecciona un juego o sal (opcion 4) : ")

        if opcion == "1":
            adivina_numero()
        elif opcion == "2":
            piedra_papel_tijera()
        elif opcion == "3":
            ahorcado()
        elif opcion == "4":
            break
        else:
            print("Opcion no valida! Seleciona entre el 1 y 4")

    

def adivina_numero():
    numSecreto = random.randint(1, 10)
    intentos = 3
    print("Adivina un numero entre 1 y 10, tienes 3 intentos.")
    while intentos > 0:
        try:
            numUsuario = int(input("Introduce tu numero: "))
            if numUsuario < 1 or numUsuario > 10:
                print("Introduce un numero valido entre 1 y 10.")
                continue
            if numUsuario == numSecreto:
                print("Has adivinado el numero!")
                print()
                return
            elif numUsuario < numSecreto:
                print("El numero es mas grande.")
            else:
                print("El numero es mas pequeño.")
            intentos -= 1
        except ValueError:
            print("Tiene que ser un numero!!!.")
    print(f"Lo siento! El numero era {numSecreto}.")

def piedra_papel_tijera():
    opciones = ['piedra','papel','tijera']
    puntUsuario = 0
    puntMaquina = 0
    
    while puntUsuario < 3 and puntMaquina < 3:
            usuario = input("Escoge entre piedra, papel o tijera: ")
            if usuario not in opciones:
                print("Opcion no valida. Introduce piedra, papel o tijera")
                continue
            maquina = random.choice(opciones)
            print(f"La maquina ha sacado: {maquina}")
            if usuario == maquina:
                print("Empate!")
            elif (usuario == "piedra" and maquina == "tijera") or \
                (usuario == "papel" and maquina == "piedra") or \
                (usuario == "tijera" and maquina == "papel"):
                print("Has ganado el punto!")
                puntUsuario+=1
            else:
                print("La maquina gana el punto, mala suerte")
                puntMaquina+=1
            print(f"Marcador de la partida - Tu: {puntUsuario} vs Maquina: {puntMaquina}")
        
    if puntUsuario == 3:
        print("Enhorabuena, has ganado la partida!")
    else:
        print("Mas suerte la proxima, la maquina gana la partida")

def mostrar_tablero(palabra, aciertos):
    tablero = ""
    for letra in palabra:
        if letra in aciertos:
            tablero += letra + " "
        else:
            tablero += "_ "
    print("Tablero: " + tablero.strip())

def ahorcado():
    try:
        with open("palabras.txt", "r", encoding="utf-8") as fichero:
            palabras = fichero.read().splitlines()
    except FileNotFoundError:
        print("Fichero de palabras no encontrado. ¿El fichero existe?")
        return

    palabra_secreta = random.choice(palabras)
    intentos = len(palabra_secreta) * 2
    aciertos = set()
    errores = set()

    print(f"Bienvenido al ahorcado! Tu palabra tiene {len(palabra_secreta)} letras.")

    while intentos > 0 and palabra_secreta != 0:
        mostrar_tablero(palabra_secreta, aciertos)
        letra = input("Introduce una letra: ").lower()

        if letra in palabra_secreta:
            aciertos.add(letra)
            if all(l in aciertos for l in palabra_secreta):
                print(f"Felicidades! Has adivinado la palabra: {palabra_secreta}")
                return
        else:
            errores.add(letra)
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        if len(letra) > 1:
            if letra == palabra_secreta:
                aciertos = list(palabra_secreta)
                palabra_secreta = 0
                break
            else:
                intentos -= 1
                print(f"Incorrecto! Te quedan {intentos} intentos.")
        

        if letra in aciertos or letra in errores:
            print("Esta letra ya la has dicho antes!")
            continue

    if aciertos == list(palabra_secreta):
        print(f"Felicidades! Has adivinado la palabra: {palabra_secreta}")
    else:
        print(f"Lo siento! Has perdido, la palabra era: {palabra_secreta}")
    

    print(f"Lo siento, has perdido! La palabra era: {palabra_secreta}")
    
menu()