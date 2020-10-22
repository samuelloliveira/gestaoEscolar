# Classe Aluno

from cadastro.PessoaFisica import PessoaFisica

class Aluno(PessoaFisica):

    # Método inicializador
    def __init__(self, nome, telefone, endereco, cpf, dataNascimento, matricula, turma, curso):
        super().__init__(nome, telefone, endereco, cpf, dataNascimento)
        self.matriculaAluno = matricula
        self.turma = turma
        self.curso = curso

    # Retornando o valor dos atributos através do método GET
    def getMatricula(self):
        return self.matricula

    def getTurma(self):
        return self.turma

    def getCurso(self):
        return self.curso

    # Inserindo dados nos atributos pelo método SET
    def setMatricula(self, matricula):
        self.matricula = matricula

    def setTurma(self, turma):
        self.turma = turma

    def setCurso(self, curso):
        self.curso = curso