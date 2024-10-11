from configurations.database import db


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.String(200), nullable=False)
    completa = db.Column(db.Boolean, default=False)
    prioridade = db.Column(db.String(50), nullable=False, default="Média")

    def __repr__(self):
        return f"Tarefa('{self.conteudo}', '{self.completa}', '{self.prioridade}')"

    def __str__(self):
        return f"Conteúdo: {self.conteudo}, Completa: {self.completa}, Prioridade: {self.prioridade}"

    def completar(self):
        self.completa = True