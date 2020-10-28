# Classe Pessoa Física

from cadastro.Pessoa import Pessoa

class PessoaFisica(Pessoa):

    # Método inicializador
    def __init__(self, nome, telefone, endereco, cpf, dataNascimento):
        super().__init__(nome, telefone, endereco)
        self.__cpf = cpf
        self.__dataNascimento = dataNascimento

    def __str__(self):
        return super().__str__() + "\nCPF: " + str(self.cpf) + "\nData de Nascimento: " + str(self.dataNascimento)

    # Retornando o valor dos atributos através do método GET
    @property
    def cpf(self):
        return self.__cpf

    @property
    def dataNascimento(self):
        return self.__dataNascimento

    # Inserindo dados nos atributos pelo método SET
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @dataNascimento.setter
    def dataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento

    # Métodos da Classe

    # Imprimindo Pessoa
    def imprimir(self):
        print(self)
