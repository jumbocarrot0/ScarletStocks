from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from os import environ
from hashlib import sha224
from db_functions import *
from pyasx_to_sql import *
from yahoo_to_sql import *
import json
from datetime import datetime
from math import ceil

app = Flask(__name__)
login_manager = LoginManager(app)
login_manager.init_app(app)

# ---------------------------------LOGIN SETUP------------------------------------------

sqla_db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# set the type and location of the DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocks.db'
# make sure this key stays secret
app.config['SECRET_KEY'] = environ.get('SECRET_KEY') or sha224(b'A very hard t0 guess password').hexdigest()


# class name has to match the table name
# class variables must match the column names of the table
# one column must be called 'id'
class Users(UserMixin, sqla_db.Model):
    userId = sqla_db.Column(sqla_db.Integer, primary_key=True)
    id = userId  # Required for flask_login to function
    email = sqla_db.Column(sqla_db.String)
    password = sqla_db.Column(sqla_db.String)
    firstname = sqla_db.Column(sqla_db.String)
    surname = sqla_db.Column(sqla_db.String)
    phone = sqla_db.Column(sqla_db.Integer)
    dateOfBirth = sqla_db.Column(sqla_db.String)

    def set_password(self, password):
        self.Password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


# Adding a user from here is easier than from sql_functions.py
def add_user(firstname, surname, password, email, phone, dateOfBirth):
    # Encrypts the password, so that the password is meaningless when directly accessed in the SQLite3 database
    password = generate_password_hash(password)
    add_to_sql_table('users', firstname=firstname, surname=surname, password=password, email=email, phone=phone,
                     dateOfBirth=dateOfBirth)


# should be set to refer to the class name as above
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


# ----------------------- Context Processors -----------------------------

# Context processors allow for variables and functions to be injected into Jinja templates
# This one creates a 'global variable' for stocks to be used in the search bar's auto-fill.
@app.context_processor
def inject_stock_names():
    stock_data = select_specific_columns('stocks', 'code', 'exchange', 'name')
    return dict(global_stock_data=stock_data)


# This one gives a list of stocks in the user's watchlists. This is not strictly
# necessary but is less hassle than putting on every possible route it could appear on.
@app.context_processor
def inject_watchlist():
    if current_user.is_authenticated:
        watchlist_data_raw = select_watchlist(current_user.id, idOnly=True)
        watchlist_data = {}
        for stock in watchlist_data_raw:
            if stock['exchange'] not in watchlist_data:
                watchlist_data[stock['exchange']] = []
            watchlist_data[stock['exchange']].append(stock['code'])
    else:
        watchlist_data = []
    print(watchlist_data)
    return dict(watchlist_data=watchlist_data)


# --------------------------------- ROUTES ------------------------------------

@app.route('/')
def home_route():
    pctChangeColumn = 'price_day_change/price AS pctChange'
    best_change = select_conditions('stocks', 'code', 'exchange', 'name', 'lastTradeTime', pctChangeColumn,
                                    query_limit=1, order_by='pctChange DESC')[0]
    worst_change = select_conditions('stocks', 'code', 'exchange', 'name', 'lastTradeTime', pctChangeColumn,
                                     query_limit=1, order_by='pctChange ASC')[0]
    biggest_volume = select_conditions('stocks', 'code', 'exchange', 'name', 'lastTradeTime', 'volume',
                                       query_limit=1, order_by='volume DESC')[0]
    stock_data = {'best': {'data': best_change},
                  'worst': {'data': worst_change},
                  'biggest_volume': {'data': biggest_volume}}
    return render_template('dashboard.html', title='ScarletStocks - Home', stock_data=stock_data,
                           abstain_margin=True)


@app.route('/search', methods=['GET'])
def search_route():
    search_input = request.args.get('search')
    results = select_search(search_input)
    if len(results) == 1:
        return redirect(url_for('profile_route', ticker=results[0]['code'], exchange=results[0]['exchange']))
    else:
        if len(results) == 0:
            flash('''Your search - "''' + str(search_input) + '''" - did not match any documents.
                        Make sure that all words are spelled correctly. 
                        Otherwise, Try different keywords or more general keywords.''')
        return render_template('search_results.html',
                               output_results=results,
                               search_input=search_input)


@app.route('/stocklist')
def exchangelist_route():
    return 'Exchanges here'
    # return render_template('stocklist.html', title='ScarletStocks - Exchanges')


