from flask import Blueprint, render_template, request, url_for, redirect, flash

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route("/adicionar_usuario", methods=['GET', 'POST'])
def criar_usuario():
    flash('Usuário criado')
    return redirect(url_for("task.index"))