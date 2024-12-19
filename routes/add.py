from flask import Blueprint, render_template
add_bp = Blueprint("add", __name__, url_prefix="/add")

@add_bp.route("/")
def list():
    return render_template("add.html")
