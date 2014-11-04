# -*- encoding: utf-8 -*-

class Promocao:
	'''
	 Método "construtor" da classe promocao.
	 author	Alexandre Baixo/Matheus Franco/Carlos Segundo.
	 param  self		Objeto invocador.
	 param  nome 		Nome da promocao.
	 param  validade 	validade da promocao.
	''' 
	def __init__(self, nome, validade):
		self.__nome = nome
		self.__validade = validade
	def getNome(self):
		return(self.__nome)
	def getValidade(self):
		return(self.__validade)

class PromocaoInternet(Promocao):
	'''
	 Método "construtor" da classe PromocaoInternet.
	 author	Alexandre Baixo/Matheus Franco/Carlos Segundo.
	 param  self		Objeto invocador.
	 param  nome 		Nome da promocao.
	 param	velocidade	Velocidade da internet enquanto a franquia nao for totalmente usada.
	 param  franquia 	quantidade de MB da promocao.
	 param  velocidade_alem_da_franquia Velocidade de navegação apos termino da franquia.
	 param	validade	tempo de validade da promocao.
	''' 
	def __init__(self, nome, velocidade, franquia, velocidade_alem_da_franquia, validade):
		Promocao.__init__(self, nome, validade)
		self.__velocidade = velocidade
		self.__franquia = franquia
		self.__velocidade_alem_da_franquia = velocidade_alem_da_franquia
	def getVelocidade(self):
		return(self.__velocidade)
	def getFranquia(self):
		return(self.__franquia)
	def getVelocidadeAlem(self):
		return(self.__velocidade_alem_da_franquia)
	def removerFranquia(self, valor):
		self.__franquia = self.__franquia - valor

class PromocaoMinutos(Promocao):
	'''
	 Método "construtor" da classe promocao de Minutos.
	 author	Alexandre Baixo/Matheus Franco/Carlos Segundo.
	 param  self		Objeto invocador.
	 param  nome 		Nome da promocao.
	 param  validade 	validade da promocao.
	 param	quantidade	Quantidade de minitos que a promocao oferece.
	''' 
	def __init__(self, nome, validade, quantidade):
		Promocao.__init__(self, nome, validade)
		self.__quantidade = quantidade
	def getQuantidade(self):
		return(self.__quantidade)
	def removerQuantidade(self, valor):
		self.__quantidade = self.__quantidade - valor

class PromocaoBonus(Promocao):
	'''
	 Método "construtor" da classe promocao.
	 author	Alexandre Baixo/Matheus Franco/Carlos Segundo.
	 param  self		Objeto invocador.
	 param  nome 		Nome da promocao.
	 param  validade 	validade da promocao.
	 param	quantidade	Quantidade de bonus que a promocao oferece.
	 param 	limite_diario	limite de bonus que podem ser usados em um unico dia.
	''' 
	def __init__(self, nome, validade, quantidade, limite_diario):
		Promocao.__init__(self, nome, validade)
		self.__quantidade = quantidade
		self.__limite_diario = limite_diario
	def getQuantidade(self):
		return(self.__quantidade)
	def getLimiteDiario(self):
		return(self.__limite_diario)
	def removerQuantidade(self, valor):
		self.__quantidade = self.__quantidade - valor

