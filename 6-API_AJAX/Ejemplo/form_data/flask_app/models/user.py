from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "user_names"
    def __init__(self, data):
        self.id = data['id']
        self.user_name = data['user_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query  = "INSERT INTO users (user_name, email) VALUES (%(user_name)s,%(email)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_one_by_user_name(cls,data):
        query = "SELECT * FROM users WHERE user_name = %(user_name)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def get_all_json(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for user_data in results:
            users.append( user_data )
        return users