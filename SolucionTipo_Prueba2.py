registros=""
print("*"*10,"Bienvenido a Centro Médico DUOC UC","*"*10)
#Iteración menú
while True:
    #Menú
    menu_option=int(input("1. Registrar Paciente.\n2. Atención Paciente.\n3. Consultar Datos Paciente.\n4. Salir.\n"))
    #Registro
    if menu_option == 1:
        #Ingreso de datos
        print("*"*5,"REGISTRO NUEVO PACIENTE","*"*5)
        #Validación rut
        while True:
            try:
                rut=int(input("Ingrese su RUT (sin puntos ni guión):\n"))
                if rut >= 5000000 and rut <= 99999999:
                    break
                else:
                    print("Ingreso incorrecto")
            except ValueError:
                print("Ingreso incorrecto")
        #Validación nombre sin números
        while True:
            nombre=input("Ingrese su nombre:\n").upper()
            num=0
            for i in nombre:
                if i in "0123456789+-*/=¿?¡!":
                    num+=1
            if num == 0:
                break
            else:
                print("Ingreso erroneo")
        direccion=input("Ingrese su direccion:\n").upper()
        #Validación mail con @
        while True:
            mail=0
            correo=input("Ingrese su correo:\n").upper()
            for j in correo:
                if j == "@":
                    mail+=1
            if mail > 0:
                break
            else:
                print("Ingreso erroneo")
        #Validación rango de edad
        while True:
            try:
                edad=int(input("Ingrese su edad:\n"))
                if edad in range(0,111):
                    break
                else:
                    print("Ingreso erroneo")
            except ValueError:
                print("Ingreso erroneo")
        #Validación letra sexo
        while True:
            sexo=input("Ingrese su sexo legal: \nHombre (H)\nMujer (M)\n").lower()
            if sexo == "h" or sexo == "m":
                break
            else:
                print("Ingreso erroneo")
            #Asignación para ver la consulta más bonita
        if sexo == "h":
            sexo = "HOMBRE"
        else:
            sexo = "MUJER"
        #Validación PS con mayúsculas
        while True:
            ps=input("Ingrese su sistema de salud (Utilice mayúsculas):\nISAPRE\nFONASA\n")
            if ps == "ISAPRE" or ps == "FONASA":
                break
            else:
                print("Ingreso erroneo")
    #Atención
    elif menu_option == 2:
        print("*"*5,"ATENCIÓN PACIENTE","*"*5)
        #Validación ingreso correcto RUT
        while True:
            try:
                paciente=int(input("Ingrese el RUT del paciente (sin puntos ni guión):\n"))
                if rut >= 5000000 and rut <= 99999999:
                        break
                else:
                    print("Ingreso incorrecto")
            except ValueError:
                print("Ingreso incorrecto")
        #Validación RUT
        if paciente == rut:
            #Validacion formato fecha
            while True:
                guion_fecha=0
                fecha=input("Ingrese la fecha de la consulta (dd-mm-aa):\n")
                for i in fecha:
                    if i == "-":
                        guion_fecha+=1
                if guion_fecha == 2:
                    break
                else:
                    print("Ingreso erroneo. Formato de fecha dd-mm-aa. INGRESAR GUIONES.")
            #Concatenación con registros anteriores.
            observacion=input("Ingrese las observaciones de la consulta:\n")
            nuevo_registro=observacion+". "
            registros+=nuevo_registro
        else:
            print("Es necesario registrar al paciente.")
    #Consultar
    elif menu_option == 3:
        print("*"*5,"CONSULTAR DATOS PACIENTE","*"*5)
        #Validación ingreso correcto RUT
        while True:
            try:
                consulta_rut=int(input("Indique el RUT del paciente a consultar:\n"))
                if rut >= 5000000 and rut <= 99999999:
                        break
                else:
                    print("Ingreso incorrecto")
            except ValueError:
                print("Ingreso incorrecto")
        if consulta_rut == rut:
            print("*"*34,"\nRUT:        ",rut,"\nNOMBRE:     ",nombre,"\nDIRECCIÓN:  ",direccion,"\nCORREO:     ",correo,"\nEDAD:       ",edad,"\nSEXO:       ",sexo,"\nPS:         ",ps)
            print("*"*34,"\nFECHA REGISTRO:\n",fecha,"\nREGISTROS:\n",registros)
        else:
            print("Es necesario registrar al paciente.")
        print("*"*34)
    elif menu_option == 4:
        print("*"*3,"SALIR DEL SISTEMA","*"*3)
        break
    else:
        print("Opcion incorrecta.")
