# Função gerenciar

import os

from imprimir import *

def gerenciarEscola(escola):
    root = True

    while root:
        # Apaga a Tela
        os.system("cls") or None

        # Chama o cabeçalho Estilizado com o nome da escola
        cabecalho.cabecalhoEscola(escola.getNome())

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
            pass
        elif opcaoUser == 6 or opcaoUser == "6":
            pass
        elif opcaoUser == 7 or opcaoUser == "7":
            pass
        elif opcaoUser == 8 or opcaoUser == "8":
            pass
        elif opcaoUser == 9 or opcaoUser == "9":
            root = False
        else:
            print("Opção inválida, por favor escolha uma das alternativas apresentadas.")