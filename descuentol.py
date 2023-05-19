#Hacer un algoritmo que calcule el total a pagar por la compra de camisas. 
#Si se compran tres camisas o más se aplica un descuento del 20% sobre el total de la compra y 
#si son menos de tres camisas un descuento del 10%
#Recuerda que tú también pones el precio de la camisa

camisa = 4000

print("Bienvenido al sistema de compra de su camisa")
print("El precio de las camisas cada una es de:", camisa)

print("Ingrese la cantidad de camisas que desea comprar:")
cantidad = int(input())
if cantidad <= 0:
    print("No se ha ingresado una cantidad a comprar")
    
elif cantidad >= 3:
    cant = camisa * cantidad
    print("Se le aplicara un descuento del 20 %")
    resultadofinal = cant - (cant * 0.20)
    print("El precio a pagar sera de:", resultadofinal)

elif cantidad <= 2:
    cant = camisa * cantidad
    print("Se le aplicara un descuento del 10 %")
    resultadofinal = cant - (cant * 0.10)
    print("El precio a pagar sera de:", resultadofinal)




    




