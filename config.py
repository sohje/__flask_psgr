class Config(object):
    DEBUG = True
    DATABASE_URI = 'sqlite:///testing.db'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DATABASE_URI = 'postgresql://localhost/testing'