@app.route('/stocklist/<exchange>/browse/<page>')
def stocklist_route(exchange, page):
    # Prevents generating url where page is not a valid number
    # (a valid number being between 1 and the number of stocks / 100 rounded up.
    try:
        page = int(page)
    except ValueError:
        abort(404)
    page_count = ceil(select_table_size('stocks') / 100)
    if page <= 0 or page > page_count:
        abort(404)
    stock_data = select_conditions('stocks', '*', query_limit=100, query_offset=100 * (page - 1), order_by='code',
                                   exchange=exchange)
    # for row in stock_data:
    #     del row['description']
    return render_template('stocklist.html', title='ScarletStocks - ' + exchange,
                           exchange=exchange,
                           stock_data=stock_data,
                           heading='Stock List',
                           page_count=page_count,
                           current_page=page)


@app.route('/stocklist/<exchange>/<ticker>')
def profile_route(exchange, ticker):
    # Google auto replaces ' ' with '%20' in URLs, which breaks SQL code.
    # This must be reversed before substituting into SQL.
    stock_data = select_one(exchange.replace('%20', ' '), ticker)[0]
    return render_template('profile.html', title='ScarletStocks - ' + stock_data['name'],
                           stock_data=stock_data)


@app.route('/watchlist')
@login_required
def watchlist_route():
    stock_data = select_watchlist(userId=current_user.id)
    # for row in stock_data:
    #     del row['description']
    return render_template('stocklist.html', title='ScarletStocks - Watchlist', stock_data=stock_data,
                           heading='Your Watchlist',
                           page_count=1)


@app.route('/portfolio')
@login_required
def portfolio_route():
    stock_data = select_portfolio(userId=current_user.id)
    for stock in stock_data:
        del stock['userId']
    return render_template('stocklist.html', title='ScarletStocks - Portfolio', stock_data=stock_data,
                           heading='Your Portfolio',
                           page_count=1)


@app.route('/portfolio/add', methods=["POST", "GET"])
@login_required
def portfolio_add_route():
    if request.method == "POST":
        input_data = dict(request.form)
        exchange, code, quantity, price, dateBought, timeBought = input_data.values()
        dateTimeBought = datetime.strptime(dateBought + timeBought, '%Y-%m-%d%H:%M')
        add_to_sql_table('portfolios', userID=current_user.id, code=code, exchange=exchange, quantity=quantity,
                         price=price, timeBought=dateTimeBought, active=1)
        return redirect(url_for('portfolio_route'))
    elif request.method == "GET":
        current_time = {'date': datetime.now().strftime('%Y-%m-%d'), 'time': datetime.now().strftime('%H:%M')}
        return render_template('portfolio_add.html', title='ScarletStocks - Portfolio', current_time=current_time)


@app.route('/top5')
def top5_route():
    pctChangeColumn = 'price_day_change/price AS pctChange'
    stock_data = select_conditions('stocks', 'code', 'exchange', 'name', 'lastTradeTime', pctChangeColumn,
                                   query_limit=5, order_by='pctChange DESC')
    return render_template('stocklist.html', title='ScarletStocks - Top5',
                           stock_data=stock_data, heading='TOP 5',
                           page_count=1)


@app.route('/bottom5')
def bottom5_route():
    pctChangeColumn = 'price_day_change/price AS pctChange'
    stock_data = select_conditions('stocks', 'code', 'exchange', 'name', 'lastTradeTime', pctChangeColumn,
                                   query_limit=5, order_by='pctChange ASC')
    return render_template('stocklist.html', title='ScarletStocks - Bottom5',
                           stock_data=stock_data, heading='BOTTOM 5',
                           page_count=1)


@app.route('/login', methods=["POST", "GET"])
def login_route():
    if request.method == "POST":
        input_data = dict(request.form)
        error_message = '''Invalid credentials, the email or password you supplied was incorrect. 
        Please double check them before attempting to log back in'''
        # Backend email validation
        if len(input_data['inputEmail'].split('@')) != 2:
            flash(error_message)
            return redirect(request.url)

        try:
            # Selects user with the given email
            MyUser = Users.query.filter_by(email=input_data['inputEmail']).first()
        except:
            flash(error_message)
            return redirect(request.url)

        if MyUser is not None:
            # Checks that password matches the hashed password in the database
            if MyUser.check_password(input_data['inputPassword']):
                if current_user.is_authenticated:
                    logout_user()
                login_user(MyUser)
                return redirect(url_for('home_route'))
            else:
                flash(error_message)
                return redirect(request.url)
        else:
            flash(error_message)
            return redirect(request.url)
    elif request.method == "GET":
        return render_template('login.html', title='ScarletStocks - Login')


