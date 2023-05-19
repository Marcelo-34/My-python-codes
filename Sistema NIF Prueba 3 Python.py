#Formatos del nif
#La estructura del NIF en España, es la siguiente: 
#99999999-RTX 
#03034567-XXY 
#12312345-CCU 
#00000001-03F 

def grabar():
    global nif,nombre,edad,unioneu,sexo,lugarnaci,dianaci,mesnaci,añonaci,resptaestado,Dveri
    print("Bievenido a la opcion de grabar su informacion")
    while Dveri !="RTX" or Dveri !="XXY" or Dveri != "CCU" or Dveri != "03F":
        print("Porfavor ingrese en que formato termina su NIF (RTX, XXY, CCU, 03F)")
        Dveri = str(input())

        match Dveri:

            case "RTX":
                print("Digitos verificados")
                break
            case "XXY":
                print("Digitos verificados")
                break
            case "CCU":
                print("Digitos verificados")
                break
            case "03F":
                print("Digitos verificados")
                break
            case _:
                print("No ingreso o nada o sus digitos son incorrectos, intente de nuevo")

    while True:
        print("Ingrese los numeros de su NIF")
        nif = str(input())
        if len (nif) == 9:
            print("Numero de NIF registrado")
            print("Su NIF es:", nif,Dveri)
            break
        else:
            print("Sobrepaso el limite de caracteres o son insuficientes")

    while True:
        print("Ingrese su nombre")
        nombre = str(input())
        if len (nombre) <= 8:
            print("Su nombre ha sido registrado")
            break
        else:
            print("Sobrepaso el limite de caracteres, intete de nuevo")
    
    while True:
        print("Ingrese su edad")
        edad = int(input())
        if edad >= 0:
            print("Edad registrada")
            break

        else:("Tu edad es incorrecta o ingreso un numero negativo")

    while True:
        print("ingrese su genero")
        sexo = str(input())

        match sexo:

            case "Hombre":
                print("Genero registrado")
                break
            case "Masculino":
                print("Genero registrado")
                break
            case "Mujer":
                print("Genero registrado ")
                break
            case "Femenino":
                print("Genero registrado ")
                break
            case _:
                print("No se ha ingresado el genero, intente de nuevo")

    while True:
        print("Ingrese su fecha de nacimiento")
        print("Ingrese el dia")
        dianaci = int(input())
        if dianaci <= 31:
            print("Dia registrado")
            break
        else:
            print("Dato mal ingresado")

    while True:    
        print("Ingrese el mes")
        mesnaci = int(input())
        if mesnaci <= 12:
            print("Mes registrado")
            break
        else:
            print("Dato mal ingresado")

    while True:    
        print("Ingrese su año de nacimiento")
        añonaci = int(input())
        if añonaci <= 2022:
            print("Año registrado")
            print(dianaci,mesnaci,añonaci)
            break
        else:
            print("Dato mal ingresado")
    
    while True:
        print("Es usted soltero o casado")
        resptaestado = str(input())

        match resptaestado:

            case "Soltero":
                print("Estado registrado")
                break
            case "Casado":
                print("Estado registrado")
                break
            case _:
                print("No se ha espcificado, intente de nuevo")
    
    while True:
        print("Donde nacio usted")
        lugarnaci = str(input())
        if lugarnaci == False:
            print("Usted no ha ingresado nada")
        else:
            print("Lugar registrado")
            break

    while True:
        print("Usted pertenece a la union europea? (Si o no)")
        unioneu = str(input())
        
        match unioneu:

            case "Si":
                print("Usted pertenece a la union europea")
                break
            case "No":
                print("Usted no pertenece la union europea")
                break
            case _:
                print("Usted no ha ingresado si pertence o no, o ingreso un dato incorrecto")

def buscar():
    if nif == False:
        print("Usted no esta ingresado en el sistema")
    else: 
        print("Bienvenido a la opcion de busqueda de su persona")   
        while True:
            print("Porfavor ingrese los numeros de su NIF para verificar")
            verificacionnif = str(input())
            if verificacionnif == nif:
                print("Su informacion hasta el momento es: ")
                print("Su nombres es:", nombre)
                print("Su edad es:", edad)
                print("Su NIF completo es:", nif,Dveri ) 
                print("Pertenencia la union europea:", unioneu) 
                break
            else:
                print("Sobrepaso el limite de caracteres")

def imprimircertificado():
    print("Porfavor escoja el certificado que desea imprimir")
    print("1. Certificado de nacimiento ")
    print("2. Estado conyugal")
    print("3. Pertenencia a la Unión Europea")
    opc = int(input())

    match opc:

        case 1:
            if (nif == False):
                print("Usted no esta ingresado en el sistema")
            else:
                while True:
                    print("Ingrese los numeros de su NIF")
                    verificacionnif = str(input())
                    if verificacionnif == nif:
                        print("CERTIFICADO DE NACIMIENTO")
                        print("-------------------------------")
                        print("Su nombres es:", nombre)
                        print("-------------------------------")
                        print("Su edad es:", edad)
                        print("-------------------------------")
                        print("Su NIF completo es:", nif,Dveri ) 
                        print("-------------------------------")
                        print("Nacio en:", lugarnaci) 
                        print("-------------------------------")
                        print("Fecha de nacimiento:", dianaci,mesnaci,"del",añonaci)
                        print("-------------------------------")
                        print("Su genero es:", sexo)
                        break
                    else:
                        print("Ese NIF no esta registrado")

        case 2:
            if (nif == False):
                print("Usted no esta ingresado en el sistema")
            else:
                while True:
                    print("Ingrese los numeros de su NIF")
                    verificacionnif = str(input())
                    if verificacionnif == nif:
                        print("Su nombres es:", nombre)
                        print("-------------------------------")
                        print("Su edad es:", edad)
                        print("-------------------------------")
                        print("Su NIF completo es:", nif,Dveri )
                        print("-------------------------------")
                        print("Fecha de nacimiento:", dianaci,mesnaci,"del",añonaci)
                        print("-------------------------------")
                        print("Su genero es:", sexo)
                        print("-------------------------------")
                        print("Estado de ciudadano:", resptaestado)
                        break
                    else:
                        print("Ese NIF no esta registrado")
        
        case 3:
            if (nif == False):
                print("Usted no esta ingresado en el sistema")
            else:
                while True:
                    print("Ingrese los numeros de su NIF")
                    verificacionnif = str(input())
                    if verificacionnif == nif:
                        print("Su nombres es:", nombre)
                        print("-------------------------------")
                        print("Su edad es:", edad)
                        print("-------------------------------")
                        print("Su NIF completo es:", nif,Dveri)
                        print("-------------------------------")
                        print("Su genero es:", sexo)
                        print("-------------------------------")
                        print("Estado de ciudadano:", resptaestado)
                        print("-------------------------------")
                        print("Pertenencia a la union europea: ", unioneu)
                        break
                    else:
                        print("Ese NIF no esta registrado")


Salir = False
nif = False  
Dveri = False

while True:

    print("Bienvenido al sistema de pertenecientes a la Unión Europea")
    print("Seleccione una opcion")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir certificados")
    print("4. Salir")
    op = int(input())

    if op == 1:
        grabar()

    elif op == 2:
        buscar()

    elif op == 3:
        imprimircertificado()

    elif op == 4:
        Salir = True
        print("Gracias por usar nuestro sistema")
        print("Version: 1.0")
        break

    elif op == False:
        print("Opcion inexistente")





    
    



        


    

