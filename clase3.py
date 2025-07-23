# colores = ["rojo", "verde", "azul"]
# print(f"Lista original: {colores}")

# colores[1] = "amarillo" # Cambiamos 'verde'
# print(f"Después de cambiar: {colores}")

# colores.append("violeta") # Añadimos al final
# print(f"Después de append: {colores}")

# color_eliminado = colores.pop(0) # Eliminamos 'rojo'
# print(f"Eliminamos {color_eliminado}, la lista queda: {colores}")

# lista_a = [1, 2, 3]
# lista_b = lista_a        # ¡Esto NO es una copia!
# lista_c = lista_a.copy() # ¡Esto SÍ es una copia!
# lista_b.append(4)

# print(f"Lista A: {lista_a}") # Se modificó también
# print(f"Lista B: {lista_b}")print(f"Lista C: {lista_c}") # Se mantuvo intacta


# numeros = [4 , 1 , 8 , 5]
# for num in numeros: #num es una variable de interaccion
#     print(f"procesando el numero: {num}")
#     print(num)


# numeros = [4, 1, 8, 1, 5]
# for num in numeros:  #num es una variable de iteracion
#     print(f"Procesando el número: {num}")  # f de format string
#     print(num)

# print(f"La lista tiene {len(numeros)} elementos.")
# print(f"¿Está el 8 en la lista? {8 in numeros}")

# numeros.sort() # Modifica la lista original

# print(f"Lista ordenada con .sort(): {numeros}")
# print(f"duplidado de la lista pero ordenada{numeros.sorted()}")


#1. una lista vacía llamada playlist
playlist = []

#2. pide 3 canciones y .append(x)
print("Ingresa 3 canciones que te gusten:")
for i in range(3):
    cancion = input(f"Canción #{i+1}: ")
    playlist.append(cancion)

#3. print
print(playlist)

#. len
print(len(playlist))

#5. preguntar cuál eliminar usando len y pop()
print("¿Qué canción querés eliminar? (ingresá un número entre 1 y ", len(playlist), ")")
for idx, c in enumerate(playlist, start=1):
    print(f"{idx}. {c}")

try:
    num = int(input("Número: "))
    if 1 <= num <= len(playlist):
        eliminada = playlist.pop(num - 1)
        print("Eliminaste:", eliminada)

    else:
        print("Número fuera de rango")

except ValueError:
    print("No ingresaste un número válido")

#. print final
print(playlist)



# coordenadas = (1920, 1080, "full hd")
# Desempaquetado
# ancho, alto, calidad = coordenadas
# print(f"Ancho de la pantalla: {ancho}px")
# print(f"Alto de la pantalla: {alto}px")
# print(f"Calidad de la pantalla: {calidad}px")

# print(coordenadas)
# También funciona en bucles for con listas de tuplas
# usuarios = [("juanperez", "juan@email.com"), ("ana_g", "ana@email.com")]
# for usuario, email in usuarios:
#     print(f"Procesando a {usuario} con email {email}")
    
# lenguaje = "Python"

# # Acceso y slicing
# print(lenguaje[0])    # P

# print(lenguaje[-1])   # n   el -1 lleva al ultimo

# print(lenguaje[1:4])  # yth

# print(lenguaje[:])  #devuelve una copia de toda la cadena

# print(lenguaje[:5])   # pytho  start - stop

# print(lenguaje[1:])   # tyhon del 1 al final

# print(lenguaje[1:6:2])   #yhn va de a 2 desde el 1 al 6
# #start - stop - step == inicio - fin - paso  
# #Esto es slicing

#  ¡Esto daría un error! Las cadenas son inmutables.
# #lenguaje[0] = "J"
