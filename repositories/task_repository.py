from configurations.database import db
from sqlalchemy import text

class TaskRepository:
    @staticmethod
    def get_all_tasks():
        query = text('SELECT * FROM tasks')
        result = db.session.execute(query)
        return result.fetchall()

    @staticmethod
    def add_task(conteudo, prioridade="Média"): # Não está salvando prioridade
        query = text("""
            INSERT INTO tasks (conteudo, completa, prioridade)
            VALUES (:conteudo, :completa, :prioridade)
        """)

        db.session.execute(query, {
            'conteudo' : conteudo,
            'completa' : False,
            'prioridade' : prioridade
        })

        db.session.commit()

    @staticmethod
    def complete_task(tarefa_id): # Não está completando as tasks com retorno: mapping or list expected for parameters
        query = text("UPDATE tasks SET completa = TRUE WHERE id = :id")
        db.session.execute(query,{'id': tarefa_id})
        db.session.commit()

    @staticmethod
    def delete_task(tarefa_id):
        query = text("DELETE FROM tasks WHERE id=:id")
        db.session.execute(query, {'id': tarefa_id})
        db.session.commit()
