from random import randint,random,uniform
print("Bienvenido a Naranja Chikito")
print("Presone cualquier tecla para simular una batalla contra un bot")
key=(int(input()))

win=0
hp1=6
hp2=8

while(win!=1):

    
    print(f"HP: {hp1}    ||    HP: {hp2}")
    key=(int(input()))
    print("1 para Atacar")
    key=(int(input()))
    dado1=randint(1,6)
    
    print("P1: ")
    print(f"Dado Ataque: {dado1}")
    key=(int(input()))
    
    if(hp2==1):
        dado2=randint(1,6)
        print("P2: ")
        print(f"Dado Evade: {dado2}")
        key=(int(input()))
        if(dado2==dado1):

           hp2=hp2-dado1

        elif(dado2>dado1):
            
            hp2
                               
        elif(dado2<dado1):
            
            hp2=hp2-dado1

        if(hp2<=0):

            win=1                    
    else:
        dado2=randint(1,6)
        print("P2: ")
        print(f"Dado Defensa: {dado2}")
        key=(int(input()))
        if(dado1==dado2):

            hp2=hp2-1
                        
        elif(dado1>dado2):

            hp2=hp2-(dado1-dado2)

        elif(dado1<dado2):

            hp2=hp2-1 

        if(hp2<=0):

            win=1

    if(hp2>0):

        print(f"HP: {hp1}    ||    HP: {hp2}")
        key=(int(input()))
        dado2=randint(1,6)
        print("P2 :")
        print(f"Dado Ataque: {dado2}")
        key=(int(input()))
        print("1: Defender || 2: Evadir")
        op=(int(input()))

        if(op==1):

            dado1=randint(1,6)
            print("P1: ")
            print(f"Dado Defensa: {dado1}")
            key=(int(input()))
            if(dado2==dado1):

                hp1=hp1-1
                            
            elif(dado2>dado1):

                hp1=hp1-(dado2-dado1)

            elif(dado2<dado1):

                hp1=hp1-1 

            if(hp1<=0):

                win=1

        elif(op==2):

            dado1=randint(1,6)
            print("P1: ")
            print(f"Dado Evade: {dado1}")
            key=(int(input()))
            if(dado1==dado2):

                hp1=hp1-dado2

            elif(dado1>dado2):
                
                hp1
                                
            elif(dado1<dado2):
                
                hp1=hp1-dado2

            if(hp1<=0):

                win=1 

        
        
                    

print()
print("Fin de la partida")
if(hp1<=0):

    print()
    print("Jaja te gano un bot")

elif(hp2<=0):

    print()
    print("Fasilito")       