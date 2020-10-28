################################################################################
#                                                                              #
#                Sistema básico de gereciamento escolar v1.0                   #
#                                                                              #
# Autor: Samuell Oliveira Martins                                              #
# Descrição: Este programa visa o gerenciamento escolar com rotinas básicas;   #
#            Não possui interface gráfica, apenas a funcionalidade no prompt   #
#            de comando (tela preta).                                          #
# Data: 15 de outubro de 2020                                                  #
#                                                                              #
################################################################################

# -------------------------------------------------------------------------------#

# Importando pacotes
import os

from imprimir import *
from cadastro.funcoes import *
from cadastro import *
from ferramentas.filtros import *

# Inicializando algumas variáveis
root = True
opcaoUsuario = 0
escolasCadastradas = False

escolas = []

# Laço de execução do programa
while root:
    # Verifica se existem escolas cadastradas
    if len(escolas) == 0:
        escolasCadastradas = False
    elif len(escolas) > 0:
        escolasCadastradas = True
    else:
        pass

    # Limpando a tela no windows
    os.system('cls') or None

    # Chamando o menu, o cabeçalho e recebendo a opção do usuário
    cabecalho.cabecalhoInicial()
    menu.menuPrincipal(escolasCadastradas)
    opcaoUsuario = int(input())

    # Executando opções do menu
    if escolasCadastradas:
        # Aqui as opções do menu quando já existem escolas cadastradas
        if opcaoUsuario == 1:
            if len(escolas) == 1:
                os.system('cls') or None
                gerenciar.gerenciarEscola(escolas[0])
            else:
                os.system('cls') or None
                cabecalho.cabecalhoInicial()

                # Imprime todas as escolas cadastradas, pergunta ao usuário qual escola ele quer gerenciar e retorna o
                # objeto escola
                contador = 1
                for escola in escolas:
                    print("--------------------------------------------------------------------------------")
                    print(str(contador) + " - ")
                    escola.imprimir()
                    contador += 1

                opcaoUsuario = int(input("\nInsira o número da escola que você deseja gerenciar: "))
                opcaoUsuario -= 1

                # Chama função para gerenciar Escola
                gerenciar.gerenciarEscola(escolas[opcaoUsuario])

        elif opcaoUsuario == 2:
            contador = 1
            for escola in escolas:
                print("--------------------------------------------------------------------------------")
                print(str(contador) + " - ")
                escola.imprimir()
                contador += 1

        elif opcaoUsuario == 3:
            # Chama a função cadastrar
            cadastrando = PessoaJuridica.PessoaJuridica.cadastrarEscola()
            escolas = escolas + cadastrando

            # Ordena em ordem alfabetica os objetos na lista.
            sorted(escolas, key=lambda PessoaJuridica: PessoaJuridica.nome)

        elif opcaoUsuario == 4:
            root = False
        else:
            mensagens.mensagemErroMenu()
    else:
        # Aqui as opções do menu quando não há escolas cadastradas
        if opcaoUsuario == 1:
            # Chama a função cadastrar
            cadastrando = PessoaJuridica.PessoaJuridica.cadastrarEscola()
            escolas = escolas + cadastrando

            # Ordena em ordem alfabetica os objetos na lista.
            sorted(escolas, key=lambda PessoaJuridica: PessoaJuridica.nome)
        elif opcaoUsuario == 2:
            root = False
        else:
            mensagens.mensagemErroMenu()
