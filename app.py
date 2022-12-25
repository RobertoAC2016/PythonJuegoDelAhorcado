import random, os

# El juego del ahorcado en codigo Python

def juego():
    print("Juego del ahorcado")
    ##Seguimos con  la BDs de palabras y despues las imagenes o en este caso las listas de caracteres ascii
    #Usare una lista de palabras para el jeugo de 10
    #Usare lenguajes de programacion
    db = [
        "c",
        "javascript",
        "java",
        "php",
        "python",
        "go",
        "perl",
        "shell",
        "dart",
        "typescript",
    ]
    ## Ahora la BDs de imagenes
    #En total deben ser 7 imagenes
    IMAGES = [
        '''
        ========= 
          +---+
          |   |
              |
              |
              |
              |
        =========
        ''', '''
        =========
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
        =========
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
        =========
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
        =========
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
        =========
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
        =========
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
    ]
    # 7 imagenes son igual a 7 intentos maximo, creare la variable intentos
    tries = 6   # es 6 porque los arreglos tienen indice 0 y maximo es igual a la longitud - 1 = 7 -1 -> 6
    #Usare la libreria radom para seleccionar una palabra y en base a la cantidad de caracteres se generaran los espacios para cada palabra

    word = random.choice(db)    # la libraria random tiene la funcion choise q selecciona aleatoriamente un elemento de una lista
    # ahora a generar la DB de espacios segun la palabra seleccionado
    spaces = ["_"] * len(word)
    
    #empezamos por el ciclo q esta pidiendo la letra al usuario hasta q se terminen los intentos
    while True:
        # Aqui debo limpiar la pantalla para cada vez q se realiza el ciclo
        os.system("cls")
        #a dibujar los espacios a rellenar por el usuario con cada letra
        for caracter in spaces:
            print(caracter, end=" ")
        #dibujare la imagen a segun el numero de intento q llevamos q en este caso es el primer intento de 7
        print(IMAGES[tries])
        # a Solicitar la letra al usuario por medio del teclado
        letra = input("Escribe una letra: ")
        
        letraencontrada = False
        for idx, caracter in enumerate(word):
            if caracter == letra:
                # Si la letra q introdujo el usuario es igual a la q contiene la palabra se sustituye en la lista de espacios
                spaces[idx] = letra
                letraencontrada = True
                # Esto pasara hasta q se complete la palabra o el numero de intentos haya pasado
                
        # Dicho lo anterior, restamos un intento al numero de intentos, si es q no se encontro la letra dentro de la palabra
        if not letraencontrada:
            tries -= 1
            
        # Si ya no hay espacios, entonces has ganado
        if "_" not in spaces:
            os.system("cls")
            print("GANASTE")
            break
        
        # Si aun no ganas y el numero de intentos ya llego a cero  entonces, perdiste
        if tries == 0:
            os.system("cls")
            print("PERDISTE")
            break


# empezamos por el main
if __name__ == "__main__":
    juego()