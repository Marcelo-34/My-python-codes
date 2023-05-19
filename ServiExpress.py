from setuptools import find_packages


Salir = False
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
            while patente != "AA1000" and patente != "BBBB10":
                print("Porfavor ingrese la patente(debe contener maximo 6 caracteres, donde hay 2 posibles formatos: AA1000/BBBB10.)")
                patente = str(input())
            
                match patente:
                    case "AA1000":
                        print("Patente registrada")
                    case "BBBB10":
                        print("Patente registrada")
                    case _:
                        print("No se ha ingresado la patente o no esta en nuestros formatos admitidos")
                        print("Intentelo de nuevo")

            while True:
                print("Porfavor ingrese el año de fabricacion (que se encuentre en el rango 1900-2021.)")
                añoF = int(input())

                if añoF >= 1900 and añoF <= 2021:
                    print("Año Registrado") 
                    break
                
                else:
                    print("Año no disponible en nuestro rango admitido")
                
            while True:
                print("Ingrese el tipo de vehiculo (sólo acepta las letras: d/b/e/h (mayúscula y minúscula))")
                Tvehiculo = str(input())

                match Tvehiculo:
                    
                    case "d":
                        print("Tipo de vechiculo registrado")
                        print("Diesel")
                        break
                    case "D":
                        print("Tipo de vechiculo registrado")
                        print("Diesel")
                        break
                    case "b":
                        print("Tipo de vechiculo registrado")
                        print("Bencina")
                        break
                    case "B":
                        print("Tipo de vechiculo registrado")
                        print("Bencina")
                        break
                    case "e":
                        print("Tipo de vechiculo registrado")
                        print("Electrico")
                        break
                    case "E":
                        print("Tipo de vechiculo registrado")
                        print("Electrico")
                        break
                    case "h":
                        print("Tipo de vechiculo registrado")
                        print("Hibrido")
                        break
                    case "H":
                        print("Tipo de vechiculo registrado")
                        print("Hibrido")
                        break
                    case _:
                        print("Tipo de vehiculo no encontrado ")

            while True:
                print("Ingrese la marca de su coche")
                marca = str(input())
                if len (marca) == False:
                    print("No se ha ingresado nada")   
                else: 
                    print("La marca de su auto es:", marca)
                    break
              
            
            while True:
                print("Ingrese el modelo de su coche")
                modelo = str(input())
                if len (modelo) == False:
                    print("No se ha ingresado nada") 
                else:
                    print("El modelo de su auto es:", modelo)
                    break
                
                    
                    
            print("Su registro ha sido completado")
            print("Volviendo al menu...")

        case 2:
            if patente == False:
                print("Su carro no se encuentra registrado")
            else:
                
                print("Bienvenido al Registro de su Mantenimiento")
                while True:
                    print("Ingrese la patente de su coche para ver si esta registrada")
                    verificacion = str(input())
                    if verificacion == (patente):    
                        print("Su carro esta registrado")
                        break
                    else:
                        print("Patente incorrecta")
                    

               


                print("Porfavor ingrese la fecha que quiera realizar la mantencion")
                while True:
                    print("Ingrese dia (Solo numero)")
                    dia = int(input())
                    if dia <= 31:
                        print("Dia registrado")
                        break
                    else:
                        print("Ese dia no existe, intente de nuevo")

                while True:    
                    print("Ingrese el mes (Solo numero)")
                    mes = int(input())
                    if mes <= 12:
                        print("Registrado")
                        break
                    elif mes > 12:
                        print("Ese mes no existe, intente de nuevo")

                print("Su fecha registrada es:", dia, mes,"2022")
                print("Volviendo al menu...")

        case 3:
            if patente == False:
                print("Su carro no se encuentra registrado")
            elif dia == False:
                print("No ha agendado su fecha en la opcion 2")
            else:
                print("Bienvenido a la opcion de consulta")
                while True:
                    print("Ingrese la patente de su coche para ver si esta registrada")
                    verificacion = str(input())
                    if verificacion == (patente):    
                        print("Su carro esta registrado")
                        break
                    else:
                        print("Su carro no se encuentra registrado")

                  
                
                print("La patente de su coche es:", patente)
                print("---------------------------------------------")
                print("El año de fabricacio de su coche es:", añoF)
                print("---------------------------------------------")
                print("Su tipo de vehiculo es:", Tvehiculo)
                print("---------------------------------------------")
                print("La marca de su coche es:", marca)
                print("---------------------------------------------")
                print("El modelo de su coche es:", modelo)
                print("---------------------------------------------")
                print("Su fecha registrada es:", dia, mes,"2022")
                print("---------------------------------------------")
                print("Esa es toda la informacion registrada")
                print("---------------------------------------------")
                print("Volviendo al menu...")

        case 4:
            Salir = True
            print("----Gracias por usar ServiExpress----")
        
        case _:
            print("Esa opcion es inexistente")



            

                


            
            
                
            
            
      

        
                



                