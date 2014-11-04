# -*- encoding: utf-8 -*-

class Operadora():
	'''
	 Método "construtor" da classe Operadora.
	 author	Alexandre Baixo/Matheus Franco/Carlos Segundo.
	 param  self		Objeto invocador.
	''' 
	def __init__(self):
		self.__lista_de_clientes = []
		self.__lista_de_celulares = []
		self.__lista_de_planos_cartao = []
		self.__lista_de_planos_assinatura = []
		self.__lista_de_promocoes_internet = []
		self.__lista_de_promocoes_minutos = []
		self.__lista_de_promocoes_bonus = []
	def getListaDeClientes(self):
		return(self.__lista_de_clientes)
	def getListaDeCelulares(self):
		return(self.__lista_de_celulares)
	def getListaPlanosCartao(self):
		return(self.__lista_de_planos_cartao)
	def getListaPlanosAssinatura(self):
		return(self.__lista_de_planos_assinatura)
	def getListaPromocoesInternet(self):
		return(self.__lista_de_promocoes_internet)	
	def getListaPromocoesMinutos(self):
		return(self.__lista_de_promocoes_minutos)
	def getListaPromocoesBonus(self):
		return(self.__lista_de_promocoes_bonus)
	def adicionarListaCliente(self, cliente):
		self.__lista_de_clientes.append(cliente)
	def adicionarListaCelular(self, celular):
		self.__lista_de_celulares.append(celular)
	def adicionarListaPlanoCartao(self, plano):
		self.__lista_de_planos_cartao.append(plano)
	def adicionarListaPlanoAssinatura(self, plano):
		self.__lista_de_planos_assinatura.append(plano)
	def adicionarListaPromocoesInternet(self, promocao):
		self.__lista_de_promocoes_internet.append(promocao)
	def adicionarListaPromocoesMinutos(self, promocao):
		self.__lista_de_promocoes_minutos.append(promocao)
	def adicionarListaPromocoesBonus(self, promocao):
		self.__lista_de_promocoes_bonus.append(promocao)
	def getProximoNumero(self):
		if(len(self.__lista_de_celulares) == 0):
			return(10000000)
		else:
			for c in self.__lista_de_celulares:
				numero = c.getNumero()
			return(numero + 1)

