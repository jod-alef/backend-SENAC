from flask import render_template, request, url_for, Blueprint, redirect
from services.bike_services import BikeService

bike_blueprint = Blueprint('bike', __name__)
bike_service = BikeService()

@bike_blueprint.route("/")
def index():
    bikes = bike_service.listar_bikes()
    contar = bike_service.contar()
    vendidas = bike_service.valor_vendidas()
    return render_template("index.html", bikes=bikes, contar=contar, vendidas=vendidas)

@bike_blueprint.route("/adicionar", methods=["POST"])
def adicionar():
    modelo = request.form.get("modelo")
    categoria = request.form.get("categoria")
    preco = request.form.get("preco")
    bike_service.adicionar_bike(modelo, categoria, preco)
    return redirect(url_for("bike.index"))


@bike_blueprint.route("/vendida/<int:bike_id>")
def vendida(bike_id):
    bike_service.vendida(bike_id)
    return redirect(url_for("bike.index"))

@bike_blueprint.route("/remover/<int:bike_id>")
def remover(bike_id):
    bike_service.remover(bike_id)
    return redirect(url_for("bike.index"))

@bike_blueprint.route('/contar')
def contar():
    bike_service.contar()
    return redirect(url_for("bike.index"))


