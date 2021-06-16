import os

class Config:
    # UPLOADED_PHOTOS_DEST ='app/static/photos'

 
    API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    


# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mugera:Mugbwo9856@localhost/watch2_test'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mugera:Mugbwo9856@localhost/currency'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
