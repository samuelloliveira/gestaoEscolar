# Classe Turma

class Turma:

    # Método Inicializador
    def __init__(self, codigoTurma, materias, curso, alunos, dataInicio, dataFinal):
        self.codigoTurma = codigoTurma
        self.materias = materias
        self.curso = curso
        self.alunos = alunos
        self.dataInicio = dataInicio
        self.dataFinal = dataFinal

    # Retornando o valor dos atributos através método GET
    def getCodigoTurma(self):
        return self.codigoTurma

    def getMaterias(self):
        return self.materias

    def getCursos(self):
        return self.cursos

    def getAlunos(self):
        return self.alunos

    def getDataInicio(self):
        return self.dataInicio

    def getDataFinal(self):
        return self.dataFinal

    # Inserindo dados nos atributos pelo método SET
    def setCodigoTurma(self, codigoTurma):
        self.codigoTurma = codigoTurma

    def setMaterias(self, materias):
        self.materias = materias

    def setCursos(self, cursos):
        self.cursos = cursos

    def setAlunos(self, alunos):
        self.alunos = alunos

    def setDataInicio(self, dataInicio):
        self.dataInicio = dataInicio

    def setDataFinal(self, dataFinal):
        self.dataFinal = dataFinal