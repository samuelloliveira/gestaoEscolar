# Classe Professor

from cadastro.Funcionario import Funcionario


class Professor(Funcionario):

    # Método inicializador
    def __init__(self, nome, telefone, endereco, cpf, dataNascimento, nrRegistro, salario, departamento, nrPis,
                 especialidades, turmas=None):
        super().__init__(nome, telefone, endereco, cpf, dataNascimento, nrRegistro, salario, departamento, nrPis)
        if turmas is None:
            turmas = []
        self.turmas = turmas
        self.especialidades = especialidades

    # Retornando o valor dos atributos através do método GET
    def getTurmas(self):
        return self.turmas

    def getEspecialidades(self):
        return self.especialidades

    # Inserindo dados nos atributos pelo método SET
    def setTurmas(self, turmas):
        self.turmas = turmas

    def setEspecialidades(self, especialidades):
        self.especialidades = especialidades
