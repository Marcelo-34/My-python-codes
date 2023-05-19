#Crear un menu con las siguientes opciones:
#1. Grabar
#2. Buscar
#3. Imprimir
#4. Salir
from turtle import end_fill


NiF = 0

while True:

    print("Bienvenido al sistema de registro ciudadano.")
    print("Seleccione una de las siguientes opciones: ")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir")
    print("4. Salir")
    menu_op = int(input())

    if(menu_op==0 or menu_op>4):
     print("Esa opcion no existe.")
 
    if (menu_op == 1):
     print("Ingrese su nombre: ")
     nombre = input()
     print("Ingrese su Nif (Sin guion y letras): ")
     NiF=(int(input()))

    if(NiF>99999999):

     print("Excede los limites de nuestro sistema")
     print()
     print("Regresando al Menu...")

     print("Ingrese su edad: ")
     edad = int(input())

    if (menu_op == 2):
     print("Para buscar su registro")
     print("Ingrese su NiF: ")
     int(input())

    if (NiF == 0):
     print("Usted no esta registrado en el sistema: ")

    else:
     print("Informacion encontrada: ")
     print(nombre)
     print(edad)
     print(NiF)
     print("Es toda la informacion disponible")

    
    if menu_op == 3:
     print("Seleccione una de las siguientes opciones para imprimir: ")
     print("1. Certificado de nacimiento")
     print("2. Estado conyugal")
     print("3. Pertenencia a la Union Europea")
     print("4. Salir")
     menu_cert = int(input())
     if menu_cert == 1:
      print("Ingrese su fecha de nacimiento: ")
      fechaN = int(input())
      print("Usted pertenece a la Union Europea?: ")

    else:
        menu_op == 4
        print ("Gracias por usar nuestrop sistema :")
    

        







   
    


 



    
        
  
    


    
    

    
