"""Cream metodele pentru ca aplicatia sa fie interactiva"""
from db.db_connection import create_database
from models.product import Product
from db.crud.product_crud import ProductsDB
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
    try:
        produs_nou = Product(product_name, description, ingredients, price, weight, quantity)
        produs_nou.add()
        print("Produs adaugat cu succes in sistem!")
    except Exception as e:
        print(f"Eroare este: {e}")

def update_product(product_id, product_name, description, ingredients, price, weight, quantity):
    try:
        produs_actualizat = Product(id=product_id, product_name=product_name, description=description,
                                    ingredients=ingredients, price=price, weight=weight, quantity=quantity)
        produs_actualizat.update()
        print("Produsul a fost actualizat")
    except Exception as e:
        print(f"Eroarea este: {e}")
def delete_product(product_name):
    try:
        produs_sters = Product(id=product_name, product_name="", description="", ingredients="", price=None,
                               weight=None, quantity=None)
        produs_sters.delete()
        print("Produsul a fost sters din sistem.")
    except Exception as e:
        print(f"Erorea este: {e}")
def all_products():
    products_db = ProductsDB()
    produse = products_db.read()
    for produs in produse:
        print(f"id: {produs['id']}, nume_produs: {produs['product_name']}")

def get_info_products():
    product_name = input("Insert the Product Name: ")
    description = input("Insert Product Description: ")
    ingredients = input("Insert Product ingredients: ")
    price = float(input("Insert Product price: "))
    weight = int(input("Insert Product weight: "))
    quantity = int(input("Insert Product quantity: "))
    return product_name, description, ingredients, price, weight, quantity

def get_info_product_id():
    return input("Enter Product ID: ")


if __name__ == "__main__":
    create_database()
    print("Ce date doresti sa introduci in sistem?")
    print("1. Utilizatori")
    print("2. Produse")
    optiune = input("Introdu una din cele 2 optiuni: ")

    if optiune == "1":
        print("Pentru utilizatori poti face urmatoarele operatiuni:")
    elif optiune == "2":
        print("Pentru produse poti face urmatoarele operatiuni:")
        while True:
            print("1. Add product: ")
            print("2. Update product: ")
            print("3. Delete product: ")
            print("4. List product: ")
            print("5. Exit")

            optiune = input("Scrie numarul operatiunii:")

            if optiune == "1":
                product_name, description, ingredients, price, weight, quantity = get_info_products()
                add_product(product_name, description, ingredients, price, weight, quantity)
                print("Am adaugat produsul.")
            elif optiune == "2":
                product_id = get_info_product_id()
                product_name, description, ingredients, price, weight, quantity = get_info_products()
                update_product(product_id, product_name, description, ingredients, price, weight, quantity)
                print("Am actualizat produsul.")
            elif optiune == "3":
                product_id = get_info_product_id()
                delete_product(product_id)
                print("Am sters produsul.")
            elif optiune == "4":
                all_products()
                print("Lista produselor: ")
            elif optiune == "5":
                break
            else:
                print("Nu exista aceasta optiune. Incearca din nou!")
    else:
        print("Nu exista aceasta optiune. Incearca din nou!")



