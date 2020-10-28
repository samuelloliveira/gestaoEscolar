# Classe Curso

root = True

class Curso:

    # Método Inicializador
    def __init__(self, nome, descricao, materias=None):
        self.__nome = nome
        self.__descricao = descricao
        self.__materias = materias

    def __str__(self):
        return "Nome do Curso: " + str(self.nome) + "\nDescrição do Curso: " + str(self.descricao)

    # Retornando o valor dos atributos através método GET
    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.descricao

    @property
    def materias(self):
        return self.materias

    # Inserindo dados nos atributos pelo método SET
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @materias.setter
    def materias(self, materias):
        self.__materias = materias

    # Métodos da Classe

    # Imprimindo Cursos
    def imprimir(self):
        print(self)

    # Cadastrando cursos
    @staticmethod
    def cadastrarCuso():
        # Declarando variavel global
        global root

        # Vetor onde serão armazenados os cursos cadastrados
        cursos = []

        while root:
            print("--------------------------------------------------------------------------------")
            nome = input("Insira o nome do Curso: ")
            descricao = input("Insira a descrição do Curso: ")

