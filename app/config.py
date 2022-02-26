#creating classes to fit our needs

#configuration used in poduction and development
from instance.config import NEWS_API_KEY


class Config:
    '''
    Configuration of parent class
    '''
    #NEWS_API_KEY = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=API_KEY'
    pass

#configuration used in production stages, inherits from parent

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration with General configuration settings
    '''
    pass

#configuration use in development stages

class DevConfig(Config):
    '''
    Development  configuration child class
    
    Args:
        Config: Parent configuration class with General configuraiton settings
    '''

    DEBUG = True