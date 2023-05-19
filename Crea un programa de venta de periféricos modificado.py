
mouseL = 400
tecladoL = 300
audifonosL = 100
mouseR = 200
tecladoR = 500
audifonosR = 150
mouseX = 250
tecladoX = 200
audifonosX = 120

print("Bienvenido al sistema de compra de perifericos donde se ira todo su sueldo")
print("Porfavor ingrese su nombre")
nombre = str(input())
print("Hola", nombre)
print("Posee usted un cupon de descuento?")

print("Si: 1 o No: 2")
opdesc = int(input())

if opdesc == 1:
    print("Ingrese su codigo de cupon")
    codigo = str(input())

    if codigo != "TRV125":
        print("Ese codigo no es valido")

    print("Que marca desea escoger, tenemos las siguientes disponibles")
    print("Logitech (L), Razer(R), HyperX(H)")
    print("Ingrese su marca")
    opmarca = str(input())
    if opmarca == "L":
        print("Estos son nuestros precios normales: ")
        print("1.Mouse Logitech", "$",mouseL )
        print("2.Teclado Logitech", "$",tecladoL)
        print("3.Audifonos Logitech", "$",audifonosL)
        print("Cual desea?")
        opperi = int(input())

        if opperi == 1:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Logitech")
            print("Tipo de periferico: Mouse")
            print("Precio:" "$",mouseL)
        elif opperi == 2:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Logitech")
            print("Tipo de periferico: Teclado")
            print("Precio:" "$",tecladoL)
        elif opperi == 3:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Logitech")
            print("Tipo de periferico: Audifonos")
            print("Precio:" "$",audifonosL)
    
    if opmarca == "R":
        print("Estos son nuestros precios normales: ")
        print("1.Mouse Razer", "$",mouseR )
        print("2.Teclado Razer", "$",tecladoR)
        print("3.Audifonos Razer", "$",audifonosR)
        print("Cual desea?")
        opperi = int(input())

        if opperi == 1:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Razer")
            print("Tipo de periferico: Mouse")
            print("Precio:" "$",mouseR)
        elif opperi == 2:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Razer")
            print("Tipo de periferico: Teclado")
            print("$",tecladoR)
        elif opperi == 3:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Razer")
            print("Tipo de periferico: Audifonos")
            print("Precio:" "$",audifonosR)

    if opmarca == "H":
        print("Estos son nuestros precios normales: ")
        print("1.Mouse HyperX", "$",mouseX )
        print("2.Teclado HyperX", "$",tecladoX)
        print("3.Audifonos HyperX", "$",audifonosX)
        print("Cual desea?")
        opperi = int(input())

        if opperi == 1:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: HyperX")
            print("Tipo de periferico: Mouse")
            print("Precio:" "$",mouseX)
        elif opperi == 2:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: HyperX")
            print("Tipo de periferico: Teclado")
            print("Precio:" "$",tecladoX)
        elif opperi == 3:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: HyperX")
            print("Tipo de periferico: Audifonos")
            print("Precio:" "$",audifonosX)
    else:
        print("Se le aplicara un descuento del 10 por ciento a todos los productos que escoja")
        mouseLdesc = mouseL - (mouseL * 0.10)
        tecladoLdesc = tecladoL - (tecladoL * 0.10)
        audifonosLdesc = audifonosL - (audifonosL * 0.10)
        mouseRdesc = mouseR - (mouseR * 0.10)
        tecladoRdesc = tecladoR - (tecladoR * 0.10)
        audifonosRdesc = audifonosR - (audifonosR * 0.10)
        mouseXdesc = mouseX - (mouseX * 0.10)
        tecladoXdesc = tecladoX - (tecladoX * 0.10)
        audifonosXdesc = audifonosX - (audifonosX * 0.10)
    
     

    print("Que marca desea escoger, tenemos las siguientes disponibles")
    print("Logitech (L), Razer(R), HyperX(H)")
    print("Ingrese su marca")
    opmarca = str(input())
    if opmarca == "L":

        print("Estos son nuestros precios con su cupon: ")
        print("1.Mouse Logitech", "$",mouseLdesc )
        print("2.Teclado Logitech", "$",tecladoLdesc)
        print("3.Audifonos Logitech", "$",audifonosLdesc)
        print("Cual desea?")
        opperi = int(input())

        if opperi == 1:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Logitech")
            print("Tipo de periferico: Mouse")
            print("Precio:" "$",mouseLdesc)
        elif opperi == 2:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Logitech")
            print("Tipo de periferico: Teclado")
            print("Precio:" "$",tecladoLdesc)
        elif opperi == 3:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Logitech")
            print("Tipo de periferico: Audifonos")
            print("Precio:" "$",audifonosLdesc)
    else:
        print("Esa marca no esta registrada")
    
    if opmarca == "R":
        print("Estos son nuestros precios con su cupon: ")
        print("1.Mouse Razer", "$",mouseRdesc )
        print("2.Teclado Razer", "$",tecladoRdesc)
        print("3.Audifonos Razer", "$",audifonosRdesc)
        print("Cual desea?")
        opperi = int(input())

        if opperi == 1:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Razer")
            print("Tipo de periferico: Mouse")
            print("Precio:" "$",mouseRdesc)
        elif opperi == 2:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Razer")
            print("Tipo de periferico: Teclado")
            print("$",tecladoRdesc)
        elif opperi == 3:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Razer")
            print("Tipo de periferico: Audifonos")
            print("Precio:" "$",audifonosRdesc)

    if opmarca == "H":
        print("Estos son nuestros precios con su cupon: ")
        print("1.Mouse HyperX", "$",mouseXdesc )
        print("2.Teclado HyperX", "$",tecladoXdesc)
        print("3.Audifonos HyperX", "$",audifonosXdesc)
        print("Cual desea?")
        opperi = int(input())

        if opperi == 1:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: HyperX")
            print("Tipo de periferico: Mouse")
            print("Precio:" "$",mouseXdesc)
        elif opperi == 2:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: HyperX")
            print("Tipo de periferico: Teclado")
            print("Precio:" "$",tecladoXdesc)
        elif opperi == 3:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: HyperX")
            print("Tipo de periferico: Audifonos")
            print("Precio:" "$",audifonosXdesc)
    else:
        print("Esa marca no esta registrada")


