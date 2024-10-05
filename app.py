from flask import Flask

from controllers.task_controller import task_blueprint

app = Flask(__name__)

app.register_blueprint(task_blueprint)

if __name__ == '__main__':
    app.run(debug=True)