# Classe Matérias

from imprimir.mensagens import *

root = True

class Materia:

    # Método Inicializador
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao

    def __str__(self):
        return "Nome da Matéria: " + str(self.nome) + "\nDescrição da Matéria: " + str(self.descricao)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    # Métodos da Classe

    # Imprimindo matérias
    def imprimir(self):
        print(self)

    # Cadastrando matérias
    @staticmethod
    def cadastrarMaterias():
        # Declarando variável global
        global root
        root = True

        # Iniciando vetor das matérias
        materias = []

        while root:
            print("--------------------------------------------------------------------------------")
            nome = input("Insira o nome da Matéria: ")
            descricao = input("Insira a descrição da matéria: ")

            novaMateria = Materia(nome, descricao)
            materias.append(novaMateria)

            # Mensagem de erro ou sucesso
            if novaMateria in materias:
                print()
                sucesso.mensagemSucessoCadastro(novaMateria.nome)
            else:
                print()
                erro.mensagemErroCadastro(nome)

            opcaoUser = input("\nDeseja inserir outro curso?\n1 - Sim;\n2 - Não.\n")
            if opcaoUser == 1 or opcaoUser == "1":
                root = True
            elif opcaoUser == 2 or opcaoUser == "2":
                root = False
            else:
                erro.mensagemErroMenu()
                root = False

        return materias
