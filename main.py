"""Cream metodele pentru ca aplicatia sa fie interactiva"""
from db.db_connection import create_database
#Functiile pentru user

def add_user(username, first_name, last_name, email, password):
    pass

def update_user(username, first_name, last_name, email, password):
    pass

def delete_user(id_user):
    pass

def all_users():
    pass

def get_info_user():
    username = input("Enter Your Username: ")
    first_name = input("Your First Name: ")
    last_name = input("Your Last Name: ")
    email = input("Your e-mail address: ")
    password = input("Enter the Password: ")
    return username, first_name, last_name, email, password

def get_info_user_id():
    return input("Enter Your ID: ")



#Functiile pentru PRODUCT

def add_product(product_name, description, ingredients, price, weight, quantity):
    pass

def update_product(product_name, description, ingredients, price, weight, quantity):
    pass

def delete_product(id_product):
    pass

def all_users():
    pass

def get_info_user():
    product_name = input("Insert the Product Name: ")
    description = input("Insert Product Description: ")
    ingredients = input("Insert Product ingredients: ")
    price = input("Insert Product price: ")
    weight = input("Insert Product weight: ")
    quantity = input("Insert Product quantity: ")
    return product_name, description, ingredients, price, weight, quantity

def get_info_product_id():
    return input("Enter Product ID: ")


if __name__ == "__main__":
    create_database()
