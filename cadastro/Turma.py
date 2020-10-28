# Classe Turma

from imprimir.mensagens import *

root = True

class Turma:

    # Método Inicializador
    def __init__(self, codigoTurma, materias, curso, alunos, dataInicio, dataFinal):
        self.codigoTurma = codigoTurma
        self.materias = materias
        self.curso = curso
        self.alunos = alunos
        self.dataInicio = dataInicio
        self.dataFinal = dataFinal

    def __str__(self):
        return "Código da Turma: " + str(self.codigoTurma) + "\nCurso: " + str(self.curso) + "\nData de Inicio: " +\
               str(self.dataInicio) + "\nData do Final: " + str(self.dataFinal)

    # Retornando o valor dos atributos através método GET
    @property
    def codigoTurma(self):
        return self.codigoTurma

    @property
    def materias(self):
        return self.materias

    @property
    def curso(self):
        return self.curso

    @property
    def alunos(self):
        return self.alunos

    @property
    def dataInicio(self):
        return self.dataInicio

    @property
    def dataFinal(self):
        return self.dataFinal

    # Inserindo dados nos atributos pelo método SET
    @codigoTurma.setter
    def codigoTurma(self, codigoTurma):
        self.codigoTurma = codigoTurma

    @materias.setter
    def materias(self, materias):
        self.materias = materias

    @curso.setter
    def curso(self, curso):
        self.curso = curso

    @alunos.setter
    def alunos(self, alunos):
        self.alunos = alunos

    @dataInicio.setter
    def dataInicio(self, dataInicio):
        self.dataInicio = dataInicio

    @dataFinal.setter
    def dataFinal(self, dataFinal):
        self.dataFinal = dataFinal

    # Métodos da Classe

    # Imprimindo Turmas
    def imprimir(self):
        print(self)

    # Cadastrando Turmas
    @staticmethod
    def cadastrarTurma():
        global root
        turmas = []

        while root:
            print("--------------------------------------------------------------------------------")
            codTurma = input("Insira o Código da Turma: ")
            materias = input("Insira as matérias para a turma " + codTurma + ": ")
            curso = input("Insira o curso da turma " + codTurma + ": ")
            alunos = input("Insira os alunos da turma " + codTurma + ": ")
            dataInicio = input("Insira a data de inicio da Turma: ")
            dataFinal = input("Insira a data do final da Turma: ")

            # Criando nova Turma
            novaTurma = Turma(codTurma, materias, curso, alunos, dataInicio, dataFinal)

            # Adicionando a turma criada na lista das Turmas
            turmas.append(novaTurma)

            # Verificando se a turma foi add na lista e retorna mensagem de sucesso ou erro
            if novaTurma in turmas:
                sucesso.mensagemSucessoCadastro(novaTurma.codigoTurma)
            else:
                erro.mensagemErroCadastro(codTurma)

            # Pergunta se deseja cadastrar outra turma
            opcaoUsuario = input("Deseja cadastrar outra turma?\n1 - Sim;\n2 - Não.\n")
            if opcaoUsuario == 1 or opcaoUsuario == "1":
                root = True
            elif opcaoUsuario == 2 or opcaoUsuario == "2":
                root = False
            else:
                erro.mensagemErroMenu()
                root = False

        return turmas
