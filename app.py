from flask import Flask

from configurations.sql_commands import create_table_bikes
from configurations.database import db
from controllers.bike_controller import bike_blueprint
from urllib.parse import quote
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
app.register_blueprint(bike_blueprint)
app.secret_key = os.getenv('SECRET_KEY')

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
port = os.getenv('DB_PORT')
passw = quote(password)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{passw}@{host}:{port}/{db_name}'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)


if __name__ == '__main__':
    create_table_bikes(app,db)  # EXPLICAR ESSE APP, DB
    app.run(debug=True)