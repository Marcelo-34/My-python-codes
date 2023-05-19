def opcion1():
    respuesta = False
    print("Bienvenido a las preguntas de youtubers, si no los conoces, no tienes infancia xd")

    print("Pregunta 1: Que youtuber famoso termina con la frase OMG")
    while respuesta != "elrubius":
        respuesta = str(input())

        match respuesta:
            case "elrubius":
                print("Correcto, pendejete")
            case _:
                print("Pendejo ese no es")
                

    print("Pregunta 2: Que youtuber tiene en el nombre 777")
    while respuesta != "Vegetta":
        respuesta = str(input())
        match respuesta:
            case "Vegetta":
                print("Correcto, pendejete")
            case _:
                print("Pendejo ese no es")
    
    print("Pregunta 3: Que youtuber tiene un video de imitando los emotes de clash royale (Pista: Empieza con A)")
    while respuesta != "Antrax":
        respuesta = str(input())
        match respuesta:
            case "Antrax":
                print("Correcto, pendejete")
            case _:
                print("Pendejo ese no es")
    
    print("Pregunta 4: Que youtuber juega isaac como si fuera ASMR")
    while respuesta != "Elmaldito":
        respuesta = str(input())
        match respuesta:
            case "Elmaldito":
                print("Correcto, pendejete")
            case _:
                print("Pendejo ese no es")

    print("Pregunta 5: El weon de la bolsa en la cabeza")
    while respuesta != "Dylantero":
        respuesta = str(input())
        match respuesta:
            case "Dylantero":
                print("Correcto, pendejete")
            case _:
                print("Pendejo ese no es")

def opcion2():
    respuesta = False
    print("Bienvenido a las preguntas de The biding of isaac")

    print("Pregunta 1: Soy milk es buen item?")
    while respuesta != "Si":
        respuesta = str(input())
        match respuesta:
            case "Si":
                print("Asi es soy milk es un item god incomprendido")
            case "No":
                print("Eres el papulince promedio")
            case _:
                print("Eres tan inutil que no puedes opinar de la leche de soya")
    
    print("Pregunta 2: Cuantos logros tiene isaac")
    while respuesta != 637:
        try:
            respuesta = int(input())
        except:
            print("No se meten letras imbecil si te estoy preguntando cantidad de logros eso en numeros pedazo de pelotudo")
        match respuesta:
            case 637:
                print("Correcto, espero no lo tengas platinado si no eres un enfermo")
            case _:
                print("Eres sano, te felicito por no saber, pero intentalo de nuevo")
    
    print("Pregunta 3: Que personaje o mas bien que OST del juego suelta la frase 'Blasphemy to the holy spirit'")
    while respuesta != "Dogma":
        respuesta = str(input())
        match respuesta:
            case "Dogma":
                print("El besto jefe")
            case _:
                print("BLASPHEMY TO THE HOLY SPIRIT")

print("Seleccione una opcion")
opcion = False
try:
    opcion = int(input())
except:
    print("Error")

match opcion:

    case 1:
        opcion1()
    
    case 2:
        opcion2()
    

        
        
            

                
        



