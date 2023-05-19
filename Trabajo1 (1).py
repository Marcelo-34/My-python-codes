m=[[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36],[37,38,39,40,41,42]]

Asiento_normal=78900
Asiento_vip=240000
rutPasajero=0
while True:

    print()
    print("Menu")
    print()
    print("1. Ver Asientos Disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar pasajero")
    print("5. Salir")
    opcion=(int(input()))

    if(opcion==0 or opcion>5):

        print()
        print("NO existe esa opcion")
        print("Regresando al menu...")

    elif(opcion==1):

        print("Estos son los asientos disponibles")
        print("Asientos normales: 1-30  || Asientos VIP: 31-42")
        print()
        for f in range(7):
            for c in range(6):
                print(m[f][c],end=' ')
            print()
        
    elif(opcion==2):
      

        print("Nombre del pasajero: ")
        nombrePasajero=input()
        print("Rut: ")
        rutPasajero=(int(input()))
        if(rutPasajero>99999999):
            print("Error, Intentelo d")
       

        print("Telefono: ")
        telefonoPasajero=(int(input()))
        print("Banco: ")
        bancoPasajero=input()

        print("Que asiento desea tomar: ")
        asiento=(int(input()))
    
        if(0<asiento<31):
            if(bancoPasajero=='bancoDuoc'):
                
                print("Usted posee un descuento del 15% por ser de bancoDuoc")
                print(f"El monto es de {Asiento_normal-Asiento_normal*0.15}")
                print("Desea confirmar su compra?")
                print("1=Si 0=No")
                op1=(int(input()))

                if(op1==1):
                    print("Gracias por su compra")

                    if(asiento==1):
                        m[0][0]='X'
                    elif(asiento==2):
                        m[0][1]='X'
                    elif(asiento==3):
                        m[0][2]='X'
                    elif(asiento==4):
                        m[0][3]='X'
                    elif(asiento==5):
                        m[0][4]='X'  
                    elif(asiento==6):
                        m[0][5]='X'
                    elif(asiento==7):
                        m[1][0]='X'
                    elif(asiento==8):
                        m[1][1]='X'
                    elif(asiento==9):
                        m[1][2]='X'           
                    elif(asiento==10):
                        m[1][3]='X'
                    elif(asiento==11):
                        m[1][4]='X'
                    elif(asiento==12):
                        m[1][5]='X'
                    elif(asiento==13):
                        m[2][0]='X'         
                    elif(asiento==14):
                        m[2][1]='X'
                    elif(asiento==15):
                        m[2][2]='X'
                    elif(asiento==16):
                        m[2][3]='X'
                    elif(asiento==17):
                        m[2][4]='X'                 
                    elif(asiento==18):
                        m[2][5]='X'
                    elif(asiento==19):
                        m[3][0]='X'
                    elif(asiento==20):
                        m[3][1]='X'
                    elif(asiento==21):
                        m[3][2]='X'             
                    elif(asiento==22):
                        m[3][3]='X'
                    elif(asiento==23):
                        m[3][4]='X'
                    elif(asiento==24):
                        m[3][5]='X'
                    elif(asiento==25):
                        m[4][0]='X' 
                    elif(asiento==26):
                        m[4][1]='X'
                    elif(asiento==27):
                        m[4][2]='X'
                    elif(asiento==28):
                        m[4][3]='X'
                    elif(asiento==29):
                        m[4][4]='X'
                    elif(asiento==30):
                        m[4][5]='X'
                    elif(asiento==31):
                        m[5][0]='X'
                    elif(asiento==32):
                        m[5][1]='X'
                    elif(asiento==33):
                        m[5][2]='X' 
                    elif(asiento==34):
                        m[5][3]='X'
                    elif(asiento==35):
                        m[5][4]='X'
                    elif(asiento==36):
                        m[5][5]='X'
                    elif(asiento==37):
                        m[6][0]='X' 
                    elif(asiento==38):
                        m[6][1]='X'
                    elif(asiento==39):
                        m[6][2]='X'
                    elif(asiento==40):
                        m[6][3]='X'
                    elif(asiento==41):
                        m[6][4]='X'  
                    elif(asiento==42):
                        m[6][5]='X'

                elif(op1==0):

                    print()
                    print("Regresando al Menu...") 

            else:    
                print(f"El monto es de {Asiento_normal}")
                print("Desea confirmar su compra?")
                print("1=Si 0=No")
                op1=(int(input()))

                if(op1==1):
                    print("Gracias por su compra")

                    if(asiento==1):
                        m[0][0]='X'
                    elif(asiento==2):
                        m[0][1]='X'
                    elif(asiento==3):
                        m[0][2]='X'
                    elif(asiento==4):
                        m[0][3]='X'
                    elif(asiento==5):
                        m[0][4]='X'  
                    elif(asiento==6):
                        m[0][5]='X'
                    elif(asiento==7):
                        m[1][0]='X'
                    elif(asiento==8):
                        m[1][1]='X'
                    elif(asiento==9):
                        m[1][2]='X'           
                    elif(asiento==10):
                        m[1][3]='X'
                    elif(asiento==11):
                        m[1][4]='X'
                    elif(asiento==12):
                        m[1][5]='X'
                    elif(asiento==13):
                        m[2][0]='X'         
                    elif(asiento==14):
                        m[2][1]='X'
                    elif(asiento==15):
                        m[2][2]='X'
                    elif(asiento==16):
                        m[2][3]='X'
                    elif(asiento==17):
                        m[2][4]='X'                 
                    elif(asiento==18):
                        m[2][5]='X'
                    elif(asiento==19):
                        m[3][0]='X'
                    elif(asiento==20):
                        m[3][1]='X'
                    elif(asiento==21):
                        m[3][2]='X'             
                    elif(asiento==22):
                        m[3][3]='X'
                    elif(asiento==23):
                        m[3][4]='X'
                    elif(asiento==24):
                        m[3][5]='X'
                    elif(asiento==25):
                        m[4][0]='X' 
                    elif(asiento==26):
                        m[4][1]='X'
                    elif(asiento==27):
                        m[4][2]='X'
                    elif(asiento==28):
                        m[4][3]='X'
                    elif(asiento==29):
                        m[4][4]='X'
                    elif(asiento==30):
                        m[4][5]='X'
                    elif(asiento==31):
                        m[5][0]='X'
                    elif(asiento==32):
                        m[5][1]='X'
                    elif(asiento==33):
                        m[5][2]='X' 
                    elif(asiento==34):
                        m[5][3]='X'
                    elif(asiento==35):
                        m[5][4]='X'
                    elif(asiento==36):
                        m[5][5]='X'
                    elif(asiento==37):
                        m[6][0]='X' 
                    elif(asiento==38):
                        m[6][1]='X'
                    elif(asiento==39):
                        m[6][2]='X'
                    elif(asiento==40):
                        m[6][3]='X'
                    elif(asiento==41):
                        m[6][4]='X'  
                    elif(asiento==42):
                        m[6][5]='X'

                elif(op1==0):

                    print()
                    print("Regresando al menu...")

        elif(31<=asiento<=42):

            if(bancoPasajero=='bancoDuoc'):
                
                print("Usted posee un descuento del 15% por ser de bancoDuoc")
                print(f"El monto es de {Asiento_vip-Asiento_vip*0.15}")
                print("Desea confirmar su compra?")
                print("1=Si 0=No")
                op1=(int(input()))

                if(op1==1):
                    print("Gracias por su compra")

                    if(asiento==1):
                        m[0][0]='X'
                    elif(asiento==2):
                        m[0][1]='X'
                    elif(asiento==3):
                        m[0][2]='X'
                    elif(asiento==4):
                        m[0][3]='X'
                    elif(asiento==5):
                        m[0][4]='X'  
                    elif(asiento==6):
                        m[0][5]='X'
                    elif(asiento==7):
                        m[1][0]='X'
                    elif(asiento==8):
                        m[1][1]='X'
                    elif(asiento==9):
                        m[1][2]='X'           
                    elif(asiento==10):
                        m[1][3]='X'
                    elif(asiento==11):
                        m[1][4]='X'
                    elif(asiento==12):
                        m[1][5]='X'
                    elif(asiento==13):
                        m[2][0]='X'         
                    elif(asiento==14):
                        m[2][1]='X'
                    elif(asiento==15):
                        m[2][2]='X'
                    elif(asiento==16):
                        m[2][3]='X'
                    elif(asiento==17):
                        m[2][4]='X'                 
                    elif(asiento==18):
                        m[2][5]='X'
                    elif(asiento==19):
                        m[3][0]='X'
                    elif(asiento==20):
                        m[3][1]='X'
                    elif(asiento==21):
                        m[3][2]='X'             
                    elif(asiento==22):
                        m[3][3]='X'
                    elif(asiento==23):
                        m[3][4]='X'
                    elif(asiento==24):
                        m[3][5]='X'
                    elif(asiento==25):
                        m[4][0]='X' 
                    elif(asiento==26):
                        m[4][1]='X'
                    elif(asiento==27):
                        m[4][2]='X'
                    elif(asiento==28):
                        m[4][3]='X'
                    elif(asiento==29):
                        m[4][4]='X'
                    elif(asiento==30):
                        m[4][5]='X'
                    elif(asiento==31):
                        m[5][0]='X'
                    elif(asiento==32):
                        m[5][1]='X'
                    elif(asiento==33):
                        m[5][2]='X' 
                    elif(asiento==34):
                        m[5][3]='X'
                    elif(asiento==35):
                        m[5][4]='X'
                    elif(asiento==36):
                        m[5][5]='X'
                    elif(asiento==37):
                        m[6][0]='X' 
                    elif(asiento==38):
                        m[6][1]='X'
                    elif(asiento==39):
                        m[6][2]='X'
                    elif(asiento==40):
                        m[6][3]='X'
                    elif(asiento==41):
                        m[6][4]='X'  
                    elif(asiento==42):
                        m[6][5]='X'

                elif(op1==0):

                    print()
                    print("Regresando al Menu...") 

            else:    
                print(f"El monto es de {Asiento_vip}")
                print("Desea confirmar su compra?")
                print("1=Si 0=No")
                op1=(int(input()))

                if(op1==1):
                    print("Gracias por su compra")

                    if(asiento==1):
                        m[0][0]='X'
                    elif(asiento==2):
                        m[0][1]='X'
                    elif(asiento==3):
                        m[0][2]='X'
                    elif(asiento==4):
                        m[0][3]='X'
                    elif(asiento==5):
                        m[0][4]='X'  
                    elif(asiento==6):
                        m[0][5]='X'
                    elif(asiento==7):
                        m[1][0]='X'
                    elif(asiento==8):
                        m[1][1]='X'
                    elif(asiento==9):
                        m[1][2]='X'           
                    elif(asiento==10):
                        m[1][3]='X'
                    elif(asiento==11):
                        m[1][4]='X'
                    elif(asiento==12):
                        m[1][5]='X'
                    elif(asiento==13):
                        m[2][0]='X'         
                    elif(asiento==14):
                        m[2][1]='X'
                    elif(asiento==15):
                        m[2][2]='X'
                    elif(asiento==16):
                        m[2][3]='X'
                    elif(asiento==17):
                        m[2][4]='X'                 
                    elif(asiento==18):
                        m[2][5]='X'
                    elif(asiento==19):
                        m[3][0]='X'
                    elif(asiento==20):
                        m[3][1]='X'
                    elif(asiento==21):
                        m[3][2]='X'             
                    elif(asiento==22):
                        m[3][3]='X'
                    elif(asiento==23):
                        m[3][4]='X'
                    elif(asiento==24):
                        m[3][5]='X'
                    elif(asiento==25):
                        m[4][0]='X' 
                    elif(asiento==26):
                        m[4][1]='X'
                    elif(asiento==27):
                        m[4][2]='X'
                    elif(asiento==28):
                        m[4][3]='X'
                    elif(asiento==29):
                        m[4][4]='X'
                    elif(asiento==30):
                        m[4][5]='X'
                    elif(asiento==31):
                        m[5][0]='X'
                    elif(asiento==32):
                        m[5][1]='X'
                    elif(asiento==33):
                        m[5][2]='X' 
                    elif(asiento==34):
                        m[5][3]='X'
                    elif(asiento==35):
                        m[5][4]='X'
                    elif(asiento==36):
                        m[5][5]='X'
                    elif(asiento==37):
                        m[6][0]='X' 
                    elif(asiento==38):
                        m[6][1]='X'
                    elif(asiento==39):
                        m[6][2]='X'
                    elif(asiento==40):
                        m[6][3]='X'
                    elif(asiento==41):
                        m[6][4]='X'  
                    elif(asiento==42):
                        m[6][5]='X'

                elif(op1==0):

                    print()
                    print("Regresando al Menu...")

    elif(opcion==3):


        if(rutPasajero==0):

            print()    
            print("Usted aun no ha comprado un vuelo")
            print("Regresando al menu...")

        else:       
 
            print("Esta seguro de cancelar el vuelo?")
            print("1=Si 0=No")
            op1=(int(input()))

            if(op1==1):

                print("Ingrese su rut para poder confirmar")
                rutPasajero1=(int(input()))

                if(rutPasajero1==rutPasajero):

                    
                    print("Vuelo anulado")
                    nombrePasajero=0
                    rutPasajero=0
                    telefonoPasajero=0
                    bancoPasajero=0

                    if(asiento==1):
                        m[0][0]=1
                    elif(asiento==2):
                        m[0][1]=2
                    elif(asiento==3):
                        m[0][2]=3
                    elif(asiento==4):
                        m[0][3]=4
                    elif(asiento==5):
                        m[0][4]=5  
                    elif(asiento==6):
                        m[0][5]=6
                    elif(asiento==7):
                        m[1][0]=7
                    elif(asiento==8):
                        m[1][1]=8
                    elif(asiento==9):
                        m[1][2]=9           
                    elif(asiento==10):
                        m[1][3]=10
                    elif(asiento==11):
                        m[1][4]=11
                    elif(asiento==12):
                        m[1][5]=12
                    elif(asiento==13):
                        m[2][0]=13         
                    elif(asiento==14):
                        m[2][1]=14
                    elif(asiento==15):
                        m[2][2]=15
                    elif(asiento==16):
                        m[2][3]=16
                    elif(asiento==17):
                        m[2][4]=17                 
                    elif(asiento==18):
                        m[2][5]=18
                    elif(asiento==19):
                        m[3][0]=19
                    elif(asiento==20):
                        m[3][1]=20
                    elif(asiento==21):
                        m[3][2]=21             
                    elif(asiento==22):
                        m[3][3]=22
                    elif(asiento==23):
                        m[3][4]=23
                    elif(asiento==24):
                        m[3][5]=24
                    elif(asiento==25):
                        m[4][0]=25 
                    elif(asiento==26):
                        m[4][1]=26
                    elif(asiento==27):
                        m[4][2]=27
                    elif(asiento==28):
                        m[4][3]=28
                    elif(asiento==29):
                        m[4][4]=29
                    elif(asiento==30):
                        m[4][5]=30
                    elif(asiento==31):
                        m[5][0]=31
                    elif(asiento==32):
                        m[5][1]=32
                    elif(asiento==33):
                        m[5][2]=33 
                    elif(asiento==34):
                        m[5][3]=34
                    elif(asiento==35):
                        m[5][4]=35
                    elif(asiento==36):
                        m[5][5]=36
                    elif(asiento==37):
                        m[6][0]=37 
                    elif(asiento==38):
                        m[6][1]=38
                    elif(asiento==39):
                        m[6][2]=39
                    elif(asiento==40):
                        m[6][3]=40
                    elif(asiento==41):
                        m[6][4]=41  
                    elif(asiento==42):
                        m[6][5]=42
                else:

                    print()    
                    print("RUT incorrecto, vuelva a intentarlo")
                    print("Regresando al Menu...")

            if(op1==0):
                
                print()
                print("Regresando al menu...")

    elif(opcion==4):

        if(rutPasajero==0):

            print("Usted aun no ha comprado un vuelo")
        else:

            print("Que asiento ha tomado?")
            asiento1=(int(input()))
            if(asiento1==asiento):

                print("Ingrese su RUT para poder confirmar")
                rutPasajero2=(int(input()))

                if(rutPasajero2==rutPasajero):

                    print("Que datos desea modificar?") 
                    print("1. Modificar nombre") 
                    print("2. Modificar telefono")
                    op1=(int(input()))

                    if(op1==1):

                        print("Ingrese el nuevo nombre: ")
                        nombrePasajero=input()

                        print()
                        print("Transaccion completa") 
                        print("Regresando al Menu...")

                    elif(op1==2):

                        print("Ingrese el nuevo telefono")
                        telefonoPasajero=(int(input())) 

                        print()
                        print("Transaccion completa") 
                        print("Regresando al Menu...")  

                else:

                    print()        
                    print("Datos incorrectos") 
                    print("Regresando al Menu...") 

            else:

                print()        
                print("Datos incorrectos") 
                print("Regresando al Menu...")

    elif(opcion==5):

        nombrePasajero=0
        rutPasajero=0
        telefonoPasajero=0
        bancoPasajero=0

        print()
        print("Gracias por usar ....")                  