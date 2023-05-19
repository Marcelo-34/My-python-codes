#programa donde ingreses el precio de un producto y luego te muestre el precio tras aplicarle el IVA

print("Ingrese el precio de su producto")
precio = int(input())

ivaincluide = precio + (precio * 0.19)


print("Su precio final con iva incluido es de:", ivaincluide)