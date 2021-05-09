import sqlite3


def create_connection():
    connie = sqlite3.connect('stocks.db')
    return connie
