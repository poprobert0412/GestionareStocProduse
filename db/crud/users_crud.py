"""Implementam metodele crud pentru tabela users"""
from db.crud.interface_crud import CrudABC

class UsersDB(CrudABC):

    def create(self, date_de_intrare_create):
        SQL_QUERY = """
            INSERT INTO users(
            id, username, first_name, last_name, email, password)
            VALUES (:id, :username, :first_name, :last_name, :email, :password)
        """
        cursor = self.connection.cursor()
        cursor.execute(SQL_QUERY, date_de_intrare_create)
        self.connection.commit()

    def read(self, id=None, username=None, email=None):
        SQL_QUERY = "SELECT * FROM users " #adaugam un spatiu sa nu cumva sa ne dea eroare cand rulam
        value = ""
        if id:
            SQL_QUERY += "WHERE id = ?;"
            value = id
            cursor = self.connection.cursor()
            cursor.execute(SQL_QUERY, (value,))
        elif username:
            SQL_QUERY += "WHERE username = ?;"
            value = username
            cursor = self.connection.cursor()
            cursor.execute(SQL_QUERY, (value,))
        else:
            SQL_QUERY += "WHERE email = ?;"
            value = email
            cursor = self.connection.cursor()
            cursor.execute(SQL_QUERY, (value,))

        cursor = self.connection.cursor()
        cursor.execute(SQL_QUERY)
        cursor.execute(SQL_QUERY, (value, ))
        users = cursor.fetchall()
        # print(users)
        user_json = []
        for user in users:
            user_json.append({
                "id": user[0],
                "username": user[1],
                "first_name": user[2],
                "last_name": user[3],
                "email": user[4],
                "password": user[5]
            })
        return user_json


    def update(self, date_de_intrare_update):
        pass

    def delete(self, id):
        pass
