import pyasx.data.companies as Cp
import pyasx.data.securities as Sc
from pyasx.data import UnknownTickerException
from db_functions import *

import progressbar


def wipe_stocks_data():
    connie = create_connection()
    c = connie.cursor()
    c.execute('DELETE FROM stocks')
    connie.commit()
    connie.close()


# def update_given_asx_stocks():
#     # Effectively creates a 2nd python instance that runs alongside flask.
#     # Without threading this code couldn't run alongside flask
#     if threading.current_thread().getName() != 'MainThread':
#         pythoncom.CoInitialize()
#         threading.Thread(populate_stocks_table())


def update_given_asx_stocks(*stock_codes):
    format_stock_name = progressbar.FormatCustomText(
        'Current Stock: %(stock)s',
        dict(
            stock='N/A'
        ),
    )
    widgets = [progressbar.Counter('Counter: %(value)05d'),
               ' stocks refreshed (', progressbar.Timer(), ') ', format_stock_name]
    bar = progressbar.ProgressBar(widgets=widgets)
    for ticker in bar(stock_codes):
        format_stock_name.update_mapping(stock=ticker)
        # print(stock['ticker'])
        try:
            stock_data = Cp.get_company_info(ticker)
        except UnknownTickerException:
            # print(stock['ticker'])
            continue

        # Prevents stocks with no price data from being added.
        if stock_data['primary_share']['last_price'] == '':
            continue

        update_sql_table('stocks',
                         conditions={'code': stock_data['ticker'], 'exchange': 'ASX'},
                         code=stock_data['ticker'],
                         exchange='ASX',
                         name=stock_data['name'],
                         price=stock_data['primary_share']['last_price'],
                         price_day_change=stock_data['primary_share']['day_change_price'],
                         high52=stock_data['primary_share']['year_high_price'],
                         low52=stock_data['primary_share']['year_low_price'],
                         pe=stock_data['primary_share']['pe'],
                         industry=stock_data['gics_industry'],
                         # description = stock_data['description'],
                         marketCap=stock_data['primary_share']['market_cap'],
                         volume=stock_data['primary_share']['day_volume'],
                         lastTradeTime=stock_data['primary_share']['last_trade_date'],
                         website=stock_data['website'],
                         suspended=stock_data['primary_share']['is_suspended'])


def update_all_asx_stocks():
    # Read to a dataframe
    stocks_data = Cp.get_listed_companies()
    current_stocks = [i['code'] for i in select_conditions('stocks', 'code', exchange='ASX')]

    format_stock_name = progressbar.FormatCustomText(
        'Current Stock: %(stock)s',
        dict(
            stock='N/A'
        ),
    )
    widgets = [progressbar.Counter('Counter: %(value)05d'),
               ' stocks refreshed (', progressbar.Timer(), ') ', format_stock_name]
    bar = progressbar.ProgressBar(widgets=widgets)
    for stock in bar(stocks_data):
        format_stock_name.update_mapping(stock=stock['ticker'])
        # print(stock['ticker'])
        try:
            stock_data = Cp.get_company_info(stock['ticker'])
        except UnknownTickerException:
            # print(stock['ticker'])
            continue

        # Prevents stocks with no price data from being added.
        if stock_data['primary_share']['last_price'] == '':
            continue

        if stock_data['ticker'] in current_stocks:
            add_to_sql_table('stocks',
                             code=stock_data['ticker'],
                             exchange='ASX',
                             name=stock_data['name'],
                             price=stock_data['primary_share']['last_price'],
                             price_day_change=stock_data['primary_share']['day_change_price'],
                             high52=stock_data['primary_share']['year_high_price'],
                             low52=stock_data['primary_share']['year_low_price'],
                             pe=stock_data['primary_share']['pe'],
                             industry=stock_data['gics_industry'],
                             # description = stock_data['description'],
                             marketCap=stock_data['primary_share']['market_cap'],
                             volume=stock_data['primary_share']['day_volume'],
                             lastTradeTime=stock_data['primary_share']['last_trade_date'],
                             website=stock_data['website'],
                             suspended=stock_data['primary_share']['is_suspended'])
        else:
            update_sql_table('stocks',
                             conditions={'code': stock_data['ticker'], 'exchange': 'ASX'},
                             code=stock_data['ticker'],
                             exchange='ASX',
                             name=stock_data['name'],
                             price=stock_data['primary_share']['last_price'],
                             price_day_change=stock_data['primary_share']['day_change_price'],
                             high52=stock_data['primary_share']['year_high_price'],
                             low52=stock_data['primary_share']['year_low_price'],
                             pe=stock_data['primary_share']['pe'],
                             industry=stock_data['gics_industry'],
                             # description = stock_data['description'],
                             marketCap=stock_data['primary_share']['market_cap'],
                             volume=stock_data['primary_share']['day_volume'],
                             lastTradeTime=stock_data['primary_share']['last_trade_date'],
                             website=stock_data['website'],
                             suspended=stock_data['primary_share']['is_suspended'])

# print(Cp.get_listed_companies())
# sd = Cp.get_company_info('ANZ')
# print(sd)
# print(sd['primary_share']['last_price'])
# print(sd['primary_share']['day_change_price'])
# print(sd['primary_share']['year_high_price'])
# print(sd['primary_share']['year_low_price'])
# print(sd['primary_share']['is_suspended'])

# update_all_asx_stocks()
