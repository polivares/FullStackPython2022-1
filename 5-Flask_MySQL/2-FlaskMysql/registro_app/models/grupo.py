from registro_app.config.mysqlconnection import connectToMySQL
from registro_app.models import integrante

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
    def get(cls, data):
        query = "select * from grupo where idGrupo = %(idGrupo)s;"
        mysql = connectToMySQL('curso')
        result = mysql.query_db(query, data)
        if len(result) > 0:
            return cls(result[0])
        else:
            return None

    @classmethod
    def get_integrantes_by_group(cls, data):
        query = "select idIntegrante from grupo join integrantes on grupo.idGrupo = integrantes.idGrupo where grupo.idGrupo = %(idGrupo)s;"
        mysql = connectToMySQL('curso')
        results = mysql.query_db(query, data)
        integrantes = []
        print('resultados',results)
        for result in results:
            data_integrante = {'idIntegrante': result['idIntegrante']}
            integrantes.append(integrante.Integrante.get(data_integrante))
        return integrantes

    @classmethod
    def save(cls, data):
        query = "insert into grupo (nombre_grupo, descripcion_grupo) values (%(nombre_grupo)s, %(descripcion_grupo)s);"
        mysql = connectToMySQL('curso')
        result = mysql.query_db(query, data)
        data_grupo = {'idGrupo': result}
        return cls.get(data_grupo)
        
