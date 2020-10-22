# Configurando filtros das Escolas

def mostrarTodasEscolas(escolas):
    contador = 1
    for escola in escolas:
        print("--------------------------------------------------------------------------------")
        print(str(contador) + " - " + escola.getNome())
        print("    " + escola.getEndereco())
        print("    " + escola.getTelefone())

        contador += 1

    opcaoUsuario = int(input("Insira o númerop da escola que você deseja gerenciar: "))
    opcaoUsuario -= 1

    return escolas[opcaoUsuario]
