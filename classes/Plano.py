# -*- encoding: utf-8 -*-

class Plano:
	'''
	 Método "construtor" da classe Plano.
	 author	Alexandre Baixo/Matheus Franco/Carlos Segundo.
	 param  self		Objeto invocador.
	 param  nome 		Nome da promocao.
	 param	valor		Valos mensal a ser pago pelo plano contratado.
	''' 
	def __init__(self, nome, valor):
		self.__nome = nome
		self.__valor_por_minuto = valor
		self.__lista_de_promocoes_regularphone = []
		self.__lista_de_promocoes_smartphone = []
	def getNome(self):
		return(self.__nome)
	def getValorMinuto(self):
		return(self.__valor_por_minuto)
	def getListaPromocoesRegularPhone(self):
		return(self.__lista_de_promocoes_regularphone)
	def getListaPromocoesSmartPhone(self):
		return(self.__lista_de_promocoes_smartphone)
	def adicionarPromocaoRegularPhone(self, promocao):
		self.__lista_de_promocoes_regularphone.append(promocao)
	def adicionarPromocaoSmartPhone(self, promocao):
		self.__lista_de_promocoes_smartphone.append(promocao)

class PlanoCartao(Plano):
	pass

class PlanoAssinatura(Plano):
	pass

