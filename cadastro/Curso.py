# Classe Curso

class Curso:

    # Método Inicializador
    def __init__(self, nome, descricao, materias):
        self.nome = nome
        self.descricao = descricao
        self.materias = materias

    # Retornando o valor dos atributos através método GET
    def getNome(self):
        return self.nome

    def getDescricao(self):
        return self.descricao

    def getMaterias(self):
        return self.materias

    # Inserindo dados nos atributos pelo método SET
    def setNome(self, nome):
        self.nome = nome

    def setDescricao(self, descricao):
        self.descricao = descricao

    def setMaterias(self, materias):
        self.materias = materias