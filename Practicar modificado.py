#Funciones del codigo:
import numpy as np

def arreglo():
    global asientos
    asientos = np.empty(shape=(10, 10))
    return asientos

def MostrarAsientos(asientos): #Funcion para mostrar los asientos

    print("Estos son los asientos disponibles: ")
    asientos = np.flip(asientos, axis=0)
    print()
    print(asientos) #Imprimir la lista asientos

def ComprarEntradas(): #Funcion para comprar entradas

    print("Cuantos asientos desea comprar?") #Primero preguntaremos cuantos asientos desea comprar
    cantidad=int(input())   #Ingresamos la cantidad

    for i in range(cantidad):   #Con un for en el rango del numero que ingresamos
                                #se repetira las veces que debemos comprar:

        print("Que asiento desea comprar?")
        n_asiento=int(input())    #Recuerda que la variable del asiento a comprar debe ser distinta
                                #al nombre de la lista

        if(n_asiento>0 and n_asiento<=30): #Antes debemos asegurarnos que nuestro numero esta en el
                                           #rango correcto sino es asi pondremos un else abajo de esto
                                           #para indicar que no hay un asiento en ese rango

            n_asiento=n_asiento-1 #Antes de entrar a las condiciones restaremos 1 
                            #para evitar problemas al seleccionar el asiento

            if(asientos[n_asiento])=="X": #Primero evaluaremos si el asiento que hemos seleccionado
                                        #tiene una X por lo que indicaremos que el asiento esta ocupado
                print("Asiento ocupado")

            else:                       #Si no es asi es porque el asiento esta libre por lo que se 
                                        #permitira seleccionar el asiento
                print("Compra exitosa")
                asientos[n_asiento]="X" #Recuerda que aqui es donde debemos cambiar el asiento
                                        #seleccionado por la "X" para indicar que el asiento ya fue ocupado
        else:

            print("Selecciono un asiento inexistente")





#Codigo Principal:

asientos=[] #Creamos la lista asientos

for i in range(0,30): #en el rango(x,x) escribimos siempre desde 0
                      #hasta el numero de asientos que nos piden
                      
    asientos.append(i+1) #Con esto estaremos agregando a la lista cada uno
                         #de los numeros del rango ingresado, ponemos +1
                         #para que los asientos comienzen desde 1 y no desde 0

#Menu:
opcion=False #Declaramos opcion como False para poder usar el try except
while True:
    
    print()                                 #Escribiremos las opciones del menu
    print("Opcion 1: Comprar entradas")
    print("Opcion 2: Mostrar asientos")
    print("Opcion 3: Salir")
    print("Ingrese su opcion:")
    try:                            #Antes de entrar a los casos primero haremos el try except
        opcion=int(input())
    except:                 #Si en el except ponemos un pass evitaremos cualquier caso de error
        pass                #sin mostrar algun mensaje para evitar dos posibles casos de mensaje
                            #de error que se mostara en el match
    match opcion:

        case 1:                 #Invocaremos la funcion de comprar entradas
            ComprarEntradas()

        case 2:                 #Invocaremos la funcion para mostrar los asientos
            MostrarAsientos()

        case 3:                 #La opcion salir debera contener un break para romper el ciclo
            print("Chau XD")
            break

        case _:
            print("Ocurrio un error")  #Si no se cumple ningun caso mostraremos el mensaje de error       
                                     