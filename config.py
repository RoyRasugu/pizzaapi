class Config:
   '''
   General configuration parent class
   ''' 

   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://royrasugu:qwerty@localhost:5432/pizzas'

class ProdConfig(Config):
    # '''
    # Production configuration child class

    # Args:
    #     Config: The parent configurattion class with General configuration settings
    # '''
    pass

class DevConfig(Config):
    # '''
    # Development configuration child class

    # Args:
    #     Config: The parent configuration class with General configuration settings
    # '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://royrasugu:12345@localhost:5432/pizza'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}