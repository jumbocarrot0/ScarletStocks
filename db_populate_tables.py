from db_functions import *

connie = create_connection()
c = connie.cursor()


def populate_currencies():
    c.execute('''
    INSERT INTO currencies VALUES 
    ('AUD', 'Australian Dollar'), 
    ('USD', 'United States Dollar');''')


def populate_exchanges():
    c.execute('''
    INSERT INTO exchanges VALUES 
    ('ASX', 'Australian Stock Exchange', 'XASX', 'AUD'), 
    ('NYSE', 'New York Stock Exchange', 'XNYS', 'USD'), 
    ('NASDAQ', 'Nasdaq Stock Market', 'XNAS', 'USD'),
    ('NYSEAMERICAN', 'NYSE American', 'XNYS', 'USD');''')


populate_currencies()
populate_exchanges()

connie.commit()
connie.close()
