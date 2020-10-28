# Função com o cabeçalho a ser exibido

def cabecalhoInicial():
    print("\n################################################################################")
    print("#                                                                              #")
    print("#                Sistema básico de gereciamento escolar v1.0                   #")
    print("#                                                                              #")
    print("################################################################################\n\n")


# Cabeçalho com o nome da Escola
def cabecalhoEscola(nomeEscola):
    # Esse cód é apenas para deixar o desenho alinhado
    espaco = " "
    contarNome = len(nomeEscola)
    contarNome += 30
    contarNome -= 80
    espaco *= contarNome

    print("\n################################################################################")
    print("#                                                                              #")
    print("#                Sistema básico de gereciamento escolar v1.0                   #")
    print("#                                                                              #")
    print("#                              " + nomeEscola + espaco + "#")
    print("#                                                                              #")
    print("################################################################################\n\n")
