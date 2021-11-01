from app import app, api
from flask import request
from flask_restful import Resource

todos = []
post_id = 0

class Todo(Resource):
    def get(self):
        return todos, post_id

    def post(self):
        todos.append(request.json)
        return todos, post_id

    def delete(self):
        todos.clear()
        return todos, post_id



api.add_resource(Todo, "/api/v1/todos")
