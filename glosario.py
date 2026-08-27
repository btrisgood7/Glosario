import json

with open("glosario.json") as f:
    glosario = json.load(f)
    #Primero son las key(llaves) y luego los values(valores)
opcion = None
while opcion != 0:
    print("GLOSARIO INGLÉS ESPAÑOL")
    print("¿Qué deseas hacer?")
    print("1.- Buscar una palabra")
    print("2.- Ver todas las palabras")
    print("3.- Agregar una palabra")
    print("4.- Modificar palabra en español")
    print("5.- Modificar palabra en inglés")
    print("6.- Eliminar una palabra")
    print("0.-Salir\n")

    opcion = int(input(""))
    print("Elegiste la opción: ",opcion)

    match opcion:

        case 1:
            print("BUSCAR UNA PALABRA:")
            busqueda = input("¿Qué palabra deseas buscar? ").lower().strip()
            resultado = (glosario.get(busqueda))
            if (resultado is None):
                print("La palabra que intentas buscar no esta en el glosario, ¿quieres agregarla?")
                respuesta = int(input(" 1- Sí \n 2- No"))
                if (respuesta == 1):
                    palabra_espanol2 = input("Escriba la traducción: ")
                    glosario[busqueda] = palabra_espanol2
                    with open ("glosario.json","w") as i:
                        json.dump(glosario,i)
                        print("Traducción agregada con éxito :D")
                elif (respuesta == 2):
                    print("Okey, adios")
            else:
                print("La traducción de tu palabra es:", resultado)

        case 2:
            print("VER TODAS LAS PALABRAS")
            for clave, valor in sorted(glosario.items()): #sorted las acomoda en orden alfabetico || sorted(glosario.items(), key=lambda x: x[1])) para mostrarlo de la Z a la A
                print(clave,valor)

        case 3:
            print ("AGREGAR UNA PALABRA")
            palabra_ingles = input("Escribe la palabra en inglés: ").lower().strip()
            if (palabra_ingles in glosario):
                print("Esa palabra ya está en el glosario, por favor revisa bien :D")
            else:
                palabra_espanol = input("Escribe la traducción: ")
                glosario[palabra_ingles] = palabra_espanol
                with open("glosario.json","w") as e:
                    json.dump(glosario,e)
                    print("Palabra agregada con éxito")

        case 4:
            print("Modificar palabra en español")
            palabra_antes_de_modificar=input("¿Qué palabra deseas modificar? ").lower().strip()
            if (palabra_antes_de_modificar in glosario):
                palabra_modificada =input("¿Cuál es su corrección? ")
                glosario[palabra_antes_de_modificar]=palabra_modificada
                with open ("glosario.json","w") as m:
                    json.dump(glosario,m)
                    print("\nTraducción modificada con éxito :D")
            else:
                print("Palabra no encontrada, por favor intente de nuevo")
        case 5:
            print("Modficar palabra en inglés")
            palabra_ingles_am = input("¿Qué palabra deseas modificar?: ").lower().strip()
            #if (palabra_ingles_am in glosario):

        case 6:
            print("Eliminar una palabra ")
            palabra_elimina=input("¿Qué palabra deseas eliminar? ").lower().strip()
            if (palabra_elimina in glosario):
                glosario.pop(palabra_elimina)
                with open("glosario.json","w") as d:
                    json.dump(glosario,d)
                    print("Palabra eliminada!")
            else:
                print("Palabra no encontrada, por favor intente de nuevo")
                    

        