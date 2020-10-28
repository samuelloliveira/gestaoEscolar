# Classe Funcionário

from cadastro.PessoaFisica import PessoaFisica
from imprimir.mensagens import *

root = True


class Funcionario(PessoaFisica):

    # Método inicializador
    def __init__(self, nome, telefone, endereco, cpf, dataNascimento, nrRegistro, salario, departamento, nrPis):
        super().__init__(nome, telefone, endereco, cpf, dataNascimento)
        self.__nrRegistro = nrRegistro
        self.__salario = salario
        self.__departamento = departamento
        self.__nrPis = nrPis

    def __str__(self):
        return super(Funcionario, self).__str__() + "\nNúmero do PIS: " + str(self.nrPis()) + "\nMatrícula do Funcionário: " + str(self.nrRegistro()) + "\nSalário: " + str(self.salario()) + "\nSetor: " + str(self.departamento())

    # Retornando o valor dos atributos através do método GET
    @property
    def nrRegistro(self):
        return self.__nrRegistro

    @property
    def salario(self):
        return self.__salario

    @property
    def departamento(self):
        return self.__departamento

    @property
    def nrPis(self):
        return self.__nrPis

    # Inserindo dados nos atributos pelo método SET
    @nrRegistro.setter
    def nrRegistro(self, nrRegistro):
        self.__nrRegistro = nrRegistro

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento

    @nrPis.setter
    def nrPis(self, nrPis):
        self.__nrPis = nrPis

    # Métodos da classe

    # Função para gerar matrícula
    @classmethod
    def gerarMatricula(cls, funcionarios):
        matricula = 1
        # Fazendo uma conferencia para evitar que o funcionário tenha matricula repetida
        try:
            for funcionario in funcionarios:
                if funcionario.nrRegistro() == matricula:
                    matricula += 1
            return matricula
        except:
            return matricula

    # Para imprimir
    def imprimir(self):
        print(self)

    # Cadastro de Funcionário
    @staticmethod
    def cadastrarFuncionario():
        # Declarando que a variável root é global
        global root
        funcionarios = []

        while root:
            print("--------------------------------------------------------------------------------")
            nomeFuncionario = input("Insira o nome do Funcionário: ")
            telefoneFuncionario = input("Insira o telefone do Funcionário: ")
            enderecoFuncionario = input("Insira o endereço do Funcionário: ")
            cpfFuncionario = input("Insira o CPF do Funcionário: ")
            dataNascimentoFuncionario = input("Insira a data de nascimento do Funcionario: ")
            nrRegistroFuncionario = Funcionario.gerarMatricula(funcionarios)
            salarioFuncionario = input("Insira o salário do Funcionário: ")
            departamentoFuncionario = input("Insira o setor onde o Funcionário vai trabalhar: ")
            nrPisFuncionario = input("Insira o número do PIS do Funcionario: ")


            novoFuncionario = Funcionario(nomeFuncionario, telefoneFuncionario, enderecoFuncionario, cpfFuncionario, dataNascimentoFuncionario, nrRegistroFuncionario, salarioFuncionario, departamentoFuncionario, nrPisFuncionario)

            funcionarios.append(novoFuncionario)

            # Mensagem de erro ou sucesso
            if novoFuncionario in funcionarios:
                print()
                sucesso.mensagemSucessoCadastro(novoFuncionario.nome())
            else:
                print()
                erro.mensagemErroCadastro(novoFuncionario)

            # Pergunta se quer continuar cadastrando
            opcaoUsuario = input("\nDeseja cadastrar outro Funcionario?\n1 - Sim;\n2 - Não.\n")
            if opcaoUsuario == 1 or opcaoUsuario == "1":
                root = True
            elif opcaoUsuario == 2 or opcaoUsuario == "2":
                root = False
            else:
                erro.mensagemErroMenu()
                root = False

        return funcionarios
