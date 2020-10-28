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
    @property
    def codigoTurma(self):
        return self.codigoTurma

    @property
    def materias(self):
        return self.materias

    @property
    def curso(self):
        return self.curso

    @property
    def alunos(self):
        return self.alunos

    @property
    def dataInicio(self):
        return self.dataInicio

    @property
    def dataFinal(self):
        return self.dataFinal

    # Inserindo dados nos atributos pelo método SET
    @codigoTurma.setter
    def codigoTurma(self, codigoTurma):
        self.codigoTurma = codigoTurma

    @materias.setter
    def materias(self, materias):
        self.materias = materias

    @curso.setter
    def curso(self, curso):
        self.curso = curso

    @alunos.setter
    def alunos(self, alunos):
        self.alunos = alunos

    @dataInicio.setter
    def dataInicio(self, dataInicio):
        self.dataInicio = dataInicio

    @dataFinal.setter
    def dataFinal(self, dataFinal):
        self.dataFinal = dataFinal
