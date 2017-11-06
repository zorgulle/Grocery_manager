class Config(object):
    DEBUG = False

class DevConfig(Config):
    DEBUG = True
    DB_PATH = '.'
    DB_NAME = 'database.db'

class ProductionConfig(Config):
    DEBUG = False