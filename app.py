from flask import Flask

from configurations.sql_commands import create_table_tasks, create_table_users, create_root_user
from configurations.database import db
from controllers.task_controller import task_blueprint
from controllers.user_controller import user_blueprint
from urllib.parse import quote
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.register_blueprint(task_blueprint)
app.register_blueprint(user_blueprint)

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
port = os.getenv('DB_PORT')
passw = quote(password)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{passw}@{host}:{port}/{db_name}'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
#app.config´['SQLALCHEMY_ECHO'] = False

db.init_app(app)

if __name__ == '__main__':
    create_table_tasks(app, db)
    create_table_users(app, db)
    create_root_user(app, db)
    app.run(debug=True)