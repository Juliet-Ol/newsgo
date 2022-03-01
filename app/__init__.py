# from ensurepip import bootstrap

from flask import Flask
from .config import ProdConfig

# from app import error


#Initializing application
app = Flask(__name__,instance_relative_config=True)

#Setting up configuration
app.config.from_object(ProdConfig) # For live Environment
app.config.from_pyfile('config.py')

#Initializing Flask Extensions

from app import views



# bootstrap = Bootstrap()

# def create_app(config_name):
#     app = Flask(__name__)

#     #Creating the app configurations
#     app.config.from_object(config_options[config_name])

#     #Initializing flask extentions
#     bootstrap.init_app(app)

#     #Will add the views and forms

#     return app