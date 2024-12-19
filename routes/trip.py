from flask import Blueprint, render_template
from models import prace
from peewee import fn

# Blueprintの作成
trip_bp = Blueprint("trip", __name__, url_prefix="/trip")


@trip_bp.route("/")
def list():

    trip_data = prace.select()\
        .where(prace.evaluation == 5)\
        .order_by(prace.day.desc())\
        .limit(5)
    
    print(trip_data)

    return render_template("trip.html",trip_data = trip_data)

