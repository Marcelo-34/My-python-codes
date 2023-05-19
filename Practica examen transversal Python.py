def mostrarasientos():
    print("Estos son los asientos disponibles")
    print()
    print(asiento)

def comprarasientos():
    global opent, cedula,n_asientos, entradaP,entradaG,entradaS, contGold, contPla, contSilver, sumaGold, sumaPla, sumaSilver
    entradaP = 120000
    entradaG = 80000
    entradaS = 50000
    print("Bienvenido al sistema de compra de asientos")
    print("Que tipo de entrada quiere")
    print("1. Entrada Platinum:","$",entradaP)
    print("2. Entrada Gold:","$",entradaG)
    print("3. Entrada Silver:","$",entradaS)
    opent = int(input())
    entradas.append(opent)
    match opent:

        case 1:
            print("Ingrese su cedula de identidad (Sin puntos ni guion ni digito verificador)")
            while True:
                cedula = str(input())
                if len (cedula) == 8:
                    print("Cedula registrada")
                    break
                else:
                    print("Excedio los limites de caracteres o se ingreso mal un dato, intente de nuevo")
                    

            print("Cuantos asientos quiere")
            cantidadasientos = int(input())
            if cantidadasientos <= 3:

                for i in range (cantidadasientos):
                    print("Que numero de asiento quiere: ")
                    n_asientos = int(input())
                    

                    if n_asientos > 0 and n_asientos <=20:
                        n_asientos -= 1

                
                        if asiento [n_asientos] == "X":
                            print("Asiento ocupado")
                    
                        else:
                            print("Asiento comprado")
                            asiento [n_asientos] = "X"
                            nuasientos.append(n_asientos)
                            asistentes.append(cedula)
                            contPla += 1
                            sumaPla += entradaP
                    else:
                        print("Su asiento no se incluye en el rango de su entrada")
            
            else:
                print("Limite de entradas excedido")
        
        case 2:
            print("Ingrese su cedula de indentidad (Sin puntos ni guion ni digito verificador)")
            while True:
                cedula = int(input())
                if cedula > (99999999):
                    print("Excedio los limites de caracteres, intente de nuevo")
                else:
                    print("Cedula registrada")
                    break
            print("Cuantos asientos quiere")
            cantidadasientos = int(input())
            if cantidadasientos <= 3:

                for i in range (cantidadasientos):
                    print("Que numero de asiento quiere: ")
                    n_asientos = int(input())

                    if n_asientos >= 21 and n_asientos <=50:
                        n_asientos -= 1

                
                        if asiento [n_asientos] == "X":
                            print("Asiento ocupado")
                    
                        else:
                            print("Asiento comprado")
                            asiento [n_asientos] = "X"
                            nuasientos.append(n_asientos)
                            asistentes.append(cedula)
                            contGold +=1
                            sumaGold += entradaG
                            
                    else:
                        print("Su asiento no se incluye en el rango de su entrada")
            
            else:
                print("Limite de entradas excedido")

        
        case 3:
            print("Ingrese su cedula de indentidad (Sin puntos ni guion ni digito verificador)")
            while True:
                cedula = int(input())
                if cedula > (99999999):
                    print("Excedio los limites de caracteres, intente de nuevo")
                else:
                    print("Cedula registrada")
                    break

            print("Cuantos asientos quiere")
            cantidadasientos = int(input())
            if cantidadasientos <= 3:

                for i in range (cantidadasientos):
                    print("Que numero de asiento quiere: ")
                    n_asientos = int(input())

                    if n_asientos >= 51 and n_asientos <=100:
                        n_asientos -= 1

                
                        if asiento [n_asientos] == "X":
                            print("Asiento ocupado")
                    
                        else:
                            print("Asiento comprado")
                            asiento [n_asientos] = "X"
                            nuasientos.append(n_asientos)
                            asistentes.append(cedula)
                            contSilver += 1
                            sumaSilver += entradaS
                    else:
                        print("Su asiento no se incluye en el rango de su entrada")
            
            else:
                print("Limite de entradas excedido")

def listadoasist():
    print("Estos son los asistentes ingresados")
    print(asistentes) , print("Tipo de entrada:",entradas), print("Asiento:", nuasientos) 

def mostrarganacias():
    print("Tipo de entrada \t Cantidad \t Total") 

    print("1. Entrada Platinum:\t","\t",contPla,"\t","$",sumaPla )
    print("2. Entrada Gold:\t","\t",contGold,"\t","$",sumaGold)
    print("3. Entrada Silver:\t","\t",contSilver,"\t","$",sumaSilver)
    total = sumaPla + sumaGold + sumaSilver
    print("Total ganado:", total)




asiento = []
for i in range (0,100):
    asiento.append(i+1)

asistentes = []
entradas = []
nuasientos = []
contPla = 0
contGold = 0
contSilver = 0
sumaPla = 0
sumaGold = 0
sumaSilver = 0

while True:
    print("Bienvenido al sistema de compra de entradas")
    print("Eliga una opcion")
    print("1. Mostrar asientos")
    print("2. Comprar entradas")
    print("3. Mostrar asistentes")
    print("4. Mostrar ganancias")
    print("5. Salir")
    op = int(input())

    match op:
        
        case 1:
            mostrarasientos()
        
        case 2:
            comprarasientos()
        
        case 3:
            listadoasist()

        case 4:
            mostrarganacias()
        
        case 5:
            print("Gracias por usar nuestro sistema")
            break


    

