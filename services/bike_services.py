from flask import flash
from repositories.bike_repository import BikeRepository

class BikeService:

    def __init__(self):
        self.bike = []
        self.quantidade = 0
        self.valorVendidas = 0

    def adicionar_bike(self, modelo, categoria, preco):
        precoint = float(preco)
        for bike in self.bike:
            if bike.modelo == modelo and bike.status == False:
                flash("Erro: Modelo repetido", "error")
                return
        if precoint < 100:
            flash("Erro: Valor não pode ser menor que R$ 100,00", "error")
            return

        BikeRepository.add_bike(modelo, categoria, preco)
        flash("Bike adicionada com sucesso!", "success")

    def listar_bikes(self):
        return BikeRepository.list_bikes()

    def vendida(self, bike_id):
        BikeRepository.sell_bike(bike_id)
        self.quantidade += 1
        self.valorVendidas += self.bike[bike_id].preco

    def remover(self, bike_id):
        BikeRepository.delete_bike(bike_id)

    def contar(self):
        return self.quantidade

    def valor_vendidas(self):
        return self.valorVendidas