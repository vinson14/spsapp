import os

class Config:

    SECRET_KEY = 'jkl;38dasfj)8!#'
    SESSION_COOKIE_NAME = "my_cookie"
    FLASK_DEBUG = 1
    FLASK_APP = 'wsgi.py'

    # Database
    SQLALCHEMY_DATABASE_URI = "postgres://unkhxuyztfpceq:fb7205832ce6845b0f5a48d210e6a7e3beb23780624e95386c3fdaa40e724ee4@ec2-18-232-143-90.compute-1.amazonaws.com:5432/d77170j54loomn"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