@app.route('/register', methods=["POST", "GET"])
def register_route():
    if request.method == "POST":
        input_data = dict(request.form)
        # Backend email validation
        if len(input_data['inputEmail'].split('@')) != 2:
            flash('Your email is invalid')
            return redirect(url_for('register_route'))

        # Creates a list of entered emails that will be checked against
        # the entered  email to prevent duplicate emails.
        user_emails = select_specific_columns('users', 'email')

        if input_data['inputEmail'] in user_emails:
            flash('The email provided is already being used. Please select another one')
            return redirect(url_for('register_route'))
        else:
            add_user(input_data['inputFirstname'],
                     input_data['inputSurname'],
                     input_data['inputPassword'],
                     input_data['inputEmail'],
                     input_data['inputPhone'],
                     input_data['inputDateOfBirth'])

            # Too insecure for final build. At best, need email validation to validate account.
            MyUser = Users.query.filter_by(email=input_data['inputEmail']).first()
            login_user(MyUser)
            return redirect(url_for('home_route'))

    elif request.method == "GET":
        return render_template('register.html', title='ScarletStocks - Register')


@app.route('/logout')
@login_required
def logout_route():
    logout_user()
    return redirect(url_for('home_route'))


# If user loads a page with an invalid URL, redirects to the home page
@app.errorhandler(404)
def invalid_page(e):
    if 'favicon.ico' not in request.url:
        flash('Unknown or invalid URL: "' + request.url + '"')
    return redirect(url_for('home_route'))


# Loads this page if an internal server error happens.
@app.errorhandler(500)
def invalid_page(e):
    return render_template('500error.html')


# Redirects user to login page if they access any login-restricted page.
@app.errorhandler(401)
def invalid_page(e):
    if current_user.is_authenticated:
        return redirect(url_for('home_route'))
    else:
        return redirect(url_for('login_route'))


# ------------------------------- AJAX Queries ------------------------------------------


@app.route('/return_historic_data', methods=['POST'])
def ajax_get_historic_data():
    code = request.form['code']
    exchange = request.form['exchange']
    # THIS MAKES WEBSITE SLOW
    add_historic_data(code, exchange, datetime(2016, 1, 1))
    # print(stock_data)
    stock_history = select_conditions('historic_prices', 'price', 'date', order_by='date DESC', query_limit=30,
                                      code=code, exchange=exchange)
    stock_history.reverse()
    chart_data = [{'t': p['date'][:10], 'y': p['price']} for p in stock_history]
    chart_labels = [p['date'][:10] for p in stock_history]
    output_data = [chart_data, chart_labels]
    return json.dumps(output_data)


@app.route('/update_stocks_data', methods=['POST'])
def ajax_update_stocks():
    visible_codes = request.form['visibleCodes']
    exchange = request.form['exchange']
    if exchange == 'ASX':
        update_given_asx_stocks(visible_codes)
    elif exchange == 'NYSE':
        update_all_nyse_stocks()
    elif exchange == 'NASDAQ':
        update_all_nasdaq_stocks()
    elif exchange == 'NYSEAMERICAN':
        update_all_amex_stocks()
    else:
        return json.dumps('error')
    print(visible_codes)
    return json.dumps('success')


@app.route('/return_stocks_data', methods=['POST'])
def ajax_get_stock_data():
    code = request.form['code']
    exchange = request.form['exchange']

    stock_data = select_one(exchange, code)

    return json.dumps(stock_data)


@app.route('/modify_watchlist', methods=['POST'])
def modify_watchlist():
    code = request.form['code']
    exchange = request.form['exchange']
    instruction = request.form['instruction']
    if instruction == 'add':
        add_to_sql_table('watchlists', userID=current_user.id, code=code, exchange=exchange, timeAdded=datetime.now())
    elif instruction == 'remove':
        remove_from_sql_table('watchlists', userID=current_user.id, code=code, exchange=exchange)
    return 'Success'


if __name__ == '__main__':
    app.run()
