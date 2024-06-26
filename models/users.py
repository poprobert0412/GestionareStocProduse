"""Cream modelul(obiectul) pentru aplicatia noastra (gestionare stoc produse)"""
from db.crud.users_crud import UsersDB

class Users:
    def __init__(self, username, first_name, last_name, email, password, id=None):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.user_db = UsersDB

    def add(self):
        user_data = self.dict_user
        with UsersDB() as db:
            db.create(user_data)
    def delete_user(self):
        if not self.id:
            raise Exception("Avem nevoie de id pentru a sterge utilizatorul!")
        self.user_db.delete(self.id)

    def dict_user(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
        }

