from flask import Flask
from controllers.bike_controller import bike_blueprint

app = Flask(__name__)

app.register_blueprint(bike_blueprint)


if __name__ == '__main__':
    app.run(debug=True)