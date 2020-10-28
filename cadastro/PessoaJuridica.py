# Classe Pessoa Jurídica

from cadastro.Pessoa import Pessoa
from imprimir.mensagens import *

root = True


class PessoaJuridica(Pessoa):

    # Método inicializador
    def __init__(self, nome, telefone, endereco, cnpj, dataAbertura):
        super().__init__(nome, telefone, endereco)
        self.__cnpj = cnpj
        self.__dataAbertura = dataAbertura

    def __str__(self):
        return super(PessoaJuridica,
                     self).__str__() + "\nCNPJ: " + str(self.cnpj) + "\nData de Abertura: " + str(self.dataAbertura)

    # Retornando o valor dos atributos através do método GET
    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def dataAbertura(self):
        return self.__dataAbertura

    # Inserindo dados nos atributos pelo método SET
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @dataAbertura.setter
    def dataAbertura(self, dataAbertura):
        self.__dataAbertura = dataAbertura

    # Métodos da Classe

    # Para imprimir
    def imprimir(self):
        print(self)

    @staticmethod
    def cadastrarEscola():

        # Declarando que a variável root é global
        global root
        escolas = []  # Lista que será retornada

        while root:
            print("--------------------------------------------------------------------------------")
            nomeEscola = input("Insira o nome da Escola: ")
            telefoneEscola = input("Insira o número de telefone: ")
            enderecoEscola = input("Insira o endereço da Escola: ")
            cnpjEscola = input("Insira o CNPJ da Escola: ")
            dataAbertura = input("Insira a data de abertura da escola: ")

            novaEscola = PessoaJuridica(nomeEscola, telefoneEscola, enderecoEscola, cnpjEscola, dataAbertura)

            escolas.append(novaEscola)

            # Mensagem de sucesso ou erro
            if novaEscola in escolas:
                print()
                sucesso.mensagemSucessoCadastro(novaEscola.nome)
            else:
                print()
                erro.mensagemErroCadastro(nomeEscola)

            # pergunta se deseja cadastrar nova escola
            opcaoUsuario = input("\nDeseja Cadastrar outra Escola?\n1 - Sim;\n2 - Não.\n")
            if opcaoUsuario == 2 or opcaoUsuario == "2":
                root = False
            elif opcaoUsuario == 1 or opcaoUsuario == "1":
                pass
            else:
                erro.mensagemErroMenu()
                root = False
        return escolas
