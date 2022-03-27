# Este es un comentario de una sola linea
# Esta es la segunda linea de tu comentario

''' Esto de aca
es un comentario
que ocupa varias
lineas
'''

# Variables
x=2 # Esta de aca es la variable x y tiene asignada un valor de 2
y=5 # Esta seria la variable y
z=x+y # Creamos la variable z y le asignamos el resultado de x + y. z = 7
print(z) # Esto muestra por la terminal el valor de la variable z

# Cosas que se pueden almacenar en variables python (básico)
a1 = 10 # Numeros enteros. Almacena el entero 10 (integer - int)
a2 = 15.3 # Numeros decimales (reales). Almacena el numero flotante 15.3 (flotantes - float)
a3 = "Este es un texto creado con comillas dobles" # Strings. Almacena el texto indicado (strings - str)
a4 = 'Este es un texto creado con comillas simples' # Tambien es un string
a5 = True # Booleanos (valores de verdadero (True) y falso (False)). Almacena valor True. (booleanos - bool)
a6 = 3.3 + 5.1j # Numeros completos. Estos tiene una parte real y una parte imaginaria (acompañada de una j). (complejos - complex)

print(a1, a2, a3, a4, a5, a6) # Muestra los datos almacenados en todas las variables por la terminal

''' 
Quiero escribir por pantalla: 
El valor de la variable a1 es <aqui va el valor de a1> y el valor de a2 es <aqui va el valor de a2>
Ej:
El valor de la variable a1 es 10 y el valor de a2 es 15.3
'''
print("El valor de la variable a1 es", a1, "y el valor de la variable a2 es", a2)
print("El valor de la variable a1 es " + str(a1) + " y el valor de la variable a2 es " + str(a2))
print("El valor de la variable a1 es %d y el valor de la variable a2 es %f " % (a1, a2))
print(f"El valor de la variable a1 es {a1} y el valor de la variable a2 es {a2}")

# Tipos de datos compuestos
# Existen 3 tipos de datos compuestos: listas, tuplas y los diccionarios

# Listas
lista1 = [1, 2, 3] # Es una lista cuyos elementos son todos enteros
lista2 = [1, 9.5, "Texto", [1,4.5, "prueba"]]
# Para acceder a los elementos de una lista, debes utilizar un indice. Ojo: Este parte en 0
print(lista1[1]) # Con el indice 1 estamos accediendo al segundo elemento (porque los indices parten en 0)
print(lista2[0])
print(lista1) # Esto muestra todos los elementos de la lista1
# Como podemos modificar un elemento de mi lista?
# Ejemplo, quiero modificar el primer elemento en lista1 para que, en vez de ser 1, sea "Primer elemento"
lista1[0] = "Primer elemento" # Esto va a reemplazar el valor almacenado en lista1[0] por "Primer elemento"
print(lista1)
# Como accedo a los elementos de la lista interna a lista 2?
# Ej, quiero acceder al tercer elemento -> "prueba"
print(lista2[3][2])
# Agregar elementos a una lista
lista1.append(20)
print(lista1)
# Queremos ahora quita ese elemento que agregamos
lista_removed = lista1.pop(0)
print(lista_removed, lista1)
# Puedo acceder a más de un elemento a la vez de mi lista?
lista3 = [1,2,3,4,5,6,7,8,9,10,11]
print(lista3[2:6:2])
# Quiero mostrar el último elemento
print(lista3[::]) # Parto en el primer elemento, hasta el último elemento y avanazo de 1 en 1
print(lista3[:2],lista3[-2:])
# Como sabemos cual es el largo de una lista?
# Se utiliza la funcion len()
print(len(lista3)) # Te indica el largo de la lista
print(lista3[int(len(lista3)/2)]) # El elemento del medio es

# Tuplas: Son basicamente iguales a las listas....pero son inmutables!
tupla1 = ( 1, 2, 3, 4) # Esta es una tupla de elementos enteros
print(tupla1[:3:2])
# La diferencia entre tuplas y listas es que los elementos de una tupla no se pueden momdificar
# tupla1[2] = 5 # Esto lanza error
tupla2 = (1, "hola", [1,2,3])
print(tupla2)
tupla2[2][1] = 10
print(tupla2)
#tupla2[2] = "Este es un texto" # Esto va a lanzar error
tupla3 = tupla2[:2]
print(tupla3)

# Diccionarios: tipo de dato compuesto cuyo acceso se puede dar con índices de distinto tipo
# Requisito para los indices: deben ser INMUTABLES!

