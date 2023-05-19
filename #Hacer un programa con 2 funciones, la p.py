#Hacer un programa con 2 funciones, la primera funcion para registrar datos, donde te preguntara tu nombre apellido y edad. 
#Una segunda funcion donde mostraras los datos antes mencionados verificando primero que hayas ingresado 
#algun dato sino mostrara el mensaje que no has ingresado datos aun.
#Un menu en la funcion principal donde tengas 2 opciones la de ingresar y mostrar datos y una 3 de salir.
#Tratando de evitar errores si ingresas una letra al escoger una opcion

def registro():
    global nombre, apellido, edad
    print("Porfavor ingrese su nombre")
    nombre = str(input())
    print("Ingrese su apellido")
    apellido = str(input())
    print("Ingrese su edad")
    edad = int(input())

def verificar():
    if nombre == False:
        print("Usted no ha ingresado nada")
    else:
        print("Su nombre es:", nombre)
        print("Su apellido es:", apellido)
        print("Tienes la edad de", edad,"Años")

nombre = False
apellido = False
edad = False

while True:
    print("Seleccione una opcion")
    print("1. Registrar")
    print("2. Verificar")
    print("3. Salir")
    op = int(input())

    if op == 1:
        registro()

    elif op == 2:
        verificar()
    
    elif op == 3:
        print("Adios")
        break
            
    

