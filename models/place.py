from peewee import Model, TextField, FloatField,DateField,IntegerField
from .db import db


class Place(Model):
    day = DateField(formats='%Y-%m-%d %H:%M:%S')
    name = TextField()
    address = TextField()
    lat = FloatField()
    lon = FloatField()
    evaluation = IntegerField()
    comment = TextField()

    class Meta:
        database = db
