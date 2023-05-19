a = 5
b = 0
try:
    c = a/b
    print(f"El resultado es: {c}")
except ZeroDivisionError:
    print("No se ha podido realizar la division")