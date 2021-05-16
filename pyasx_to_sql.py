import pyasx.data.companies as Cp
import pyasx.data.securities as Sc
from pyasx.data import UnknownTickerException
from db_functions import *

import progressbar

# Multiprocessing is used to speed up process
from multiprocessing import Pool
from json.decoder import JSONDecodeError


# def update_given_asx_stocks():
#     # Effectively creates a 2nd python instance that runs alongside flask.
#     # Without threading this code couldn't run alongside flask
#     if threading.current_thread().getName() != 'MainThread':
#         pythoncom.CoInitialize()
#         threading.Thread(populate_stocks_table())


# def update_given_asx_stocks(*stock_codes):
#     for ticker in stock_codes:
#         # print(stock['ticker'])
#         try:
#             stock_data = Cp.get_company_info(ticker)
#         except UnknownTickerException:
#             # print(stock['ticker'])
#             continue
#
#         # Prevents stocks with no price data from being added.
#         if stock_data['primary_share']['last_price'] == '':
#             continue
#
#         update_sql_table('stocks',
#                          conditions={'code': stock_data['ticker'], 'exchange': 'ASX'},
#                          code=stock_data['ticker'],
#                          exchange='ASX',
#                          name=stock_data['name'],
#                          price=stock_data['primary_share']['last_price'],
#                          price_day_change=stock_data['primary_share']['day_change_price'],
#                          high52=stock_data['primary_share']['year_high_price'],
#                          low52=stock_data['primary_share']['year_low_price'],
#                          pe=stock_data['primary_share']['pe'],
#                          industry=stock_data['gics_industry'],
#                          # description = stock_data['description'],
#                          marketCap=stock_data['primary_share']['market_cap'],
#                          volume=stock_data['primary_share']['day_volume'],
#                          lastTradeTime=stock_data['primary_share']['last_trade_date'],
#                          website=stock_data['website'],
#                          suspended=stock_data['primary_share']['is_suspended'])
#
#
# def update_all_asx_stocks():
#     # Read to a dataframe
#     stocks_data = Cp.get_listed_companies()
#     current_stocks = [i['code'] for i in select_conditions('stocks', 'code', exchange='ASX')]
#
#     for stock in stocks_data:
#         # print(stock['ticker'])
#         try:
#             stock_data = Cp.get_company_info(stock['ticker'])
#         except UnknownTickerException:
#             # print(stock['ticker'])
#             continue
#
#         # Prevents stocks with no price data from being added.
#         if stock_data['primary_share']['last_price'] == '':
#             continue
#
#         if stock_data['ticker'] in current_stocks:
#             add_to_sql_table('stocks',
#                              code=stock_data['ticker'],
#                              exchange='ASX',
#                              name=stock_data['name'],
#                              price=stock_data['primary_share']['last_price'],
#                              price_day_change=stock_data['primary_share']['day_change_price'],
#                              high52=stock_data['primary_share']['year_high_price'],
#                              low52=stock_data['primary_share']['year_low_price'],
#                              pe=stock_data['primary_share']['pe'],
#                              industry=stock_data['gics_industry'],
#                              # description = stock_data['description'],
#                              marketCap=stock_data['primary_share']['market_cap'],
#                              volume=stock_data['primary_share']['day_volume'],
#                              lastTradeTime=stock_data['primary_share']['last_trade_date'],
#                              website=stock_data['website'],
#                              suspended=stock_data['primary_share']['is_suspended'])
#         else:
#             update_sql_table('stocks',
#                              conditions={'code': stock_data['ticker'], 'exchange': 'ASX'},
#                              code=stock_data['ticker'],
#                              exchange='ASX',
#                              name=stock_data['name'],
#                              price=stock_data['primary_share']['last_price'],
#                              price_day_change=stock_data['primary_share']['day_change_price'],
#                              high52=stock_data['primary_share']['year_high_price'],
#                              low52=stock_data['primary_share']['year_low_price'],
#                              pe=stock_data['primary_share']['pe'],
#                              industry=stock_data['gics_industry'],
#                              # description = stock_data['description'],
#                              marketCap=stock_data['primary_share']['market_cap'],
#                              volume=stock_data['primary_share']['day_volume'],
#                              lastTradeTime=stock_data['primary_share']['last_trade_date'],
#                              website=stock_data['website'],
#                              suspended=stock_data['primary_share']['is_suspended'])


def get_stock_data(ticker):
    try:
        stock_data = Cp.get_company_info(ticker)
        if stock_data['primary_share']['last_price'] == '':
            return {}
        sql_data = {'code': stock_data['ticker'],
                    'exchange': 'ASX',
                    'name': stock_data['name'],
                    'price': stock_data['primary_share']['last_price'],
                    'price_day_change': stock_data['primary_share']['day_change_price'],
                    'high52': stock_data['primary_share']['year_high_price'],
                    'low52': stock_data['primary_share']['year_low_price'],
                    'pe': stock_data['primary_share']['pe'],
                    'industry': stock_data['gics_industry'],
                    # description : stock_data['description'],
                    'marketCap': stock_data['primary_share']['market_cap'],
                    'volume': stock_data['primary_share']['day_volume'],
                    'lastTradeTime': stock_data['primary_share']['last_trade_date'],
                    'website': stock_data['website'],
                    'suspended': stock_data['primary_share']['is_suspended']}
        return sql_data
    except KeyError as e:
        print(repr(e))
        print(ticker)
        return {}
    except JSONDecodeError as e:
        print(repr(e))
        print(ticker)
        return {}


def update_given_asx_stocks(ticker_list):
    current_stocks = [i['code'] for i in select_conditions('stocks', 'code', exchange='ASX')]
    stocks_to_update = [i for i in ticker_list if i in current_stocks]
    stocks_to_add = [i for i in ticker_list if i not in current_stocks]

    print('add:', stocks_to_add)
    print('update:', stocks_to_update)

    if __name__ == '__main__':
        with Pool() as p:
            sql_data_add = p.imap_unordered(get_stock_data, stocks_to_add, 10)
            sql_data_update = p.imap_unordered(get_stock_data, stocks_to_update, 10)

        # Fancy method to remove any None values, i.e. stocks that had missing data
        sql_data_add = list(filter({}.__ne__, sql_data_add))
        sql_data_update = list(filter({}.__ne__, sql_data_update))

        print('add:', sql_data_add)
        print('update:', sql_data_update)

        for row in sql_data_add:
            add_to_sql_table('stocks', exchange='ASX', **row)
        for row in sql_data_update:
            update_sql_table('stocks', conditions={'code': row['code'], 'exchange': 'ASX'}, exchange='ASX', **row)
