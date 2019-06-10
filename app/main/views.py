from flask import render_template, request, url_for, redirect
from . import main
from datetime import datetime
from ..models import Plants, Orders, Search
from app import mongo
from config import DEMAND_COLLECTION, PLANTS_COLLECTION
from flask_login import current_user,login_required


@main.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    plants = Plants(mongo, page)
    return render_template('main/index.html', plants=plants.cur_page, pagination=plants.pagination)


@main.route('/supply')
def supply():
    page = request.args.get('page', 1, type=int)
    plants = Plants(mongo, page)
    return render_template('main/supply.html', plants=plants.cur_page, pagination=plants.pagination)


@main.route('/purchase')
def purchase():
    page = request.args.get('page', 1, type=int)
    orders = Orders(mongo, page)
    current_time = str(datetime.now())
    return render_template('main/purchase.html', orders=orders.cur_page, pagination=orders.pagination,
                           current_time=current_time)


@main.route('/order_info/<int:id>')
def order_info(id):
    order = mongo.db[DEMAND_COLLECTION].find_one({'purchase_id': int(id)})
    return render_template('main/order_info.html', order=order)


@main.route('/search', methods=['POST', 'GET'])
def search():
    key_word = request.form['key_word']
    if 'purchase' in request.referrer:
        return redirect(url_for('main.search_purchase', key_word=key_word))
    else:
        return redirect(url_for('main.search_supply', key_word=key_word))


@main.route('/search_supply', methods=['POST', 'GET'])
def search_supply():
    key_word = request.args.get('key_word')
    page = request.args.get('page', 1, type=int)
    if current_user.is_authenticated:
        current_user.add_favorite(key_word)
    content = Search(mongo, key_word, PLANTS_COLLECTION, 'name', page)
    return render_template('main/supply.html', plants=content.cur_page, pagination=content.pagination)

@main.route('/search_purchase', methods=['POST', 'GET'])
def search_purchase():
    key_word = request.args.get('key_word')
    page = request.args.get('page', 1, type=int)
    if current_user.is_authenticated:
        current_user.add_favorite(key_word)
    content = Search(mongo, key_word, DEMAND_COLLECTION, 'kinds', page)
    current_time = str(datetime.now())
    return render_template('main/purchase.html', orders=content.cur_page, pagination=content.pagination,
                           current_time=current_time)