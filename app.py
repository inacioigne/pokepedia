from flask import Flask

def create_app():

    app = Flask(__name__)

    @app.route("/")
    def home():

        return "<h1>Pokepedia</h1>"

    return app