from repositories.task_repository import TaskRepository
from configurations.database import db

class TaskService:
    def adicionar_tarefa(self, conteudo, prioridade="Média"):
        if not conteudo:
            raise Exception("A tarefa não pode ser vazia")
        TaskRepository.add_task(conteudo, prioridade)

    def listar_tarefas(self):
        return TaskRepository.get_all_tasks()

    def completar_tarefa(self, tarefa_id):
        TaskRepository.complete_task(tarefa_id)

    def remover_tarefa(self, tarefa_id):
        TaskRepository.delete_task(tarefa_id)