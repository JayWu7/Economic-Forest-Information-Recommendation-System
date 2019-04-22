from . import db, login_manager
from flask_login import UserMixin
from config import PLANTS_COLLECTION as pc
from config import DEMAND_COLLECTION as dc
from config import PER_PAGE_PLANTS


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    mobile_phone = db.Column(db.String(11), unique=True)
    password = db.Column(db.String(20))

    def verify_password(self, password):
        return self.password == password


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Pagination:
    def __init__(self, cursor, page, per_page):
        #: the current cursor object
        self.cursor = cursor
        #: the current page number (1 indexed)
        self.page = page
        #: the number of items to be displayed on a page.
        self.per_page = per_page
        #: the amount of total items
        self.total = self.cursor.count()
        #: the items for the current page
        self.items = self._generate_items()

    def _generate_items(self):  # 从数据库中取出当前页面的items
        former_items = (self.page - 1) * self.per_page
        items = self.cursor.skip(former_items).limit(self.per_page)
        return items

    @property
    def pages(self):
        """The total number of pages"""
        if self.per_page == 0:
            pages = 0
        else:
            pages = self.total / float(self.per_page)
            if pages.is_integer():
                pages = int(pages)
            else:  # 不整除
                pages = int(pages) + 1
        return pages

    def prev(self, error_out=False):
        """Returns a :class:`Pagination` object for the previous page."""
        pass
        # return self.query.paginate(self.page - 1, self.per_page, error_out)

    @property
    def prev_num(self):
        """Number of the previous page."""
        if not self.has_prev:
            return None
        return self.page - 1

    @property
    def has_prev(self):
        """True if a previous page exists"""
        return self.page > 1

    def next(self, error_out=False):
        """Returns a :class:`Pagination` object for the next page."""
        pass
        # return self.query.paginate(self.page + 1, self.per_page, error_out)

    @property
    def has_next(self):
        """True if a next page exists."""
        return self.page < self.pages

    @property
    def next_num(self):
        """Number of the next page"""
        if not self.has_next:
            return None
        return self.page + 1

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        """Iterates over the page numbers in the pagination.  The four
        parameters control the thresholds how many numbers should be produced
        from the sides.  Skipped page numbers are represented as `None`.
        """
        last = 0
        for num in range(1, self.pages + 1):
            if num <= left_edge or \
                    (num > self.page - left_current - 1 and \
                     num < self.page + right_current) or \
                    num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num


class Plants:
    collection = pc

    # def __init__(self, items_dic):
    #     self.title = items_dic['title']
    #     self.name = items_dic['name']
    #     self.other_name = items_dic['other_name']
    #     self.area = items_dic['area']
    #     self.info = items_dic['info']
    #     self.post_time = items_dic['post_time']
    #     self.total_amount = items_dic['total_amount']
    #     self.start_sell_num = items_dic['start_sell_num']
    #     self.price = items_dic['price']
    #     self.pictures = items_dic['pictures']
    #     self.from_url = items_dic['from_url']
    #     self.barcode2D = items_dic['barcode2D']
    #     self.company = items_dic['name']
    #     self.sell_tel = items_dic['sell_tel']
    def __init__(self, mongo, page=1):
        self.cursor = mongo.db[self.collection].find().sort('post_time', -1)
        self.pagination = Pagination(self.cursor, page, per_page=PER_PAGE_PLANTS)
        self.cur_page = self.pagination.items

    def get_cur_plants(self, page=1):  # 获得当前页的plants
        return self.pagination.items
