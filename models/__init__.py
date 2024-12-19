from peewee import SqliteDatabase
from .db import db
from .prace import prace

MODELS = [prace]

# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()
