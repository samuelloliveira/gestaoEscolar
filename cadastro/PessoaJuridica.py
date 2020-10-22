# Classe Pessoa Jurídica

from cadastro.Pessoa import Pessoa

class PessoaJuridica(Pessoa):

  # Método inicializador
  def __init__(self, nome, telefone, endereco, cnpj, dataAbertura):
    super().__init__(nome, telefone, endereco)
    self.__cnpj = cnpj
    self.__dataAbertura = dataAbertura

  def __str__(self):
    return self.getNome()

  # Retornando o valor dos atributos através do método GET
  def getCnpj(self):
    return self.__cnpj

  def getDataAbertura(self):
    return self.__dataAbertura

  # Inserindo dados nos atributos pelo método SET
  def setCnpj(self, cnpj):
    self.__cnpj = cnpj

  def setDataNascimento(self, dataNascimento):
    self.__dataNascimento = dataNascimento