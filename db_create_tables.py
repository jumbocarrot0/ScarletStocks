from db_deets import *

connie = create_connection()
c = connie.cursor()


def create_stocks_excel_table():
    c.execute('''
    CREATE TABLE IF NOT EXISTS stocks_excel(
    code TEXT NOT NULL,
    exchange TEXT NOT NULL,
    name TEXT NOT NULL,
    price DECIMAL(20, 2) NOT NULL,
    pctChange DECIMAL(6, 2) NOT NULL,
    high52 DECIMAL(20, 2) NOT NULL,
    low52 DECIMAL(20, 2) NOT NULL,
    pe DECIMAL(20, 2) NOT NULL,
    industry TEXT,
    description TEXT,
    marketCap INTEGER,
    volume INTEGER,
    lastTradeTime TEXT NOT NULL,
    PRIMARY KEY (code, exchange)
    )
    ''')


def create_stocks_table():
    c.execute('''
    CREATE TABLE IF NOT EXISTS stocks(
    code TEXT NOT NULL,
    exchange TEXT NOT NULL,
    name TEXT NOT NULL,
    price DECIMAL(20, 2) CHECK(price >= 0),
    price_day_change DECIMAL(20, 2) NOT NULL,
    high52 DECIMAL(20, 2) CHECK(high52 >= 0),
    low52 DECIMAL(20, 2) CHECK(low52 >= 0),
    pe DECIMAL(20, 2) NOT NULL,
    suspended INTEGER CHECK(0 == suspended or suspended == 1),
    industry TEXT,
    description TEXT,
    marketCap INTEGER,
    volume INTEGER,
    lastTradeTime TEXT NOT NULL,
    website TEXT,
    PRIMARY KEY("code","exchange") -- This is the only way to get multiple primary keys
    )
    ''')


def create_users_table():
    c.execute('''
    CREATE TABLE IF NOT EXISTS users(
    userId INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    surname TEXT,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone INTEGER,
    dateOfBirth TEXT
    )''')


def create_watchlist_table():
    c.execute('''
    CREATE TABLE IF NOT EXISTS watchlists(
    userId INTEGER NOT NULL,
    code TEXT NOT NULL,
    exchange TEXT NOT NULL,
    timeAdded TEXT NOT NULL
    --FOREIGN KEY(userId) REFERENCES users(userId),
    --FOREIGN KEY(code) REFERENCES stocks(code),
    --FOREIGN KEY(exchange) REFERENCES stocks(exchange)
    )''')


def create_portfolio_table():
    c.execute('''
    CREATE TABLE IF NOT EXISTS portfolios(
    userId INTEGER NOT NULL,
    code TEXT NOT NULL,
    exchange TEXT NOT NULL,
    price FLOAT NOT NULL,
    quantity INTEGER NOT NULL,
    timeBought TEXT,
    active INTEGER CHECK(0 <= active <= 1),
    timeSold TEXT,
    soldPrice FLOAT
    )''')


def create_historic_prices_table():
    c.execute('''
    CREATE TABLE IF NOT EXISTS historic_prices(
    code TEXT NOT NULL,
    exchange TEXT NOT NULL,
    price FLOAT NOT NULL,
    date TEXT
    )''')


def create_exchanges_table():
    c.execute('''
    CREATE TABLE IF NOT EXISTS exchanges(
    exchange TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    excelCode TEXT NOT NULL,
    currencyCode TEXT NOT NULL
    )''')


def create_currencies_table():
    c.execute('''
    CREATE TABLE IF NOT EXISTS currencies(
    currencyCode TEXT PRIMARY KEY,
    name TEXT NOT NULL
    )''')


def create_stocksdb():
    create_stocks_table()
    create_users_table()
    create_watchlist_table()
    create_portfolio_table()
    create_historic_prices_table()
    create_exchanges_table()
    create_currencies_table()


create_stocksdb()

connie.commit()
connie.close()
