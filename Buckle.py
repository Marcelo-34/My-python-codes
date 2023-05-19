# que el programa te pregunte cuando es 2+2 y hasta que la respuesta no sea correcta el programa 
# seguira preguntandote lo mismo, y una ves acertado que te muestre un mensaje de felicidades 

respuesta = 0
vidas= 3

while(vidas != 0):
    while(respuesta != 4):
    

    
        print("Cuando es 2 + 2")
        respuesta =int(input())
        if(respuesta!= 4):
            vidas-=1

        print("La Respuesta es incorrecta")

        print("Perdiste una vida, te quedan: ", vidas)
if vidas == 0:
    print("Te quedaste sin vidas")

        

            




