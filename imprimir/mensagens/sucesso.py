import time # importa a biblioteca time
import os # importando biblioteca para executar comandos do sistema operacional

def mensagemSucessoCadastro(nome):
  os.system('cls') or None # Primeiro apaga a tela e depois exibe a mensagem.
  print(nome + " foi cadastrado(a) com sucesso")
  time.sleep(3) # Após exibir a mensagem, aguarda 3 segundos para apagar a tela e continuar a execução do programa.