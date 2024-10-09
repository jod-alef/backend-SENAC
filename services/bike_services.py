from flask import flash
from models.bike_models import Bikes

class BikeService:

    def __init__(self):
        self.bike = []

    def adicionar_bike(self, modelo, categoria, preco):
        precoint = int(preco)
        for bike in self.bike:
            if bike.modelo == modelo:
                flash("Erro: Modelo repetido", "error")
                return
            if precoint > 100:
                flash("Erro: Valor não pode ser maior que R$ 100,00")
                return

        nova_bike = Bikes(modelo, categoria, preco, False)
        self.bike.append(nova_bike)
        flash("Bike adicionada com sucesso!", "success")

    def listar_bikes(self):
        return self.bike

    def vendida(self, bike_id):
        self.bike[bike_id].status = True

    def remover(self, bike_id):
        self.bike.pop(bike_id)




