# Classe Pessoa

class Pessoa:

    # Método inicializador
    def __init__(self, nome, telefone, endereco):
        self.__nome = nome
        self.__telefone = telefone
        self.__endereco = endereco

    # Retornando os atributos através do método GET
    def getNome(self):
        return self.__nome

    def getTelefone(self):
        return self.__telefone

    def getEndereco(self):
        return self.__endereco

    # Inserindo dados nos atributos pelo método SET
    def setNome(self, nome):
        self.__nome = nome

    def setTelefone(self, telefone):
        self.__telefone = telefone

    def setEndereco(self, endereco):
        self.__endereco = endereco
