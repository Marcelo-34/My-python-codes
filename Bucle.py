import math

num = int(input("Digite un numero: "))

while num<0:
    print("Error: El numero debe ser positivo :(")
    num = int(input("Difite un numero: "))

print(f"\n La raiz cuadrara es: {(math.sqrt(num)):.2f}")