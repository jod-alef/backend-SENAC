from configurations.database import db

class Bikes(db.Model):
    __tablename__ = 'bikes'
    modelo = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(200), nullable=False)
    preco = db.Column(db.Float(20), nullable=False)
    status = db.Column(db.Boolean, default=False)

    def __str__(self):
        return f"Modelo: {self.modelo}, Categoria: {self.categoria}, Preço: {self.preco}, Status: {self.status}"

    def vendida(self):
        self.status = True