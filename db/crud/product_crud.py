"""Implementam metodele crud pentru tabela products"""
from db.crud.interface_crud import CrudABC


class ProductsDB(CrudABC):

    def create(self, date_de_intrare_create):
        SQL_QUERY = """
            INSERT INTO product(
            id, product_name, description, ingredients, price, weight, quantity)
            VALUES (:id, :product_name, :description, :ingredients, :price, :weight, :quantity)
        """
        cursor = self.connection.cursor()
        cursor.execute(SQL_QUERY, date_de_intrare_create)
        self.connection.commit()

    def read(self, id=None, product_name=None, description=None, price=None, quantity=None):
        SQL_QUERY = "SELECT * FROM product " #adaugam un spatiu sa nu cumva sa ne dea eroare cand rulam
        value = ""
        if id:
            SQL_QUERY += "WHERE id = ?;"
            value = id
        elif product_name:
            SQL_QUERY += "WHERE product_name = ?;"
            value = product_name
        elif description:
            SQL_QUERY += "WHERE description = ?;"
            value = description
        elif price:
            SQL_QUERY += "WHERE price = ?;"
            value = price
        else:
            SQL_QUERY += "WHERE quantity = ?;"
            value = quantity

        cursor = self.connection.cursor()

        if not value:
            cursor.execute(SQL_QUERY)
        else:
            cursor.execute(SQL_QUERY, (value,))

        product = cursor.fetchall()

        product_json = []
        for prod in product:
            product_json.append({
                "id": prod[0],
                "product_name": prod[1],
                "description": prod[2],
                "ingredients": prod[3],
                "price": prod[4],
                "weight": prod[5],
                "quantity": prod[6]
            })
        return product_json

    def update(self, date_de_intrare_update):
        pass

    def delete(self, id):
        pass
