from registro_app.config.mysqlconnection import connectToMySQL

# Crearemos una clase llamada Grupo
class Integrante:
    def __init__(self, data):
        self.idIntegrante = data['idIntegrante']
        self.nombre_integrante = data['nombre_integrante']
        self.apellido_integrante = data['apellido_integrante']
        self.idGrupo = data['idGrupo']

    @classmethod
    def get_all(cls):
        query = "select * from integrantes;"
        mysql = connectToMySQL('curso')
        results = mysql.query_db(query) # Conexión a la base de datos
        integrantes = []
        for result in results:
            integrante = cls(result)
            integrantes.append(integrante)
        return integrantes

    @classmethod
    def get(cls, data):
        query = "select * from integrantes where idIntegrante = %(idIntegrante)s;"
        mysql = connectToMySQL('curso')
        result = mysql.query_db(query, data)
        print("Resultado", data)
        if len(result) > 0:
            return cls(result[0])
        else:
            return None

    @classmethod
    def save(cls, data):
        query = "insert into integrantes (nombre_integrante, apellido_integrante, idGrupo) values (%(nombre_integrante)s, NULL, %(idGrupo)s);"
        mysql = connectToMySQL('curso')
        result = mysql.query_db(query, data)
        data_integrante = {'idIntegrante': result}
        return cls.get(data_integrante)
