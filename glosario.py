import json

with open("glosario.json") as f:
    glosario = json.load(f)
    #Primero son las key(llaves) y luego los values(valores)
    print("GLOSARIO INGLÉS ESPAÑOL")

    #Almacena la palabra a buscar que ingresa el usuario
    busqueda = input("¿Qué palabra deseas buscar? ").lower().strip()

    #Hace la busqueda de la palabra que le genero el usuario
    resultado = (glosario.get(busqueda))

    #Condición que busca la palabra si esta agregada o no y si desea agregarla.
    if  (resultado  is None):
        print("La palabra que buscas no está en el glosario, ¿Quieres agregarla?")
        Respuesta = int(input(" 1-. Sí\n 2-. No\n"))
        if(Respuesta == 1):

            #Guarda la traducción
            palabra_espanol = input("Escribe la traducción: ").lower().strip()

            #Es como si buscaramos dog: glosario["dog"] = "perro"
            glosario[busqueda] = palabra_espanol

            #abre el .json y le damos la opción de escribir, que para nosotros es la variable e
            with open("glosario.json", "w") as e:

                #Toma el contenido de glosario y lo escribe dentro del archivo e
                json.dump(glosario,e)
                print("¡La palabra fue agregada con éxito!")
        else:
            print("Hasta la proximaaaa, tutututututututu")

    else:
        print(resultado)
