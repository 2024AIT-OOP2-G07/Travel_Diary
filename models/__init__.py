from .db import db
from .place import Place

MODELS = [Place]

# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()
