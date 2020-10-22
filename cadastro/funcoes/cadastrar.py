# Métodos para cadastrar

from cadastro import *
from imprimir.mensagens import *

# variável para implementar um laço usado em todas as funções ou grande parte delas
root = True

def cadastrarEscola():

    # Declarando que a variável root é global
    global root
    escolas = []  # Lista que será retornada

    while root:
        nomeEscola = input("Insira o nome da Escola: ")
        telefoneEscola = input("Insira o número de telefone: ")
        enderecoEscola = input("Insira o endereço da Escola: ")
        cnpjEscola = input("Insira o CNPJ da Escola: ")
        dataAbertura = input("Insira a data de abertura da escola: ")

        novaEscola = PessoaJuridica.PessoaJuridica(nomeEscola, telefoneEscola, enderecoEscola, cnpjEscola, dataAbertura)

        escolas.append(novaEscola)

        # Mensagem de sucesso ou erro
        if novaEscola in escolas:
            sucesso.mensagemSucessoCadastro(nomeEscola)
        else:
            print(escolas)
            erro.mensagemErroCadastro(nomeEscola)

        # pergunta se deseja cadastrar nova escola
        opcaoUsuario = int(input("Deseja Cadastrar outra Escola?\n1 - Sim;\n2 - Não.\n\n"))
        if opcaoUsuario == 2:
            root = False
        elif opcaoUsuario == 1:
            pass
        else:
            erro.mensagemErroMenu()
    return escolas

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
        nrRegistro = input("Insira o número do Registro do Professor: ")
        salarioProfessor = input("Insira o salário do Professor: ")
        departamentoProfessor = "Professor"  # Departamento seria o setor onde o funcionário trabalha
        nrPis = input("Insira o número do PIS: ")
        especialidades = input("Insira todas as especialidades do Professor separadas por vírgula: ")

        opcaoUser = input("\nDeseja Cadastrar outro professor?\n1 - Sim;\n2 - Não\n")
        if opcaoUser == 1 or opcaoUser == "1":
            root = True
        elif opcaoUser == 1 or opcaoUser == "1":
            root = False
        else:
            erro.mensagemErroMenu()