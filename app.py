from flask import Flask

from configurations.sql_commands import create
from controllers.bike_controller import bike_blueprint

app = Flask(__name__)

app.register_blueprint(bike_blueprint)
app.secret_key = 'aslhd812uy3408hdafs'

if __name__ == '__main__':
    app.run(debug=True)