from flask import Blueprint, render_template, request, url_for, redirect, flash, session
from repositories.user_repository import UserRepository

user_blueprint = Blueprint('user', import_name=__name__, url_prefix='/usuario')

@user_blueprint.route("/adicionar", methods=['GET', 'POST'])
def criar_usuario():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            flash('Usuário já existe!', 'danger')
            return redirect(url_for('user.adicionar_usuario'))

        UserRepository.create_user(username, password)
        flash('Usuário cadastrado com sucesso!')
        return redirect(url_for("user.adicionar_usuario"))

    flash("Bem vindo a página de cadastro!", 'success')
    return render_template('add_user.html')

@user_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash ('Login realizado com sucesso!', 'success')
            return redirect(url_for('tarefa.index'))

        flash('Usuário ou senha inválidos!', 'danger')
    return render_template('login.html')

@user_blueprint.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logout realizado com sucesso', 'success')
    return redirect(url_for('user.login'))




