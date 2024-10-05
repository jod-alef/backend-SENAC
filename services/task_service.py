from models.task_models import Task

class TaskService:

    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, conteudo):
        if not conteudo:
            raise Exception("A tarefa não pode ser vazia") #Exception não necessária pois o campo do form no index.html
                                                           #está marcado como required, fazendo a checagem no frontend

        nova_tarefa = Task(conteudo, False)
        self.tarefas.append(nova_tarefa)

    def listar_tarefas(self):
        return self.tarefas

    def completar_tarefa(self, tarefa_id):
        self.tarefas[tarefa_id].completa = True

    def remover_tarefa(self, tarefa_id):
        self.tarefas.pop(tarefa_id)
