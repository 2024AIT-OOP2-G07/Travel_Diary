import datetime
from flask import Blueprint, render_template, request
from models import Place
from peewee import fn

# Blueprintの作成
trip_bp = Blueprint("trip", __name__, url_prefix="/trip")


@trip_bp.route("/", methods=['GET', 'POST'])
def list():

    if request.method == 'POST':
        address = request.form.get('address', '').strip()

        trip_data = Place.select()\
            .where(Place.evaluation == 5,Place.address.contains(address))\
            .order_by(Place.day.desc())\
            .limit(5)
        
        return render_template("trip.html",trip_data = trip_data)
        
    trip_data = Place.select()\
        .where(Place.evaluation == 5)\
        .order_by(Place.day.desc())\
        .limit(5)

    return render_template("trip.html",trip_data = trip_data)