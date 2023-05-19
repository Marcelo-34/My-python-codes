import numpy as np


def arreglo():
    global departamento
    departamento = np.empty(shape=(20, 5), dtype=("U"))
    return departamento


def comprarDept():
    print("\t\tSELECCION DE PISO")
    print(
        "Piso 1\nPiso 2\nPiso 3\nPiso 4\nPiso 5\nPiso 6\nPiso 7\nPiso 8\nPiso 9\nPiso 10"
    )
    try:
        fila = int(input("Ingrese el numero de piso: "))
        while fila < 1 or fila > 10:
            print("\t\tERROR\nVuelva a ingresar un piso valido")
            fila = int(input())
        print("---" * 15)
        piso = fila - 1

        print("\t\tCOMPRA DE DEPARTAMENTO")
        print(
            "1)\tBlock A : 3.800 UF\n2)\tBlock B : 3.000 UF\n3)\tBlock C : 2.800 UF\n4)\tBlock D : 3.500 UF"
        )
        columna = int(input("Ingrese el numero de Block que desea comprar: "))
        while columna < 1 or columna > 4:
            print("\t\tERROR\nVuelva a ingresar un departamento valido")
            columna = int(input())
        print("---" * 15)
        block = columna - 1

        if "X" in departamento[piso][block]:
            print("El departamento ya esta vendido, eliga otro por favor")
            return
        else:
            departamento[piso][block] = "X"

        rut = int(input("Ingrese su RUT sin puntos ni digito verificador: "))
        while rut < 1000000 or rut > 28000000:
            rut = int(input("\t\tERROR\nVuelva a ingresar su rut: "))
        else:
            print("La operacion se ha realizado correctamente")
            listadoRut.append(rut)
        return departamento
    except ValueError:
        print("Opcion ingresada no valida, vuelva a ingresar una opcion valida")


def listadoCompra():
    print("\t\tLISTADO DE COMPRADORES")
    listadoRut.sort()
    numerador = 1
    for x in listadoRut:
        print("---" * 10)
        print(f"{numerador}) RUT CLIENTE: {x}")
        numerador += 1
        print("")
    input("PRESIONE ENTER PARA CONTINUAR...\t")


def mostrar_Departamento_Disponible(departamento):
    departamento = np.flip(departamento, axis=0)
    print("\t\tDEPARTAMENTO DISPONIBLES\n")
    print("Los departamentos marcados con una X ya estan vendidos\n")
    print("PISO   | A | B| C| D |")
    for piso in range(10):
        print(f"|{abs(piso-10)}|\t{departamento[piso]}")
    input("PRESIONE ENTER PARA CONTINUAR...\t")


def mostrarGanancias():
    total = 0
    contadorA = 0
    contadorB = 0
    contadorC = 0
    contadorD = 0
    for piso in range(10):
        for block in range(4):
            if departamento[piso][block] == "X":
                if departamento[piso][0] == "X":
                    total += 3800
                    contadorA += 1

                elif departamento[piso][1] == "X":
                    total += 3000
                    contadorB += 1

                elif departamento[piso][2] == "X":
                    total += 2800
                    contadorC += 1

                elif departamento[piso][3] == "X":
                    total += 3500
                    contadorD += 1

    print("\t\tGANANCIAS\nTipo de Departamento\t|Cantidad\t|Total|")
    print(f"Tipo A 3800 UF\t\t|{contadorA}\t\t|{contadorA * 3800} UF")
    print(f"Tipo B 3000 UF\t\t|{contadorB}\t\t|{contadorB * 3000} UF")
    print(f"Tipo C 2800 UF\t\t|{contadorC}\t\t|{contadorC * 2800} UF")
    print(f"Tipo D 3500 UF\t\t|{contadorD}\t\t|{contadorD * 3500} UF")
    print(f"TOTAL\t\t\t|{contadorA+contadorB+contadorC+contadorD}\t\t|{total} UF")
    input("PRESIONE ENTER PARA CONTINUAR...\t")


def principal():
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
            opcion = int(
                input(
                    "1) Comprar departamento\n2) Mostrar departamento disponibles\n3) Ver listado de compradores\n4) Mostrar ganancias totales\n5) Salir\n\n\nDigite una de las opciones: "
                )
            )
            print("---" * 15)
            if opcion == 1:
                comprarDept()
            # Mostrar Departamentos Disponibles
            elif opcion == 2:
                mostrar_Departamento_Disponible(departamento)
            # Ver Listado de Compradores
            elif opcion == 3:
                listadoCompra()
            # Mostrar Ganancias totales
            elif opcion == 4:
                mostrarGanancias()

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
