from sqlalchemy import text
from models.bike_models import Bikes

def create_table_bikes(app, db):
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS bikes (
        id SERIAL PRIMARY KEY,
        modelo VARCHAR(200) NOT NULL,
        categoria VARCHAR(200) NOT NULL,
        preco FLOAT(20) NOT NULL,
        status BOOLEAN DEFAULT FALSE    
    );'''

    with app.app_context():
        db.session.execute(text(create_table_sql))
        db.session.commit()
        print("Tabela 'bikes' criada com sucesso!")
