from flask import Flask, request, jsonify, make_response
from database import schema
from service import TaskService
from flask_cors import CORS, cross_origin
import sqlite3
import logging
from service import FamilyService

app = Flask(__name__)
logging.getLogger('flask_cors').level = logging.DEBUG

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers[
        'Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE, OPTIONS"
    print(response.headers)
    return response

@app.route("/")
def test_method():
    return "Local server is running"

@app.route("/task", methods=["GET"])
def get_tasks():
    return jsonify({'tasks': TaskService().list()})

@app.route("/members", methods=["GET"])
def get_members():
    return jsonify({'members': FamilyService().list()})


@app.route("/create/task", methods=["POST", "OPTIONS"])
def create_task():
    if request.method == "OPTIONS":
        return build_cors_prelight_response()
    elif request.method == "POST":
        post_data = request.get_json()
        print("post data :")
        return corsify_actual_response(jsonify(TaskService().create(post_data)))
    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))

def build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/update-task/<int:item_id>", methods=["PUT"])
def update_task(item_id):
    if request.method == "OPTIONS":
        return build_cors_prelight_response()
    elif request.method == "PUT":  # The actual request following the preflight
        put_data = request.get_json()  # Whatever.
        print("post data :")
        return corsify_actual_response(jsonify(TaskService().update(item_id, put_data)))
    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))

@app.route("/delete-task/<item_id>", methods=["DELETE"])
def delete_task(item_id):
    return jsonify(TaskService().delete(item_id))

if __name__ == "__main__":
    schema()
    app.run(host='0.0.0.0', debug=True, use_reloader=False)
