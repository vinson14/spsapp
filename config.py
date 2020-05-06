import os

class Config:

    SECRET_KEY = 'jkl;38dasfj)8!#'
    SESSION_COOKIE_NAME = "my_cookie"
    FLASK_DEBUG = 1
    FLASK_APP = 'wsgi.py'

    # Database
    SQLALCHEMY_DATABASE_URI = "postgres://iybvaosvdzrjar:1c615d5b7e143c0d9e2ed628b4480e785323e3b5cb9b796fe0a9798c1c7fd02a@ec2-52-87-135-240.compute-1.amazonaws.com:5432/da48nr8lseo1v5"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
