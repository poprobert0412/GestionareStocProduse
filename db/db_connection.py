"""Cream conexiunea catre baza de date"""

import sqlite3

PATH_DB = "gestionare_stoc_produse.db"

def get_db_connection(db_path = PATH_DB):
    connection = sqlite3.connect(db_path)
    return connection

def create_tables(connection):
    create_user_table(connection)
    create_product_table(connection)

def create_user_table(connection):
    pass

def create_product_table(connection):
    pass