dict1 = {
    0: "Texto para indice 0",
    "llave1": "Texto para la llave llave1",
    (1,2,3): "Texto para la llave tupla (1,2,3)"
}

print(dict1[0]) # Estoy mostrando el contenido asociado a la llave 0 dentro de dict1
print(dict1["llave1"]) # Estoy mostrando el contenido asociado a la llave "llave1" dentro de dict1
print(dict1[(1,2,3)]) # Estoy mostrando el contenido asociado a la llave (1,2,3) dentro de dict1

personas = {
    'Pedro': {"edad":30, "estatura":1.76, "rut":'11111111-1'},
    'Juan': {"edad":28, "estatura":1.92, "rut":'22222222-2'},
    'Maria': [41, 1.68, '33333333-3']
}
print(personas['Pedro']['estatura'])

# Se pueden inicializar múltiples variables al mismo tiempo
a1, a2, a3, a4 = 10, 20, 30, 40

# Se puede determinar el tipo de dato de una variable/dato utilizando la función type()
a1 = 53 # Esta variable es de tipo entero porque se le asigno un entero (53)
print(type(a1)) # type() Retorna cual es el tipo de dato asociado con la variable a1 para este ejemplo
a1 = 13.1
print(type(a1))

# Condicionales, bucles y funciones
###################################

# Condicionales: if, elif, else
x = 11

if x < 4:
    print("El valor de x es menor que 4")
    print("Esta linea si se encuentra en el if")
elif x>1 and x<15: # elif es un else acompañado de un if abreviado
    print("El valor de x es menor que 8")
elif x < 20: # Si no se cumplió la condición anterior, pregunto por esta nueva condición
    print("El valor de x es menor que 20") 
else: 
    print("El valor de x no cumple ninguna de las condiciones")

if x < 4:
    print("El valor de x es menor que 4")
    print("Esta linea si se encuentra en el if")
if x>1 and x<15: # elif es un else acompañado de un if abreviado
    print("El valor de x es menor que 8")
if x < 20: # Si no se cumplio la condición anterior, pregunto por esta nueva condicion
    print("El valor de x es menor que 20") 
# Bucles:
# Existen dos tipos de bucles: for y while

# For
lista5 = [4,2,8,6,3,4]

for i in lista5: # Por cada elemento i pertenciente a la lista5, hago algo
    print("Estoy iterando")
    print(i)

# Puedo usar un for de manera parecida a como lo hacia en javascript? (con un contador?)
# ... Algo asi...
for i in range(0,len(lista5)):
    print(f"El valor del elemento {i} en lista5 es", lista5[i])

# While (mientras)
k=1
# Mientras k sea menor que 10... hago algo
while k<10:
    print(k)
    k+=1
print("Valor de k fuera del while", k)

# El while, por lo general, puede ir acompanado de dos sentencias: break y continue
# break: detiene la ejecucion completa del while
# continue: se salta una iteracion del while
k=1
while k<10:
    if k%3 == 0: # Todos los numeros cuyo resto al dividirse por 3 sea cero, son multiplos de 3
        k+=1
        print("Encontre un multiplo de 3")
        continue

    if k%4 == 0:
        print("Encontre un multiplo de 4")
        break
    
    print("El valor de k es:", k)
    k +=1
print("Termine la ejecucion del while")

# Funciones (por fin!)
# Funciones son bloques de codigo que pueden ser llamados
def suma_num(a, b): # Esta funcion retornara la suma de a+b
    return a+b

# Vamos a utilizar esta funcion que acabamos de definir
x = 10
y = 7
z=suma_num(x, y) # A la variable z se le asigna el retorno de suma_num (17)
print(f"La suma de {x} y {y} es:", suma_num(x,y))

# Las funciones pueden tener cero parametros de entrada
def getMessage():
    return "Este es mi mensaje"
print(getMessage())

# Incluso puedes tener funciones sin parametros de entrada y sin parametros de salida
def printMessage():
    print("Este es mi nuevo mensaje")
for i in range(3):
    printMessage() # Este for llamara a la funcion printMessage tres veces

# Las funciones en python permiten tener parametros por omision
def sumaTresNumeros(a, b, c=0): # Indicaremos un valor por omision para c. En este caso, de cero para que no afecte la suma cuando son dos numeros
    return a+b+c

print(sumaTresNumeros(10,7,3)) # Este print mostrara 20
print(sumaTresNumeros(10,7)) # Este print mostrara 17

# Recursion: Una recursion es cuando llamas a una funcion recursivamente
def factorial(n):
    if n == 1 or n==0:
        return 1
    
    return n*factorial(n-1)

print(factorial(6))