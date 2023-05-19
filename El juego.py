print("Bienvenido a este jueguito pedorro de matematicas ;3")
print("Porfavor eliga con que operaciones quiere jugar como jugo ella conmigo")

Salir = 0
respuesta = 0

while (Salir != 1):
    print("1. Sumas")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

    opc = int(input())

    if opc == 1:
        print("Bienvenido al juego de la suma o la sumame esta coño")
        print("Resuelva los siguientes ejercicios: ")

        print("Ejercicio 1: 15 + 25")
        respuesta =int(input())
        while (respuesta != 40):
            print("Incorrecto, Intente de nuevo")
        else:
            print("Correcto, pasando a")