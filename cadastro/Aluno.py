# Classe Aluno

from cadastro.PessoaFisica import PessoaFisica
from imprimir.mensagens import *

root = True


class Aluno(PessoaFisica):

    # Método inicializador
    def __init__(self, nome, telefone, endereco, cpf, dataNascimento, matricula, turma, curso):
        super().__init__(nome, telefone, endereco, cpf, dataNascimento)
        self.__matriculaAluno = matricula
        self.__turma = turma
        self.__curso = curso

    def __str__(self):
        return super().__str__() + "\nNúmero da Matrícula: " + str(self.matricula) + "\nTurma: " + str(self.turma) + \
               "\nCurso: " + str(self.curso)

    # Retornando o valor dos atributos através do método GET
    @property
    def matricula(self):
        return self.__matricula

    @property
    def turma(self):
        return self.__turma

    @property
    def curso(self):
        return self.__curso

    # Inserindo dados nos atributos pelo método SET
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @turma.setter
    def turma(self, turma):
        self.__turma = turma

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    # Métodos da Classe

    # Imprimindo
    def imprimir(self):
        print(self)

    # Função para gerar matrícula
    @classmethod
    def gerarMatricula(cls, alunos):
        matricula = 1
        # Fazendo uma conferencia para evitar que o funcionário tenha matricula repetida
        try:
            for aluno in alunos:
                if aluno.matricula == matricula:
                    matricula += 1
            return matricula
        except:
            return matricula

    # Cadastrando Alunos
    @staticmethod
    def cadastrarAluno():
        # Definindo variavel global
        global root
        alunos = []

        while root:
            print("--------------------------------------------------------------------------------")
            nome = input("Insira o Nome do Aluno:")
            telefone = input("Insira o numero de telefone do Aluno")
            endereco = input("Insira o endereço do Aluno")
            cpf = input("Insira o número do CPF do Aluno")
            dataNascimento = input("Insira a data de nascimento do Aluno: ")
            matricula = Aluno.gerarMatricula(alunos)  # Aqui chamar a função gerar matrícula
            turma = input("Insira Turma do Aluno")  # Aqui chamar a função para imprimir todas as turmas
            curso = input("Insira o Curso do Aluno")  # Aqui chamar a função para imprimir todos os cursos

            # Criando objeto Aluno
            novoAluno = Aluno(nome, telefone, endereco, cpf, dataNascimento, matricula, turma, curso)

            # Colocando o novo aluno na lista de alunos
            alunos.append(novoAluno)

            # Verificando se o Aluno foi inserido na lista
            if novoAluno in alunos:
                sucesso.mensagemSucessoCadastro(novoAluno.nome)
            else:
                erro.mensagemErroCadastro(nome)

            # Pergunta se quer continuar cadastrando alunos
            opcaoUsuario = input("Deseja cadastrar outro Aluno?\n1 - Sim;\n2 - Não.\n")
            if opcaoUsuario == 1 or opcaoUsuario == "1":
                root = True
            elif opcaoUsuario == 2 or opcaoUsuario == "2":
                root = False
            else:
                erro.mensagemErroMenu()
                root = False

        return alunos
