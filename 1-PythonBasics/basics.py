# Este es un comentario de una sola línea
# Esta sería la segunda línea de mi comentario

''' DOCSTRING   
Esto de acá en un programa normal, correspondería
a un comentario de múltiples
líneas
'''

# Variables
x = 2 # x representa una variable con valor asignado 2
y = 5 # y sería una variable con valor asignado 5
z = x + y # z es una variable con valor asignado x + y = 7
print(z) # print muestra el contenido de lo que se entrega por entrada en la terminal

# Qué cosas se pueden almacenar en variables python (básico)
a1 = 10 # Números enteros. Tipo de dato integer - int
a2 = 15.3 # Números decimales (reales). Tipo de dato flotante - float
a3 = "Este es un texto creado con comillas dobles" # Textos. Tipo de dato es string - str
a4 = 'Este es un texto creado con comillas simples' # También es un string
a5 = True # Valores de verdad. Pueden ser Verdadero (True) y Falso (False). Tipo de dato es boolean - bool
# Números complejos. Tienen una parte real y una parte imaginaria
# La parte imaginaria se indica acompañada de una j. Tipo de dato complex - complex
a6 = 3.3 + 5.1j  

print(a1, a2, a3, a4, a5, a6) # Mostramos los valores almacenados en las variables por terminal

# Quieres escribir por pantalla lo siguiente:
# El valor de la variable a1 es <valor de a1> y el valor de a2 es <valor de a2>
# Ej. El valor de la variable a1 es 10 y el valor de a2 es 15.3
print("El valor de la variable a1 es", a1, "y el valor de la variable a2 es", a2)
print("El valor de la variable a1 es " + str(a1) + " y el valor de la variable a2 es " + str(a2))
print("El valor de la variable a1 es %d y el valor de la variable a2 es %f " % (a1, a2))
print(f"El valor de la variable a1 es {a1} y el valor de la variable a2 es {a2}")

# Tipos de datos compuestos
# Existen 3 tipos de datos compuestos: listas, tuplas y los diccionarios... 
# también están los objetos (después)

# Listas
lista1 = [1, 2, 3] # lista1 es una variable de tipo lista - list que contiene 3 elementos enteros
lista2 = [1, 9.5, "Texto", [1, 4.5, "prueba"]]
# Para acceder a los elementos de una lista, debes utilizar un índice.
# Ojo: Los índices parten en 0
# ej. Con el índice 1, estamos accediendo al segundo elemento
print("El elemento con índice 1 en lista1 es", lista1[1])
print(lista1)
# Cómo podemos modificar un elemento de mi lista?
# Ej. quiero modificar el primer elemento de lista1 para que
# en vez de ser 1, sea "Primer elemento"
lista1[0] = "Primer elemento" # Se reemplaza el valor almacenado en lista1[0]
print(lista1)
# Es posible acceder a los elementos de la lista interna a lista2?
# Ej. Quiero acceder al tercer elemento de la lista interna -> "prueba"
print(lista2[3][2])
# Agregar elemento a una lista
lista1.append(20)
print(lista1)
# Agregar un elemento en una cierta posición
lista1.insert(1, "pez")
print(lista1)
# Queremos ahora quitar el elemento que acabamos de agregar
elemento = lista1.pop()
print(elemento, lista1)
new_elemento = lista1.pop(0)
print(new_elemento, lista1)
# Qué pasa si queremos eliminar/agregar dentro de la lista interna?
lista2[3].append("pollo")
print(lista2)
lista2[3].pop()
print(lista2)
# Puedo acceder a más de un elemento a la vez de mis listas?
lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(lista3[2:6:2])
# También se puede recorrer de forma inversa
print(lista3[-1:0:-2])
# Quiero mostrar el último elemento
print(lista3[::]) # Parto en el primer elemento, hasta el último elemento y avanazo de 1 en 1
print(lista3[:2],lista3[-2:])
# Como sabemos cual es el largo de una lista?
# Se utiliza la funcion len()
print(len(lista3)) # Te indica el largo de la lista
print(lista3[int(len(lista3)/2)]) # El elemento del medio es

# Tuplas: Son básicamente iguales a las listas... pero inmutables!
tupla1 = (1, 2, 3, 4)
print(tupla1[:2])
# La diferencia entre tuplas y listas es que los elementos de una tupla no se pueden modificar
# tupla1[2] = 5 # Lanza error
tupla2 = (1, "hola", [1, 2, 3])
print(tupla2)
# Ojo, tupla[2] = "pez", esto también lanza error
tupla2[2].append(4)
print(tupla2)

# Diccionarios: tipo de dato compuesto cuyo acceso se puede dar con diferentes índices
# El índice dentro de un diccionario puede ser CUALQUIER COSA... siempre y cuando
# ese índice sea un dato INMUTABLE
dict1 = {
    0: "Texto para llave 0",
    "llave1": "Texto para la llave1",
    (1, 2, 3): "Texto para la llave tupla (1, 2, 3)",
}

print(dict1[0]) # Muestra el contenido para la llave 0
print(dict1["llave1"]) # Muestra el contenido para la llave llave1
print(dict1[(1, 2, 3)]) # Muestra el contenido para la llave (1, 2, 3)






# Escriba un código Python que entregue ciertas caracterı́sticas de un número solicitado. Para esto, el programa deberá realizar las siguientes tareas:
# Solicitar al usuario un número entero positivo perteneciente al rango [2,1000]. Su programa debe verificar esta condición. En caso contrario, se debe pedir otro número hasta que se cumpla la condición.
# Indicar las siguientes caracterı́sticas del número solicitado:
# ¿Es un número par o impar?
# ¿Es un número primo?
# ¿Cuál es el conjunto de divisores del número? (Se dice que y es divisor de x si el resultado de x ÷ y es un número entero).
# Una vez indicada las caracterı́sticas del número, el programa debe finalizar. Ejemplo de funcionamiento:

# Ingrese un número: 6
# Número par
# No es un número primo
# Conjunto de divisores:
# 1
# 2
# 3
# 6