Salir = False
formato = False
patente = False
marca = False
modelo = False
opcion = False
dia = False


print("---Bienvenido a este sistema de ServiExpress---")

print("---Menu---")
print("---Que opcion desea elegir---")
while Salir!=True:
    print("1. Registrar Automovil")
    print("2. Registro Mantenimiento")
    print("3. Consultar Automovil")
    print("4. Salir")
    try:
        opcion = int(input())
    except:
        print("No se ingresan letras o no ingresaste nada")
    
    match opcion:

        case 1:
            print("Bievenido al registro de su automovil")
            while formato != "AA" and formato != "BBBB":
                print("De que formato es su patente (Solo se admite AA o BBBB)")
                formato = str(input())

                match formato:

                    case "AA":
                        print("Formato registrado")
                        while True:
                            print("Usted ha seleccionado el formato AA, solo puede ingresar 4 numeros")
                            numpatente = int(input())

                            if numpatente > (9999):
                                print("Ha excedido el limite intente de nuevo")
                            else:
                                print("Numero de patente registrada")
                                print("Su patente es:", formato,numpatente)
                                break

                    case "BBBB":
                        print("Formato registrado")
                        while True:
                            print("Usted ha seleccionado el formato BBBB, solo puede ingresar 2 numeros")
                            numpatente = int(input())

                            if numpatente > (99):
                                print("Ha excedido el limite intente de nuevo")
                            else:
                                print("Numero de patente registrada")
                                print("Su patente es:", formato,numpatente)
                                break


                    case _:
                        print("No se ha ingresado la patente o no esta en nuestros formatos admitidos")
                        print("Intentelo de nuevo")
            
            
                
        

                

            
