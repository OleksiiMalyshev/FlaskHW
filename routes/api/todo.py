from app import app, api
from flask import request, Response
from flask_restful import Resource

todos = {}
todo_id = 0

class Todo(Resource):
    def get(self):
        return todos

    def post(self):
        global todo_id
        todos[todo_id] = response.json
        todo_id += 1
        return todos

    def delete(self):
        todos = {}

class TodoId(Resource):
    def get(self):
        return todo_id

api.add_resource(Todo, "/api/v1/todos")
api.add_resource(TodoId, "/api/v1/todo_id")
