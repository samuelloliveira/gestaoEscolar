import time  # importa a biblioteca time
import os  # importando biblioteca para executar comandos do sistema operacional


def mensagemErroMenu():
    # Função para imprimir mensagem de erro do menu

    os.system('cls') or None  # Primeiro apaga a tela e depois exibe a mensagem.
    print("Opção inválida, selecione alguma das opções apresentadas no menu.")
    time.sleep(3)  # Após exibir a mensagem, aguarda 3 segundos para apagar a tela e continuar a execução do programa.


def mensagemErroCadastro(nome):
    os.system('cls') or None  # Primeiro apaga a tela e depois exibe a mensagem.
    print("Não foi possível cadastrar " + nome + ". Tente novamente.")
    time.sleep(3)  # Após exibir a mensagem, aguarda 3 segundos para apagar a tela e continuar a execução do programa.
