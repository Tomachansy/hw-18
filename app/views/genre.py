from flask import request
from flask_restx import Resource, Namespace

from app.container import genre_service
from app.dao.models.genre import GenreSchema

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):

    def get(self):
        genres_schema = GenreSchema(many=True)
        all_genres = genre_service.get_all()
        if all_genres:
            return genres_schema.dump(all_genres), 200
        else:
            return "", 404

    def post(self):
        req_json = request.json
        genre_service.create(req_json)

        return "", 201


@genres_ns.route('/<int:id>')
class GenreView(Resource):

    def get(self, id):
        genre = genre_service.get_one(id)
        if genre:
            genre_schema = GenreSchema()
            return genre_schema.dump(genre), 200
        else:
            return "", 404

    def put(self, id):
        if id:
            req_json = request.json
            req_json["id"] = id
            genre_service.update(req_json)
            return "", 204
        else:
            return "", 404

    def patch(self, id):
        if id:
            req_json = request.json
            req_json["id"] = id
            genre_service.update(req_json)
            return "", 204
        else:
            return "", 404

    def delete(self, id):
        if id:
            genre_service.delete(id)
            return "", 204
        else:
            return "", 404
