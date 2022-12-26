import os

def programa():
    os.system("cls")
    while True:
        print("Menu principal\n")
        print("Opcion 1 suma")
        print("Opcion 2 resta")
        print("Opcion 3 divicion")
        print("Opcion 4 multiplicacion")
        print("Salir = s o S")
        print("\n")
        key = input("Elige una opcion: ")
        os.system("cls")
        if key == "1":
            operacion1()
        elif key == "2":
            operacion2()
        elif key == "3":
            operacion3()
        elif key == "4":
            operacion4()
        elif key == "s" or key == "S":
            break
        else:
            print("Opcion no valida")
    print("Programa terminado")
    

def operacion1():
    suma = 3 + 4
    print(f"Se ejecuto la operacion de la opcion suma: {suma}")

    
def operacion2():
    resta = 9 - 5
    print(f"Se ejecuto la operacion de la opcion resta: {resta}")

    
def operacion3():
    div = 8 / 2
    print(f"Se ejecuto la operacion de la opcion division: {div}")

    
def operacion4():
    mul = 5 * 8
    print(f"Se ejecuto la operacion de la opcion multiplicacion: {mul}")


if __name__ == "__main__":
    programa()