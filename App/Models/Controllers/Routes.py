from flask import Blueprint, jsonify

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return jsonify({"msg": "Sistema funcionando"})

@routes.route("/produtos")
def produtos():
    return jsonify({"msg": "Lista de produtos"})