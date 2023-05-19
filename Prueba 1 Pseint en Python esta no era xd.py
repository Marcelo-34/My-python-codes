menu1=1000000
menu2=1500000
menuA1=1800000
menuB2=2300000
menuC1=3500000
menuC3=4000000
postre=500000
cantAS = 0



print("*"*30)
print("Bienvenido al sistema de Food and Dance")
print("Los precios variaran dependiendo la cantidad de asistentes")
print("*"*30)
    
print("Ingrese la cantidad de ingrantes: ")
int(input())

if cantAS <= 50:
    print("*"*10)
    print("Seleccione su menu: ")
    print("Menu1 = ",menu1)
    print("Menu2 = ",menu2)
    print("Opcional: Agregar postre = ",postre)
    print("*"*10)
    print()

    print("Que opcion de menu desea (1 o 2): ")
    op = int(input())
    print("Desea postre? (s/n)")
    opPos = str(input())

    if op == 1 and opPos == "n":
        total = menu1

        print("*"*10)
        print("Eventos Food and Dance")
        print()
        print("Hasta 50 personas:",menu1, "Seleccionado" )
        print("Postre: No = $0")
        print("Total a pagar es: $",total)
        print("Gracias por preferir nuestro servicio")
        print("*"*10)

    else:
        if op == 1 and opPos == "s":
            totalconPos = menu1 + postre

        print("*"*10)
        print("Eventos Food and Dance")
        print()
        print("Hasta 50 personas:",menu1, "Seleccionado" )
        print("Postre: Si = $",postre)
        print("Total a pagar es: $",totalconPos)
        print("Gracias por preferir nuestro servicio")
        print("*"*10)

    if op == 2 and opPos == "n":
        total = menu2

        print("*"*10)
        print("Eventos Food and Dance")
        print()
        print("Hasta 50 personas:",menu2, "Seleccionado" )
        print("Postre: No = $0")
        print("Total a pagar es: $",total)
        print("Gracias por preferir nuestro servicio")
        print("*"*10)
    else:
        if op == 2 and opPos == "s":
            TotalconPos2 = menu2 + postre

        print("*"*10)
        print("Eventos Food and Dance")
        print()
        print("Hasta 50 personas:",menu2, "Seleccionado" )
        print("Postre: Si = $",postre)
        print("Total a pagar es: $",TotalconPos2)
        print("Gracias por preferir nuestro servicio")
        print("*"*10)

        








