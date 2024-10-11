from models.task_models import Task
from configurations.database import db

class TaskService:
    def adicionar_tarefa(self, conteudo, prioridade="Média"):
        if not conteudo:
            raise Exception("A tarefa não pode ser vazia")

        nova_tarefa = Task(conteudo=conteudo, prioridade=prioridade)
        db.session.add(nova_tarefa) # adicionar a tarefa no banco, mas não vai salvar
        db.session.commit() #persistir o dado no banco

    def listar_tarefas(self):
        return Task.query.all()

    def completar_tarefa(self, tarefa_id):
        tarefa = Task.query.get(tarefa_id)
        if tarefa:
            tarefa.completar()
            db.session.commit()
        else:
            raise Exception("Tarefa não encontrada")

    def remover_tarefa(self, tarefa_id):
        tarefa = Task.query.get(tarefa_id)
        if tarefa:
            db.session.delete(tarefa)
            db.session.commit()
        else:
            raise Exception("Tarefa não encontrada")
