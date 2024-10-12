from flask import Flask
from configurations.database import db
from controllers.task_controller import task_blueprint
#from urllib.parse import quote

app = Flask(__name__)
app.register_blueprint(task_blueprint)

user = 'postgres.xdaftsgbbbscfrueidzc'
password = 'D6YJTdKyN9vZSfS1'
# password = quote(password)
host = 'aws-0-sa-east-1.pooler.supabase.com'
db_name = 'postgres'
port = 5432

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
#app.config´['SQLALCHEMY_ECHO'] = False

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
