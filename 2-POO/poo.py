# Definición de una clase
# Ej. Definir la clase Perro

class Perro:
    # En esta parte del código es donde definiremos tantos las
    # características como funcionalidades que puede realizar
    # un elemento perteneciente a la clase (para este ejemplo,
    # la clase Perro)

    # Características: son aquellos elementos dentro de la clase
    # que definen su estado. En el caso de los perros,
    # qué características me interesan de los perritos?
    def __init__(self, name, age, r, date_v):
        # Aquí, en el código de __init__, definiremos los atributos
        # internos de nuestra clase (características)
        self.nombre = name
        self.edad = age
        self.raza = r
        self.f_vacunacion = date_v

    # A continuación, escribiremos todas las funcionalidades que puede
    # realizar esta clase. Recordemos que la funcionalidades queda definidas
    # como "funciones" internas (métodos)
    def updateFVacunacion(self, new_date_v):
        self.f_vacunacion = new_date_v

    def cumple(self):
        self.edad = self.edad + 1
    
# Ya tenemos definida nuestra clase Perro. Cómo creamos objetos a partir de
# esta clase? Recordemos que un objeto es algo concreto dentro del grupo que
# se define a partir de la clase
a = 10 # Esto crea una variable que almacena un entero
print(type(a))
perroA = Perro("Toto", 5, "Poodle", "02-02-2022")
perroB = Perro("Lara", 5, "Schnauzer", "15-12-2021")
print(type(perroA))

# Cuál es el nombre del perrito perroA?
print(perroA.nombre) # Esto accede al nombre que hayamos definido para perroA (Toto)
print(perroB.nombre)

# Cómo utilizamos los métodos internos de una clase a partir de su objeto?
perroA.cumple()
print(f"La edad de {perroA.nombre} es {perroA.edad}")

# Herencia
# Es la creación de una clase base que agrupa aquellos elementos
# ue son comunes entre una o varias clases. Esto, lo que permite es
# agrupar características comunes (y funcionalidades) entre dichas clases
class Felino:
    def __init__(self, nombre, edad, sonido):
        self.nombre = nombre
        self.edad = edad
        self.sonido = sonido
    
    def emitirSonido(self):
        return self.sonido

class Gato(Felino):
    # En este punto, debido a la herencia que definimos, la clase Gato
    # puede hacer TODO lo que puede hacer la clase Felino
    def __init__(self, nombre, edad, dueno):
        super().__init__(nombre, edad, "Miau")
        self.dueno = dueno

class Leon(Felino):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "Grrrr")

# Creamos objetos a partir de las clases recién creadas
cat = Gato("Garfield", 7, "John")
lion = Leon("Leoncio", 10)

print(cat.emitirSonido())
print(lion.emitirSonido())

def makeSound(felino):
    print(felino.emitirSonido())

makeSound(cat)
makeSound(lion)

# Actividad
# Cree las clases Cuenta y Banco donde cada clase tiene las siguientes características
# Clase Cuenta: contiene un número de cuenta (id de cuenta) y un saldo. Además, posee 
# métodos para ver y actualizar el saldo de dicha cuenta
# Clase Banco: Un banco posee múltiples cuentas bancarias. Además posee un 
# método el cual permite realizar transferencias desde una cuenta origen
# a una cuenta destino a partir de sus números de cuenta. Ojo, no se puede 
# transferir desde una cuenta con saldo menor al monto a transferir!
