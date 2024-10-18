from flask import flash
from repositories.bike_repository import BikeRepository

class BikeService:

    def adicionar_bike(self, modelo, categoria, preco):
        #TODO: como adicionar um if para checar se modelo == modelo.db e retornar uma mensagem utilizando flash que diga 'Modelos repetidos não são permitidos'
        BikeRepository.add_bike(modelo, categoria, preco)
        flash("Bike adicionada com sucesso!", "success")

    def listar_bikes(self):
        return BikeRepository.list_bikes()

    def vendida(self, bike_id):
        BikeRepository.sell_bike(bike_id)

    def remover(self, bike_id):
        BikeRepository.delete_bike(bike_id)

    def contar(self):
        return BikeRepository.count_sold_bikes()

    def valor_vendidas(self):
        return BikeRepository.sum_bikes()