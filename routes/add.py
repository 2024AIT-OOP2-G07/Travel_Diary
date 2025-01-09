from flask import Blueprint, render_template,request,url_for,redirect
from urllib.request import Request, urlopen
from urllib.parse import quote
import json
from models import Place


add_bp = Blueprint("add", __name__, url_prefix="/add")

@add_bp.route("/")
def list():
    return render_template("add.html")

@add_bp.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        name = request.form["name"]
        day = request.form["day"]
        address = request.form["address"]
        evaluation = request.form["evaluation"]
        comment = request.form["comment"]

        coordinates = get_coordinates(address)

        if not coordinates:
            return render_template(
                "add.html", error="住所が見つかりませんでした"
            )

        Place.create(
            name=name, day=day, address=address, evaluation=evaluation, comment=comment, lat=coordinates[1], lon=coordinates[0]
        )
        return redirect(url_for("add.list"))

    return render_template("add.html")

def get_coordinates(address):
    url = f"https://msearch.gsi.go.jp/address-search/AddressSearch?q={quote(address)}"
    req = Request(url)
    with urlopen(req) as res:
        data = json.load(res)

    if len(data) == 0:
        return None

    return data[0]["geometry"]["coordinates"]
