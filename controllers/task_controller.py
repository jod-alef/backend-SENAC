from flask import render_template, request, url_for, Blueprint, redirect, session
from services.task_service import TaskService


task_blueprint = Blueprint('task', __name__, url_prefix='/tarefas')  # TO NA DUVIDA
task_service = TaskService()

@task_blueprint.route("/listar")
def index():

    if 'user_id' not in session:
        return redirect(url_for('user.login'))

    user_id = session['user_id']
    tarefas = task_service.listar_tarefas(user_id)
    return render_template("index.html", tarefas=tarefas)

@task_blueprint.route("/adicionar", methods=["POST"])
def adicionar():
    conteudo = request.form.get("tarefa")
    prioridade = request.form.get("prioridade", "Média")

    if prioridade == '':
        prioridade = 'Média'

    try:
        task_service.adicionar_tarefa(conteudo, prioridade)
    except Exception as e:
        return str(e), 400

    return redirect(url_for("task.index"))

@task_blueprint.route("/completar/<int:tarefa_id>")
def completar(tarefa_id):

    try:
        task_service.completar_tarefa(tarefa_id)
    except Exception as e:
        return str(e), 400

    return redirect(url_for("task.index"))

@task_blueprint.route("/remover/<int:tarefa_id>")
def remover(tarefa_id):
    try:
        task_service.remover_tarefa(tarefa_id)
    except Exception as e:
        return str(e), 400

    return redirect(url_for("task.index"))