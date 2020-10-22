# Classe Boletim

class Boletim:

    # Método Inicializador
    def __init__(self, aluno, materias, notas, status):
        self.aluno = aluno
        self.materias = materias
        self.notas = notas
        self.status = status  # True para Aprovado e False para Reprovado

    # Retornando o valor dos atributos através método GET
    def getAluno(self):
        return self.aluno

    def getMaterias(self):
        return self.materias

    def getNotas(self):
        return self.notas

    def getStatus(self):
        return self.status

    # Inserindo dados nos atributos pelo método SET
    def setAluno(self, aluno):
        self.aluno = aluno

    def setMaterias(self, materias):
        self.materias = materias

    def setNotas(self, notas):
        self.notas = notas

    def setStatus(self, status):
        self.status = status