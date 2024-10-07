from models.bike_models import Bikes

class BikeService:

    def __init__(self):
        self.bike = []

    def adicionar_bike(self, modelo, categoria, preco):
        nova_bike = Bikes(modelo, categoria, preco, False)
        self.bike.append(nova_bike)

    def listar_bikes(self):
        return self.bike

    def vendida(self, bike_id):
        self.bike[bike_id].status = True

    def remover(self, bike_id):
        self.bike.pop(bike_id)




