import os

class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///maintenance.db'  # You can change to a different database (PostgreSQL, MySQL)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
