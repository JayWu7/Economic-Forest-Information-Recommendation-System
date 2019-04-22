import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jaysinging'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
                              'sqlite:////' + os.path.join(basedir, 'data-dev.sqlite')
    MONGO_URI = "mongodb://localhost:27017/itao"


config = {
    'development': DevelopmentConfig
}

# mongo collection config
PLANTS_COLLECTION = 'CrawelsPlantsItem'
DEMAND_COLLECTION = 'CrawelsDemandItem'

# nums of plant items show in one page, best be the multiple of 3
PER_PAGE_PLANTS = 15
