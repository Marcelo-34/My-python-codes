#Ingresa un número y que el programa muestra si es positivo o negativo

print("Ingrese un numero")
numero = int(input())

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
elif numero == 0:
    print("El numero es 0")