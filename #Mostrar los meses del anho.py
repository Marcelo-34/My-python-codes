#Mostrar los meses del anho, pidiendo al usuario un numero entre 1-12 y mostrar el mes correspondiente

print("Ingrese un numero de 1-12")
numeromes = int(input())

if numeromes == 1:
    print("El mes es enero")

elif numeromes == 2:
    print("El mes es febrero")

elif numeromes == 3:
    print("El mes es marzo")

elif numeromes == 4:
    print("El mes es abril")

elif numeromes == 5:
    print("El mes es mayo")

elif numeromes == 6:
    print("El mes es junio")

elif numeromes == 7:
    print("El mes es julio")

elif numeromes == 8:
    print("El mes es agosto")

elif numeromes == 9:
    print("El mes es septiembre")

elif numeromes == 10:
    print("El mes es octubre")

elif numeromes == 11:
    print("El mes es noviembre")

elif numeromes == 12:
    print("El mes es diciembre")

elif numeromes > 12:
    print("No existe ningun mes mas alla del 12 a no ser que seas un alien")

