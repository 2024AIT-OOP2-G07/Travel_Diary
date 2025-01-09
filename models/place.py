from peewee import Model, TextField, FloatField,DateField,IntegerField
from .db import db


class Place(Model):
    day = DateField(formats='%Y-%m-%d %H:%M:%S')
    name = TextField(unique=True)
    address = TextField()
    lat = FloatField()
    lon = FloatField()
    evaluation = IntegerField()
    comment = FloatField()

    class Meta:
        database = db
