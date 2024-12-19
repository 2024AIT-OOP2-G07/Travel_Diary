from flask import Blueprint, render_template

# Blueprintの作成
map_bp = Blueprint("map", __name__, url_prefix="/map")


@map_bp.route("/")
def list():
    return render_template("map.html")
