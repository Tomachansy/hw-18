from flask import Flask
from flask_restx import Api

from app.config import Config
from app.create_data import load_data
from app.setup_db import db
from app.views.director import directors_ns
from app.views.genre import genres_ns
from app.views.movie import movies_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    load_data(app, db)


app = create_app(Config())

if __name__ == '__main__':
    app.run(host="localhost", port=10002, debug=True)
