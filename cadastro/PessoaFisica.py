# Classe Pessoa Física

from cadastro.Pessoa import Pessoa

class PessoaFisica(Pessoa):

    # Método inicializador
    def __init__(self, nome, telefone, endereco, cpf, dataNascimento):
        super().__init__(nome, telefone, endereco)
        self.__cpf = cpf
        self.__dataNascimento = dataNascimento

    # Retornando o valor dos atributos através do método GET
    def getCpf(self):
        return self.__cpf

    def getDataNascimento(self):
        return self.__dataNascimento

    # Inserindo dados nos atributos pelo método SET
    def setCpf(self, cpf):
        self.__cpf = cpf

    def setDataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento
