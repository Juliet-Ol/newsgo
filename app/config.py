#creating classes to fit our needs

#configuration used in poduction and development
class Config:
    '''
    Configuration of parent class
    '''
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
        Config: The parent configuration class with General configuraiton settings
    '''

    DEBUG = True