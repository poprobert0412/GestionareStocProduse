"""Implementam metodele crud pentru tabela products"""
from db.crud.interface_crud import CrudABC


class ProductsDB(CrudABC):
    def __init__(self):
        super().__init__()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

    def create(self, date_de_intrare_create):
        SQL_QUERY = """
            INSERT INTO product(
            id, product_name, description, ingredients, price, weight, quantity)
            VALUES (:id, :product_name, :description, :ingredients, :price, :weight, :quantity)
        """
        cursor = self.connection.cursor()
        cursor.execute(SQL_QUERY, date_de_intrare_create)
        self.connection.commit()

    def read(self, id=None, product_name=None):
        SQL_QUERY = "SELECT * FROM product " #adaugam un spatiu sa nu cumva sa ne dea eroare cand rulam
        value = ""
        if id:
            SQL_QUERY += "WHERE id = ?;"
            value = id
            cursor = self.connection.cursor()
            cursor.execute(SQL_QUERY, (value,))
        elif product_name:
            SQL_QUERY += "WHERE product_name = ?;"
            value = product_name
            cursor = self.connection.cursor()
            cursor.execute(SQL_QUERY, (value,))
        else:
            cursor = self.connection.cursor()
            cursor.execute(SQL_QUERY)
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

    def update(self, date_de_intrare_update,product_id):
        SQL_QUERY = """
            UPDATE product SET product_name:=product_name, description:=description,
            ingredients:=ingredients, price:=price, weight:=weight, quantity:=quantity
            WHERE id:=id;
        """
        cursor = self.connection.cursor()
        date_de_intrare_update['id'] = product_id
        cursor.execute(SQL_QUERY, date_de_intrare_update)
        self.connection.commit()

    def delete(self, id):
        SQL_QUERY = """
            DELETE FROM product WHERE id = ?;
        """
        cursor = self.connection.cursor()
        cursor.execute(SQL_QUERY)
        cursor.execute(SQL_QUERY, (id,))
        self.connection.commit()
