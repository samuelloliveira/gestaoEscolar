# Menu inicial do programa
def menuPrincipal(status):
    # Uma estrutura condicional para verificar se temos escolas cadastradas
    if status is not True:
        print("Seja bem-vindo!\nPara comerçarmos, inicialize o programa inserindo uma nova escola\n")
        print("1 - Cadastrar Escola")
        print("2 - Sair")
    else:
        # caso haja alguma escola cadastrada no sistema
        print("Seja bem-vindo!")
        print("1 - Gerenciar Escola cadastrada")
        print("2 - Listar Escolas cadastradas no Sistema")
        print("3 - Cadastrar nova escola")
        print("4 - Sair")


# Menu de opções para gerenciar uma escola.
def menuGerencia(escola):
    # Opções do Menu
    print("Seja Bem vindo ao sistema de gerenciamento Escolar")
    print("1 - Cadastrar Cursos")
    print("2 - Listar Cursos Cadastrados")
    print("3 - Cadastrar Professores")
    print("4 - Listar Professores Cadastrados")
    print("5 - Cadastrar Alunos")
    print("6 - Listar Alunos Cadastrados")
    print("7 - Cadastrar Turma")
    print("8 - Relatórios")
    print("9 - Sair")