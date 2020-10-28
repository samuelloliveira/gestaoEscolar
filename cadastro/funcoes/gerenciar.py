# Função gerenciar

import os

from imprimir import *
from cadastro import *
from imprimir.mensagens import erro


def gerenciarEscola(escola):
    root = True
    funcionarios = []
    cursos = []
    professores = []
    alunos = []
    turmas = []

    while root:
        # Apaga a Tela
        os.system("cls") or None

        # Chama o cabeçalho Estilizado com o nome da escola
        cabecalho.cabecalhoEscola(escola.nome)

        # Chama o menu de opções da Escola
        menu.menuGerencia(escola)

        # Pega a oção do usuário
        opcaoUser = input("Insira a opção desejada: ")

        # Condições
        if opcaoUser == 1 or opcaoUser == "1":
            os.system("cls") or None
            cabecalho.cabecalhoEscola(escola.nome)
            cursos += Curso.Curso.cadastrarCuso()

        elif opcaoUser == 2 or opcaoUser == "2":
            os.system("cls") or None
            if len(cursos) != 0:
                os.system("cls")
                cabecalho.cabecalhoEscola(escola.nome)
                for curso in cursos:
                    print("--------------------------------------------------------------------------------")
                    curso.imprimir()
            else:
                print("Nenhum Curso foi cadastrado")

        elif opcaoUser == 3 or opcaoUser == "3":
            os.system("cls") or None
            cabecalho.cabecalhoEscola(escola.nome)
            professores += Professor.Professor.cadastrarProfessor()

        elif opcaoUser == 4 or opcaoUser == "4":
            os.system("cls") or None
            if len(professores) != 0:
                os.system("cls")
                cabecalho.cabecalhoEscola(escola.nome)
                for professor in professores:
                    print("--------------------------------------------------------------------------------")
                    professor.imprimir()
            else:
                print("Nenhum Professor foi cadastrado")

        elif opcaoUser == 5 or opcaoUser == "5":
            os.system("cls") or None
            cabecalho.cabecalhoEscola(escola.nome)
            funcionarios += Funcionario.Funcionario.cadastrarFuncionario()
            # sorted(funcionarios, key=lambda Funcionario: Funcionario.getNome())

        elif opcaoUser == 6 or opcaoUser == "6":
            os.system("cls") or None
            if len(funcionarios) != 0:
                os.system("cls")
                cabecalho.cabecalhoEscola(escola.nome)
                for funcionario in funcionarios:
                    print("--------------------------------------------------------------------------------")
                    funcionario.imprimir()
            else:
                print("Nenhum Funcionário foi cadastrado")

        elif opcaoUser == 7 or opcaoUser == "7":
            os.system("cls") or None
            cabecalho.cabecalhoEscola(escola.nome)
            alunos += Aluno.Aluno.cadastrarAluno()

        elif opcaoUser == 8 or opcaoUser == "8":
            os.system("cls") or None
            if len(alunos) != 0:
                os.system("cls")
                cabecalho.cabecalhoEscola(escola.nome)
                for aluno in alunos:
                    print("--------------------------------------------------------------------------------")
                    aluno.imprimir()
            else:
                print("Nenhum aluno foi cadastrado")

        elif opcaoUser == 9 or opcaoUser == "9":
            os.system("cls") or None
            cabecalho.cabecalhoEscola(escola.nome)
            turmas += Turma.Turma.cadastrarTurma()

        elif opcaoUser == 10 or opcaoUser == "10":
            os.system("cls") or None
            if len(turmas) != 0:
                os.system("cls")
                cabecalho.cabecalhoEscola(escola.nome)
                for turma in turmas:
                    print("--------------------------------------------------------------------------------")
                    turma.imprimir()
            else:
                print("Nenhuma turma foi cadastrado")

        elif opcaoUser == 11 or opcaoUser == "11":
            pass

        elif opcaoUser == 12 or opcaoUser == "12":
            root = False
        else:
            erro.mensagemErroMenu()
