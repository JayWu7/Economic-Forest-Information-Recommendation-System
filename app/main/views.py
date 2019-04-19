from flask import render_template, request, url_for
from . import main
from .. import mongo
from datetime import datetime
from ..models import Plants
from app import app, mongo


@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    plants = Plants(mongo, page)
    return render_template('main/index.html', plants=plants.cur_page, pagination=plants.pagination)
