from flask import Blueprint

bp = Blueprint('routes', __name__)

@bp.route("/")
def home():
    return "<h1>Pokepedia</h1>"