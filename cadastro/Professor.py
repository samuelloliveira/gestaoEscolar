# Classe Professor

root = True

from cadastro.Funcionario import Funcionario
from imprimir.mensagens import *


class Professor(Funcionario):

    # Método inicializador
    def __init__(self, nome, telefone, endereco, cpf, dataNascimento, nrRegistro, salario, departamento, nrPis,
                 especialidades, turmas=None):
        super().__init__(nome, telefone, endereco, cpf, dataNascimento, nrRegistro, salario, departamento, nrPis)
        if turmas is None:
            turmas = []
        self.turmas = turmas
        self.especialidades = especialidades

    def __str__(self):
        return super().__str__() + "\nTurmas: " + str(self.turmas) + "\nEspecialidades: " + str(self.especialidades)

    # Retornando o valor dos atributos através do método GET
    @property
    def turmas(self):
        return self.turmas

    @property
    def especialidades(self):
        return self.especialidades

    # Inserindo dados nos atributos pelo método SET
    @turmas.setter
    def turmas(self, turmas):
        self.turmas = turmas

    @especialidades.setter
    def especialidades(self, especialidades):
        self.especialidades = especialidades

    # Métodos da classe

    # Imprimindo
    def imprimir(self):
        print(self)

    # Cadastrando Professores
    @staticmethod
    def cadastrarProfessor():

        # Declarando que a variável Root é global
        global root
        professores = []

        while root:
            print("--------------------------------------------------------------------------------")
            nomeProfessor = input("Insira o nome do Professor: ")
            telefoneProfessor = input("Insira o número de telefone: ")
            enderecoProfessor = input("Insira o endereço do Professor: ")
            cpfProfessor = input("Insira o CPF do Professor: ")
            dataNascimento = input("Insira a data de nascimento do Professor: ")
            nrRegistro = Funcionario.gerarMatricula(professores)
            salarioProfessor = input("Insira do salário do Professor")
            departamentoProfessor = "Professor"  # Departamento seria o setor onde o funcionário trabalha
            nrPis = input("Insira o número do PIS: ")
            especialidades = input("Insira todas as especialidades do Professor separadas por vírgula: ")

            novoProfessor = Professor(nomeProfessor, telefoneProfessor, enderecoProfessor, cpfProfessor, dataNascimento,
                                      nrRegistro, salarioProfessor, departamentoProfessor, nrPis, especialidades)

            professores.append(novoProfessor)

            # Mensagem de erro ou sucesso
            if novoProfessor in professores:
                print()
                sucesso.mensagemSucessoCadastro(novoProfessor.nome)
            else:
                print()
                erro.mensagemErroCadastro(nomeProfessor)

            opcaoUser = input("\nDeseja Cadastrar outro professor?\n1 - Sim;\n2 - Não\n")
            if opcaoUser == 1 or opcaoUser == "1":
                root = True
            elif opcaoUser == 2 or opcaoUser == "2":
                root = False
            else:
                erro.mensagemErroMenu()
                root = False

        return professores

