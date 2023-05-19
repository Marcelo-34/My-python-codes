MantCompleta = 100500
MantSimple = 89000
Caceite = 16000
auto = 0
while auto != 3:

    print("Bienvenido al sistema automotriz")
    print("Tenemos los siguientes servicios disponibles")

    print("1. Mantencion completa","$", MantCompleta)
    print("2. Mantencion Simple","$", MantSimple)
    print("3. Cambio de aceite","$", Caceite)
    op = int(input())

    if op == 1:
        print("Usted ha seleccionado la mantencion completa")
        print("Su costo total sera de:", MantCompleta)
        auto+=1

    elif op == 2:
        print("Usted ha seleccionado la mantencion Simple")
        print("Su costo total sera de:", MantSimple)
        auto+=1

    elif op == 3:
        print("Usted ha seleccionado el cambio de aceite")
        print("Su costo total sera de:", Caceite)
        auto+=1

