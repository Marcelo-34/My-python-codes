from tkinter.ttk import Menubutton


menu1=1000000
menu2=1500000
menuA1=1800000
menuB2=2300000
menuC1=3500000
menuC2=4000000
postre=500000

print("*"*50)
print("Bienvenido al sistema de Food and Dance")
print("Los precios variaran dependiendo la cantidad de asistentes")
print("*"*50)
    
print("Ingrese la cantidad de ingrantes: ")
cantAS = int(input())

if cantAS <= 50:
    print("*"*50)
    print("Seleccione su menu: ")
    print("Menu1 = ",menu1)
    print("Menu2 = ",menu2)
    print("Opcional: Agregar postre = ",postre)
    print("*"*50)
    print()

    print("Que opcion de menu desea (1 o 2): ")
    op = int(input())
    print("Desea postre? (s/n)")
    opPos = str(input())

    if op == 1 and opPos == "n":
        total = menu1

        print("*"*50)
        print("Eventos Food and Dance")
        print()
        print("Hasta 50 personas:",menu1, "Seleccionado" )
        print("Postre: No = $0")
        print("Total a pagar es: $",total)
        print("Gracias por preferir nuestro servicio")
        print("*"*50)

    
    elif op == 1 and opPos == "s":
            totalconPos = menu1 + postre

            print("*"*50)
            print("Eventos Food and Dance")
            print()
            print("Hasta 50 personas:",menu1, "Seleccionado" )
            print("Postre: Si = $",postre)
            print("Total a pagar es: $",totalconPos)
            print("Gracias por preferir nuestro servicio")
            print("*"*50)

    elif op == 2 and opPos == "n":
            total = menu2

            print("*"*50)
            print("Eventos Food and Dance")
            print()
            print("Hasta 50 personas:",menu2, "Seleccionado" )
            print("Postre: No = $0")
            print("Total a pagar es: $",total)
            print("Gracias por preferir nuestro servicio")
            print("*"*50)
            
    elif op == 2 and opPos == "s":
            TotalconPos = menu2 + postre

            print("*"*50)
            print("Eventos Food and Dance")
            print()
            print("Hasta 50 personas:",menu2, "Seleccionado" )
            print("Postre: Si = $",postre)
            print("Total a pagar es: $",TotalconPos)
            print("Gracias por preferir nuestro servicio")
            print("*"*50)

if cantAS > 50 and cantAS <= 100:
    print("*"*50)
    print("Seleccione su menu: ")
    print("Menu1 = ",menuA1)
    print("Menu2 = ",menuB2)
    print("Opcional: Agregar postre = ",postre)
    print("*"*50)
    print()

    print("Que opcion de menu desea (1 o 2): ")
    op = int(input())
    print("Desea postre? (s/n)")
    opPos = str(input())

    if op == 1 and opPos == "n":
        total = menuA1
        print("*"*50)
        print("Eventos Food and Dance")
        print()
        print("Hasta 100 personas:",menuA1, "Seleccionado" )
        print("Postre: No = $0",)
        print("Total a pagar es: $",total)
        print("Gracias por preferir nuestro servicio")
        print("*"*50)

    elif op == 1 and opPos == "s":
        TotalconPos2 = menuA1 + postre

        print("*"*50)
        print("Eventos Food and Dance")
        print()
        print("Hasta 100 personas:",menuA1, "Seleccionado" )
        print("Postre: Si = $",postre)
        print("Total a pagar es: $",TotalconPos2)
        print("Gracias por preferir nuestro servicio")
        print("*"*50)

    elif op == 2 and opPos == "n":
        total = menuB2

        print("*"*50)
        print("Eventos Food and Dance")
        print()
        print("Hasta 100 personas:",menuB2, "Seleccionado" )
        print("Postre: No = $0",)
        print("Total a pagar es: $",total)
        print("Gracias por preferir nuestro servicio")
        print("*"*50)

    elif op == 2 and opPos == "s":
        totalconPos3 = menuB2 + postre

        print("*"*50)
        print("Eventos Food and Dance")
        print()
        print("Hasta 100 personas:",menuB2, "Seleccionado" )
        print("Postre: Si = $",postre)
        print("Total a pagar es: $",totalconPos3)
        print("Gracias por preferir nuestro servicio")
        print("*"*50)

if cantAS > 100 and cantAS <= 200:
        print("*"*50)
        print("Seleccione su menu: ")
        print("Menu1 = ",menuC1)
        print("Menu2 = ",menuC2)
        print("Opcional: Agregar postre = ",postre)
        print("*"*50)
        print()

        print("Que opcion de menu desea (1 o 2): ")
        op = int(input())
        print("Desea postre? (s/n)")
        opPos = str(input())

        if op == 1 and opPos == "n":
                total = menuC1
        
                print("*"*50)
                print("Eventos Food and Dance")
                print()
                print("Hasta 200 personas:",menuC1, "Seleccionado" )
                print("Postre: No = $0",)
                print("Total a pagar es: $",total)
                print("Gracias por preferir nuestro servicio")
                print("*"*50)

        elif op == 1 and opPos == "s":
                TotalconPos4 = menuC1 + postre

                print("*"*50)
                print("Eventos Food and Dance")
                print()
                print("Hasta 200 personas:",menuC1, "Seleccionado" )
                print("Postre: Si = $",postre)
                print("Total a pagar es: $",TotalconPos4)
                print("Gracias por preferir nuestro servicio")
                print("*"*50)

        elif op == 2 and opPos == "n":
                total = menuC2

                print("*"*50)
                print("Eventos Food and Dance")
                print()
                print("Hasta 200 personas:",menuC2, "Seleccionado" )
                print("Postre: No = $0")
                print("Total a pagar es: $",total)
                print("Gracias por preferir nuestro servicio")
                print("*"*50)

        elif op == 2 and opPos == "s":
                TotalconPos5 = menuC2 + postre

                print("*"*50)
                print("Eventos Food and Dance")
                print()
                print("Hasta 200 personas:",menuC2, "Seleccionado" )
                print("Postre: Si = $", postre)
                print("Total a pagar es: $",TotalconPos5)
                print("Gracias por preferir nuestro servicio")
                print("*"*50)








        


        



        








