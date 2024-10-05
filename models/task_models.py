class Task:
    def __init__(self, conteudo, completa):
        self.conteudo = conteudo
        self.completa = completa

    def __repr__(self):
        return f"Tarefa('{self.conteudo}', '{self.completa}')"

    def __str__(self):
        return f"Conteúdo: {self.conteudo}, Completa: {self.completa}"

    def completar(self):
        self.completa = True
