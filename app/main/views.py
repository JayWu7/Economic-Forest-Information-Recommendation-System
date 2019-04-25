from flask import render_template, request, url_for
from . import main
from datetime import datetime
from ..models import Plants, Orders
from app import mongo


@main.route('/')
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
