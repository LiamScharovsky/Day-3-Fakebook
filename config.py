#Allows for shortcut to not have to set every time. Not best practice because it has to access
#data every time it starts
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))
#gets absolute path to
#__name__ gets the file
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("FLASK_ENV")
    if os.getenv('SQLALCHEMY_DATABSE_URI').startswith('postgres'):    
        SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABSE_URI').replace('postgres', 'postgresql')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    SECRET_KEY = os.getenv('SECRET_KEY')


