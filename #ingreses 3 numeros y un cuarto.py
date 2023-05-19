#ingreses 3 numeros
#Luego debes ingresar un 4to numero
#Y luego indicar si el 4to número coincide con uno de los 3 números anteriores

print("Ingrese un numero")
numero1 = int(input())
print("Ingrese segundo numero")
numero2 = int(input())
print("Ingrese tercer numero")
numero3 = int(input())

print("Primer numero:", numero1)
print("Segundo numero:", numero2)
print("Tercer numero:", numero3)

print("Ingrese un cuarto numero numero")
numero4 = int(input())

if numero4 == numero1 or numero4 == numero2 or numero4 == numero3:
    print("El numero coincide con uno los ingresados")
else:
    numero4 != numero1 or numero4 != numero2 or numero4 != numero3
    print("El numero NO coincide con uno los ingresados")

        

