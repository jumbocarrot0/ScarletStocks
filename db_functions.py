from db_select import *
from excel_to_sql import *
from dateutil.parser import parse
import datetime
from pywintypes import com_error

import progressbar

# --------------- ARCHIVED CODE, NOW USERS KWARG SYSTEM -------------------

# Adds a new user to the database
# def db_user_add(firstname, surname, password, email, phone, dateOfBirth):
#     add_to_sql_table('users', firstname=firstname, surname=surname, password=password, email=email, phone=phone,
#                      dateOfBirth=dateOfBirth)
#     return
#     connie = create_connection()
#     c = connie.cursor()
#     c.execute("INSERT INTO users (firstname, surname, password, email, phone, dateOfBirth) VALUES (?, ?, ?, ?, ?, ?)",
#               (firstname, surname, password, email, phone, dateOfBirth))
#     connie.commit()
#     connie.close()
#
#
# def add_watchlist_sql(userID, code, exchange):
#     add_to_sql_table('watchlists', userID=userID, code=code, exchange=exchange, timeAdded=datetime.now())
#     return
#     connie = create_connection()
#     c = connie.cursor()
#     c.execute("INSERT INTO watchlists (userID, code, exchange, timeAdded) VALUES (?, ?, ?, ?)",
#               (userID, code, exchange, datetime.now()))
#     connie.commit()
#     connie.close()
#
#
# def remove_watchlist_sql(userID, code, exchange):
#     remove_from_sql_table('watchlists', userID=userID, code=code, exchange=exchange)
#     return
#     connie = create_connection()
#     c = connie.cursor()
#     c.execute("DELETE FROM watchlists WHERE userID = ? AND code =? AND exchange=?",
#               (userID, code, exchange))
#     connie.commit()
#     connie.close()
#
#
# def add_portfolio_sql(userID, code, exchange, quantity, price, dateBought, timeBought):
#     dateTimeBought = datetime.strptime(dateBought + timeBought, '%Y-%m-%d%H:%M')
#     add_to_sql_table('portfolios', userID=userID, code=code, exchange=exchange, quantity=quantity,
#                      price=price, timeBought=dateTimeBought, active=1)
#     return
#     connie = create_connection()
#     c = connie.cursor()
#     c.execute("""INSERT INTO portfolios (userID, code, exchange, quantity, price, timeBought, active)
#     VALUES (?, ?, ?, ?, ?, ?, 1)""",
#               (userID, code, exchange, quantity, price, dateTimeBought))
#     connie.commit()
#     connie.close()

# Adds to a table in the database, inserting values in the given columns.
# E.g: add_to_sql_table('users', password=password, email=email) adds a user with a given email and password
# An error is thrown if a column with a 'NOT NULL' parameter is not given a value.


def add_historic_data(ticker, exchange, start_date):
    # It shouldn't be anything other than this
    if exchange != 'Australian Securities Exchange':
        return
    latest_date = select_conditions('historic_prices', 'date',
                                    query_limit=1,
                                    order_by='date DESC',
                                    code=ticker,
                                    exchange='Australian Securities Exchange')

    # Adds a timezone to start_date, as datetime cannot compare dates with and without a timezone
    # (By default the dates in the database have timezones attached
    local_tz = datetime.timezone(datetime.timedelta(hours=10), name='UTC+10')
    start_date = start_date.replace(tzinfo=local_tz)
    print('latest date:', latest_date)
    if len(latest_date) > 0:
        latest_date = datetime.datetime.strptime(latest_date[0]['date'], '%Y-%m-%d %H:%M:%S%z')
        if start_date < latest_date:
            start_date = latest_date + datetime.timedelta(1)
            print('start date:', start_date)
            if start_date > datetime.datetime.now(tz=local_tz):
                return

    stock_history = None
    while stock_history is None:
        # print('stock_history:', stock_history)
        try:
            stock_history = get_historic_data('XASX:' + ticker, start_date)
        except com_error:
            pass
        except noStockData:
            return
    print('stock_history:', stock_history)
    # stock_data[0] is the date, stock_data[1] is the price

    widgets = [progressbar.Counter('Counter: %(value)05d'),
               ' rows committed (', progressbar.Timer(), ') ']
    bar = progressbar.ProgressBar(widgets=widgets)
    for stock_data in bar(stock_history):
        # -2146826246 is what 'N/A' is returned as in win32com, and as such
        # this skips and rows containing them
        if -2146826246 in stock_data:
            continue
        stock_date = parse(str(stock_data[0]))
        stock_price = str(stock_data[1])
        add_to_sql_table('historic_prices',
                         code=ticker,
                         exchange='Australian Securities Exchange',
                         price=stock_price,
                         date=stock_date)


def add_to_sql_table(table, **columns):
    # Constructs the SQL statement given the columns and values
    sql_statement = 'INSERT INTO ' + table + ' ('
    for column in columns:
        sql_statement += column + ', '
    sql_statement = sql_statement[:-2] + ') VALUES (' + ('?, ' * len(columns))[:-2] + ')'

    # Creates a tuple of entry values to be substituted in the statement
    sql_params = tuple(columns.values())

    execute_sql(sql_statement, sql_params)


def update_sql_table(table, conditions={}, **new_values):
    # Constructs the SQL statement given the columns and values
    sql_statement = 'UPDATE ' + table + ' '
    for column in new_values:
        sql_statement += 'SET ' + column + '=?, '
    sql_statement = sql_statement[:-2]
    if conditions:
        sql_statement += ' WHERE '
        for column in conditions:
            sql_statement += column + '=?, '
        sql_statement = sql_statement[:-2]

    # Creates a tuple of entry values to be substituted in the statement
    sql_params = tuple(new_values.values())
    if conditions:
        sql_params += tuple(conditions.values())

    execute_sql(sql_statement, sql_params)


# Removes from a table in the database given the conditions.
# E.g: remove_from_sql_table('stocks', exchange='New York Stock Exchange', currency='AUD')
# would delete every entry where exchange='New York Stock Exchange' and currency='AUD'
def remove_from_sql_table(table, **columns):
    # Constructs the SQL statement given the columns and values
    sql_statement = 'DELETE FROM ' + table + ' WHERE'
    for column in columns:
        sql_statement += ' ' + column + '=? AND'
        sql_statement = sql_statement[:-4]

    # Creates a tuple of entry values to be substituted in the statement
    sql_params = tuple(columns.values())

    execute_sql(sql_statement, sql_params)