elif opdesc == 2:
    print("Que marca desea escoger, tenemos las siguientes disponibles")
    print("Logitech (L), Razer(R), HyperX(H)")
    print("Ingrese su marca")
    opmarca = str(input())
    if opmarca == "L":
        print("Estos son nuestros precios normales: ")
        print("1.Mouse Logitech", "$",mouseL )
        print("2.Teclado Logitech", "$",tecladoL)
        print("3.Audifonos Logitech", "$",audifonosL)
        print("Cual desea?")
        opperi = int(input())

        if opperi == 1:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Logitech")
            print("Tipo de periferico: Mouse")
            print("Precio:" "$",mouseL)
        elif opperi == 2:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Logitech")
            print("Tipo de periferico: Teclado")
            print("Precio:" "$",tecladoL)
        elif opperi == 3:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Logitech")
            print("Tipo de periferico: Audifonos")
            print("Precio:" "$",audifonosL)
    else:
        print("Esa marca no esta registrada")

    
    if opmarca == "R":
        print("Estos son nuestros precios normales: ")
        print("1.Mouse Razer", "$",mouseR )
        print("2.Teclado Razer", "$",tecladoR)
        print("3.Audifonos Razer", "$",audifonosR)
        print("Cual desea?")
        opperi = int(input())

        if opperi == 1:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Razer")
            print("Tipo de periferico: Mouse")
            print("Precio:" "$",mouseR)
        elif opperi == 2:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Razer")
            print("Tipo de periferico: Teclado")
            print("$",tecladoR)
        elif opperi == 3:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: Razer")
            print("Tipo de periferico: Audifonos")
            print("Precio:" "$",audifonosR)



    if opmarca == "H":
        print("Estos son nuestros precios normales: ")
        print("1.Mouse HyperX", "$",mouseX )
        print("2.Teclado HyperX", "$",tecladoX)
        print("3.Audifonos HyperX", "$",audifonosX)
        print("Cual desea?")
        opperi = int(input())

        if opperi == 1:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: HyperX")
            print("Tipo de periferico: Mouse")
            print("Precio:" "$",mouseX)
        elif opperi == 2:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: HyperX")
            print("Tipo de periferico: Teclado")
            print("Precio:" "$",tecladoX)
        elif opperi == 3:
            print("Nombre:", nombre)
            print("Fecha: 01/07/2022")
            print("Marca: HyperX")
            print("Tipo de periferico: Audifonos")
            print("Precio:" "$",audifonosX)
    else:
        print("Esa marca no esta registrada")
 

    











