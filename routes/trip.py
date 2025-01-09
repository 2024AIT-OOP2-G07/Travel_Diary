from flask import Blueprint, render_template
from models import Place
from peewee import fn

# Blueprintの作成
trip_bp = Blueprint("trip", __name__, url_prefix="/trip")


@trip_bp.route("/")
def list():

    trip_data = Place.select()\
        .where(Place.evaluation == 5)\
        .order_by(Place.day.desc())\
        .limit(5)

    return render_template("trip.html",trip_data = trip_data)

