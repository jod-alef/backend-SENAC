class Bikes:
    def __init__(self, modelo, categoria, preco, status):
        self.modelo = modelo
        self.categoria = categoria
        self.preco = preco
        self.status = status

    def __str__(self):
        return f"Modelo: {self.modelo}, Categoria: {self.categoria}, Preço: {self.preco}, Status: {self.status}"

    def vendida(self):
        self.status = True