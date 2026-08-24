#Primero son las key(llaves) y luego los values(valores)
print("GLOSARIO INGLÉS ESPAÑOL")

#Almacena la palabra a buscar que ingresa el usuario
busqueda = input("¿Qué palabra deseas buscar? ")

#Guarda la información del glosario
glosario = {'key' : 'llave', 'house' : 'casa', 'table' : 'mesa'}

#Hace la busqueda de la palabra que le genero el usuario
resultado = (glosario.get(busqueda))

#Condición que busca la palabra si esta agregada o no y si desea agregarla.
if  (resultado is None):
    print("La palabra que buscas no está en el glosario, ¿Quieres agregarla?")
    Respuesta = int(input(" 1-. Sí\n 2-. No\n"))
    if(Respuesta == 1):
        palabra_ingles = input("Escribe la palabra en inglés: ")
        palabra_espanol = input("Escribe la traducción: ")
        glosario[palabra_ingles] = palabra_espanol
        print("¡La palabra fue agregada con éxito!")

else:
    print(resultado)
