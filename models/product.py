"""Cream modelul(obiectul) pentru aplicatia noastra (gestionare stoc produse)"""
from db.crud.product_crud import ProductsDB

class Product:
    def __init__(self, id, product_name, description, ingredients, price, weight, quantity):
        self.id = id
        self.product_name = product_name
        self.description = description
        self.ingredients = ingredients
        self.price = price
        self.weight = weight
        self.quantity = quantity
        self.user_db = ProductsDB

    def add(self):
        product_data = self.dict_product
        with ProductsDB() as db:
            db.create(product_data)

    def dict_product(self):
        return {
            "id": self.id,
            "product_name": self.product_name,
            "description": self.description,
            "ingredients": self.ingredients,
            "price": self.price,
            "weight": self.weight,
            "quantity": self.quantity,
        }
