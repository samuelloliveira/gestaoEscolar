# Função gerenciar

import os

from imprimir import *
from cadastro import *


def gerenciarEscola(escola):
    root = True
    funcionarios = []

    while root:
        # Apaga a Tela
        os.system("cls") or None

        # Chama o cabeçalho Estilizado com o nome da escola
        cabecalho.cabecalhoEscola(escola.__nome())

        # Chama o menu de opções da Escola
        menu.menuGerencia(escola)

        # Pega a oção do usuário
        opcaoUser = input("Insira a opção desejada: ")

        # Condições
        if opcaoUser == 1 or opcaoUser == "1":
            pass
        elif opcaoUser == 2 or opcaoUser == "2":
            pass
        elif opcaoUser == 3 or opcaoUser == "3":
            pass
        elif opcaoUser == 4 or opcaoUser == "4":
            pass
        elif opcaoUser == 5 or opcaoUser == "5":
            funcionarios += Funcionario.Funcionario.cadastrarFuncionario()
            print(funcionarios)
            #sorted(funcionarios, key=lambda Funcionario: Funcionario.getNome())
        elif opcaoUser == 6 or opcaoUser == "6":
            os.system("cls") or None
            if len(funcionarios) != 0:
                os.system("cls")
                cabecalho.cabecalhoEscola(escola.__nome())
                for funcionario in funcionarios:
                    print("--------------------------------------------------------------------------------")
                    funcionario.imprimir()
            else:
                print("Nenhum Funcionário foi cadastrado")
        elif opcaoUser == 7 or opcaoUser == "7":
            pass
        elif opcaoUser == 8 or opcaoUser == "8":
            pass
        elif opcaoUser == 8 or opcaoUser == "9":
            pass
        elif opcaoUser == 8 or opcaoUser == "10":
            pass
        elif opcaoUser == 9 or opcaoUser == "11":
            root = False
        else:
            print("Opção inválida, por favor escolha uma das alternativas apresentadas.")
