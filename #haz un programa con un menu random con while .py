#haz un programa con un menu random, solamente que muestre 4 opciones siendo la 4 la de salir, 
#al elegir cada opcion debe mostrarte un mensaje que elegiste x opcion,
#y al seleccionar la 4 el programa terminara, 
#pero al escribir una opcion que no sea las anteriores debes mostrar un mensaje de error, regresando al menu

Salir = 0

op = 0
while (Salir != 1):
        print("Bienvenido a ete menu random")
        print("1.Opcion 1")
        print("2.Opcion 2")
        print("3.Opcion 3")
        print("4.Opcion 4")

        try:
            op = int(input())
        except:
            print("Mensaje de error") 

        if op == 1:
            print("Usted ha seleccionado la opcion 1")
        elif op == 2:
            print("Usted ha seleccionado la opcion 2")
        elif op == 3:
            print("Usted ha seleccionado la opcion 3")
        elif op == 4:
            Salir = 1
            print("Adios")

        else:
            print("Error")
            print("Volviendo al menu...")  


