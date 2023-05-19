#Haz un programa donde ingreses una edad y que le programa determine si la edad está entre el rango de 18-25

print("Ingrese su edad")
edad = int(input())

if edad >= 18 and edad <= 25:
    print("Su edad esta en el rango")
else:
    print("Su edad no esta en el rango")