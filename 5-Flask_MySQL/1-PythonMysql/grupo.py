from sqlite3 import connect
from unittest import result
from mysqlconnection import connectToMySQL

# Crearemos una clase llamada Grupo
class Grupo:
    def __init__(self, data):
        self.idGrupo = data['idGrupo']
        self.nombre_grupo = data['nombre_grupo']
        self.descripcion_grupo = data['descripcion_grupo']

    # Decorador classmethod indica que el método puede ser llamado sin instanciar la clase
    @classmethod
    def get_all(cls):
        query = "select * from grupo;"
        mysql = connectToMySQL('curso')
        results = mysql.query_db(query) # Conexión a la base de datos
        grupos = []
        for result in results:
            grupo = cls(result) # cls() transforma los resultados en instancias de la clase Grupo
            grupos.append(grupo)
        return grupos
    
    @classmethod
    def get(cls, nombre_grupo):
        query = "select * from grupo where nombre_grupo = %(nombre_grupo)s;"
        data = {'nombre_grupo': nombre_grupo}
        mysql = connectToMySQL('curso')
        result = mysql.query_db(query, data)
        if len(result) > 0:
            return cls(result[0])
        else:
            return None

    @classmethod
    def save(cls, data):
        query = "insert into grupo (nombre_grupo, descripcion_grupo) values (%(nombre_grupo)s, %(descripcion_grupo)s);"
        mysql = connectToMySQL('curso')
        mysql.query_db(query, data)
        return cls.get(data['nombre_grupo'])
