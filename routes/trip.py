from flask import Blueprint, render_template

# Blueprintの作成
trip_bp = Blueprint("trip", __name__, url_prefix="/trip")


@trip_bp.route("/")
def list():
    return render_template("trip.html")
