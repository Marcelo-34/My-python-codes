#Hacer un programa que simule un cajero automático con un saldo inicial de 1000$ y tendrá el siguiente menu de opciones:
#1. Ingresar dinero en la cuenta
#2: Retirar dinero en la cuenta
#3. Mostrar dinero disponible
#4. Salir

saldoini = 1000

print("Bienvenido al sistema de este cajero")
print("Porfavor ingrese una opcion")

print("1.Ingresar dinero en la cuenta")
print("2.Retirar dinero en la cuenta")
print("3.Mostrar dinero disponible ")
print("4.Salir")
op = int(input())

if op == 1:
    print("Cuanto es el monto que quiere ingresar?")
    montoing = int(input())
    saldofinal = montoing + saldoini

    print("Su saldo ahora es de:" "$",saldofinal)

elif op == 2:
    print("Cuanto dinero quiere retirar de su cuenta?")
    montoreti = int(input())
    if montoreti > saldoini:
        print("El monto a retirar supera su saldo disponible")
    else:
        saldoret = saldoini - montoreti
        print("Su saldo ahora es de:" "$",saldoret)

elif op == 3:
    print("Su saldo es de:", saldoini)

elif op == 4:
    print("Adios")

