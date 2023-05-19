import numpy as np


def arreglo():
    global departamento
    departamento = np.empty(shape=(10, 4), dtype=("U"))
    return departamento

def mostrar_Departamento_Disponible(departamento):
    departamento = np.flip(departamento, axis=0)
    print("\t\tDEPARTAMENTO DISPONIBLES\n")
    print("Los departamentos marcados con una X ya estan vendidos\n")
    print("PISO   | A | B| C| D |")
    for piso in range(10):
        print(f"|{abs(piso-10)}|\t{departamento[piso]}")
    input("PRESIONE ENTER PARA CONTINUAR...\t")


def menuprincipal():
    global listadoDept
    global listadoRut
    listadoRut = []
    listadoDept = []
    menu = [0, 1, 2, 3, 4, 5]
    opcion = 0
    arreglo()
    while opcion != 5:
        print("---" * 15)
        print("\t\tMENU\n")
        try:
            "1) Comprar departamento\n2) Mostrar departamento disponibles\n3) Ver listado de compradores\n4) Mostrar ganancias totales\n5) Salir\n\n\nDigite una de las opciones: "
            opcion = int(input())
            print("---" * 15)
            if opcion == 2:
                mostrar_Departamento_Disponible(departamento)
            # Ver Listado de Compradores


            else:
                print("")
            while opcion not in menu:
                print(
                    "\t\tERROR\nVuelva a ingresar una opcion valida o ingrese 0 para volver al menu"
                )
                opcion = int(input())
        except ValueError:
            print("Opcion ingresada no valida, vuelva a ingresar una opcion valida")
    print("---" * 15)
    print("¡Hasta la proxima!")
    print("---" * 15)
    exit()

