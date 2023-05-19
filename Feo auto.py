contMC = 0
contMS = 0
contCA = 0
sumaMC = 0
sumaMS = 0
sumaCA = 0
valorMC = 100500
valorMS = 89000
valorCA = 16000

print("SERVICIOS")
print("*"*40)
print("1. Mantencion Completa:\t $",valorMC)
print("2. Mantencion Simple:\t $",valorMS)
print("3. Cambio de aceite:\t $",valorCA)
print("*"*40)

cantV = int(input("Cantidad de clientes: "))

for i in range(cantV):
  flag = True
  print("Vehiculo :", (i+1))

  while flag:
   op = int(input("Que servicio desea: "))
   if op > 0 and op <4:
    if op == 1:
     contMC = contMC + 1
    sumaMC = sumaMC + valorMC
    flag = False
  else:
    if op ==2:
      contMS = contMS + 1
      sumaMC = sumaMS + valorMS
      flag = False
    else:
      contCA = contCA + 1
      sumaCA = sumaCA+ valorCA
      flag = False
else:
  print("Las opciones estan entre 1-3")



total = sumaMC + sumaMS + sumaCA
print("MANTENCION")
print("*"*40)
print(contMC,"Mantencion Completa:\t $",sumaMC)
print(contMS,"Mantencion Simple:\t $",sumaMS)
print(contCA,"Cambio de aceite:\t $",sumaCA)
print("*"*40)
print("Total: \t\t\t",total)



