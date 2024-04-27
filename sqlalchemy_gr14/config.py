import os


class Config:
    DEBUG = True
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:1@localhost/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False