from configurations.database import db
from sqlalchemy import text

class BikeRepository:
    @staticmethod
    def list_bikes():
        query = text ('SELECT * FROM bikes')
        result = db.session.execute((query))
        return result.fetchall()

    @staticmethod
    def add_bike(modelo, categoria, preco):
        query = text('''
            INSERT INTO bikes (modelo, categoria, preco)
            VALUES (:modelo, :categoria, :preco)
        ''')

        db.session.execute(query, {
            'modelo' : modelo,
            'categoria' : categoria,
            'preco' : preco
        })

        db.session.commit()

    @staticmethod
    def sell_bike(bike_id):
        query = text("UPDATE bikes SET vendida = TRUE WHERE id = :id")
        db.session.execute(query,{'id': bike_id})
        db.session.commit()

    @staticmethod
    def delete_bike(bike_id):
        query = text('DELETE FROM bikes WHERE id = :id')
        db.session.execute((query,{'id': bike_id}))
        db.session.commit()