from db_deets import *


def execute_sql(sql_statement, sql_params):
    # Creates connection, executes code and commits changes
    connie = create_connection()
    c = connie.cursor()
    # print(sql_statement)
    c.execute(sql_statement, sql_params)
    # Collects any selected data
    data = c.fetchall()
    try:
        header_data = query_table_columns(c)
        for row in range(0, len(data)):
            data[row] = dict(zip(header_data, data[row]))
    except TypeError:
        pass
    connie.commit()
    connie.close()

    return data


def query_table_columns_by_table(table):
    connie = create_connection()
    c = connie.cursor()
    c.execute("SELECT NAME FROM PRAGMA_TABLE_INFO('" + table + "')")
    header_data = []
    for item in c.fetchall():
        header_data.append(item[0])
    return header_data


def query_table_columns(cursor):
    header_data = [i[0] for i in cursor.description]
    return header_data


def select_table_size(table):
    data = execute_sql("SELECT Count(*) FROM " + table, ())
    return data[0]['Count(*)']


def select_all():
    data = execute_sql("SELECT * FROM stocks ORDER BY code", ())
    return data


def select_many(min, max):
    data = execute_sql("SELECT * FROM stocks ORDER BY code LIMIT ? OFFSET ?", (max - min, min))
    return data


def select_watchlist(userId, idOnly=False):
    if idOnly:
        sql_query = """SELECT stocks.code, stocks.exchange FROM watchlists 
        LEFT OUTER JOIN stocks ON watchlists.code = stocks.code
        WHERE watchlists.exchange = stocks.exchange AND watchlists.userId = ?"""
    else:
        sql_query = """SELECT stocks.*, timeAdded FROM watchlists 
        LEFT OUTER JOIN stocks ON watchlists.code = stocks.code
        WHERE watchlists.exchange = stocks.exchange AND watchlists.userId = ?"""
    sql_params = (userId,)

    data = execute_sql(sql_query, sql_params)
    return data


def select_portfolio(userId, idOnly=False):
    connie = create_connection()
    c = connie.cursor()
    if idOnly:
        sql_query = """SELECT stocks.code, stocks.exchange FROM portfolios 
        LEFT OUTER JOIN stocks ON portfolios.code = stocks.code
        WHERE portfolios.exchange = stocks.exchange AND portfolios.userId = ?"""
    else:
        sql_query = """SELECT portfolios.*, (stocks.price - portfolios.price) * quantity AS profit, 
        stocks.name, stocks.price AS 'Current Price', price_day_change/stocks.price AS pctChange, 
        stocks.currency, stocks.lastTradeTime FROM portfolios 
        LEFT OUTER JOIN stocks ON portfolios.code = stocks.code
        WHERE portfolios.exchange = stocks.exchange AND portfolios.userId = ?"""
    sql_params = (userId,)

    data = execute_sql(sql_query, sql_params)
    return data


def select_search(input):
    data = execute_sql("SELECT * FROM stocks WHERE name LIKE ?", ('%' + input + '%',))
    return data


def select_specific_columns(table, *columns):
    sql_query = 'SELECT '
    for column in columns:
        sql_query += column + ','
    sql_query = sql_query[:-1] + ' FROM ' + table
    # print(sql_query)
    data = execute_sql(sql_query, ())
    return data


def select_one(exchange, ticker):
    data = execute_sql('SELECT * FROM stocks WHERE exchange == ? AND code == ?', (exchange, ticker))
    return data


def select_conditions(table, *selected_columns, query_limit=None, order_by=None, **conditions):
    sql_query = 'SELECT '
    for column in selected_columns:
        sql_query += column + ', '
    sql_query = sql_query[:-2] + ' FROM ' + table
    if conditions:
        sql_query += ' WHERE '
        for condition in conditions:
            sql_query += condition + ' = ? AND '
        sql_query = sql_query[:-5]
    if order_by:
        if conditions:
            sql_query += ' AND '
        else:
            sql_query += ' WHERE '
        # Also excludes values in the order_by column that are NULL as it interferes with ORDER BY
        sql_query += order_by.replace(' DESC', '').replace(' ASC', '') + ' NOT NULL ORDER BY ' + order_by
    if query_limit:
        sql_query += ' LIMIT ' + str(query_limit)
    sql_params = tuple([conditions[i] for i in conditions])
    # print(sql_query, sql_params)
    data = execute_sql(sql_query, sql_params)
    return data
