# Classe Funcionário

from cadastro.PessoaFisica import PessoaFisica

class Funcionario(PessoaFisica):

    # Método inicializador
    def __init__(self, nome, telefone, endereco, cpf, dataNascimento, nrRegistro, salario, departamento, nrPis):
        super().__init__(nome, telefone, endereco, cpf, dataNascimento)
        self.nrRegistro = nrRegistro
        self.salario = salario
        self.departamento = departamento

    # Retornando o valor dos atributos através do método GET
    def getNrRegistro(self):
        return self.nrRegistro

    def getSalario(self):
        return self.salario

    def getDepartamento(self):
        return self.departamento

    # Inserindo dados nos atributos pelo método SET
    def setNrRegistro(self, nrRegistro):
        self.nrRegistro = nrRegistro

    def setSalario(self, salario):
        self.salario = salario

    def setDepartamento(self, departamento):
        self.departamento = departamento