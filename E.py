sw = 1
while sw == 1:
    print("1. Opcion 1")
    print("2. Opcion 2")
    print("3. Salir")
    op = int(input("Seleccione una opcion: "))
    try:
        if (op > 0 and op < 4):
            if op == 1:
                print("Ha seleccionado la opcion 1")
                continu=int(input("Desea salir 1= Si 2=No: "))
                if continu == 1:
                    print("Adios")
                    sw = 0
            if op == 2:
                print ("Ha seleccionado la opcion 2")
                continu=int(input("Desea salir 1= Si 2=No: "))
                if continu == 1:
                    if continu == 1:
                        print("Adios")
            if op == 3:
                print("Usted desea salir del menu")
                sw = 0
    except:
        print("Ingreso erroneo")
