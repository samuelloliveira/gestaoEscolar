# Classe Pessoa

class Pessoa:

    # Método inicializador
    def __init__(self, nome, telefone, endereco):
        self.__nome = nome
        self.__telefone = telefone
        self.__endereco = endereco

    def __str__(self):
        return "Nome: " + self.nome() + "\nTelefone: " + self.telefone() + "\nEndereço: " + self.endereco()

    # Retornando os atributos através do método GET
    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone

    @property
    def endereco(self):
        return self.__endereco

    # Inserindo dados nos atributos pelo método SET
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    # Métodos da Classe

    # Para imprimir
    def imprimir(self):
        print(self)
