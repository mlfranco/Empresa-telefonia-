# -*- encoding: utf-8 -*-

class Celular:
	'''
	 Método "construtor" da classe celular.
	 author	Alexandre Baixo/Matheus Franco/Carlos Segundo.
	 param  self		Objeto invocador.
	 param  dono		CPF/CNPJ do dono do celular.
	 param  numero		Número do celular.
	 param  tipo		SmathPhone/RegularPhone
	 param  tipo_plano	Cartão/Assinatura
	 param  plano		Plano escolhido pelo dono do celular
	''' 
	def __init__(self, dono, numero, tipo, tipo_plano, plano):
		self.__dono = dono
		self.__numero = numero
		self.__tipo = tipo
		self.__tipo_plano = tipo_plano
		self.__plano = plano
		self.__credito = -1
		self.__fatura = 0
		self.__lista_de_promocoes = []
		self.__lista_de_ligacoes = []
		self.__lista_de_validade = []
		
	'''
	 Método para retornar o CPF/CNPJ do dono do celular.
	 param  self	Objeto invocador.
	 return dono	CPF/CNPJ do dono do celular.
	''' 
	def getNomeDono(self):
		return(self.__dono)
	def getNumero(self):
		return(self.__numero)
	def getTipo(self):
		return(self.__tipo)
	def getTipoPlano(self):
		return(self.__tipo_plano)
	def getPlano(self):
		return(self.__plano)
	def getCredito(self):
		return(self.__credito)
	def getFatura(self):
		return(self.__fatura)
	def getListaDePromocoes(self):
		return(self.__lista_de_promocoes)
	def getLigacoes(self):
		return(self.__lista_de_ligacoes)
	def getListaDeValidade(self):
		return(self.__lista_de_validade)
	def getVencimento(self):
		return(self.__vencimento)
	def adicionarPromocao(self, promocao):
		self.__lista_de_promocoes.append(promocao)
	def registrarLigacao(self, ligacao):
		self.__lista_de_ligacoes.append(ligacao)
	def adicionarValidade(self, data):
		self.__lista_de_validade.append(data)
	def addCredito(self, valor):
		if(self.__credito == -1):
			self.__credito = self.__credito + (valor + 1)
		else:
			self.__credito = self.__credito + valor
	def addFatura(self, valor):
		self.__fatura = self.__fatura + valor
	def retirarCredito(self, valor):
		self.__credito = self.__credito - valor

class RegularPhone(Celular):
	'''
	 Método "construtor" da classe RegularPhone.
	 author	Alexandre Baixo/Matheus Franco/Carlos Segundo.
	 param  self		Objeto invocador.
	 param  dono		CPF/CNPJ do dono do celular.
	 param  numero		Número do celular.
	 param  tipo		SmathPhone/RegularPhone
	 param  tipo_plano	Cartão/Assinatura
	 param  plano		Plano escolhido pelo dono do celular
	 param	vencimento  Caso seja do tipo Assinante dia do vencimento da fatura.
	''' 
	def __init__(self, dono, numero, tipo, tipo_plano, plano, vencimento):
		Celular.__init__(self, dono, numero, tipo, tipo_plano, plano)
		self.__vencimento = vencimento
	def getVencimento(self):
		return(self.__vencimento)
	def setVencimento(self, data):
		self.__vencimento = data	

class SmartPhone(Celular):
	'''
	 Método "construtor" da classe SmartPhone.
	 author	Alexandre Baixo/Matheus Franco/Carlos Segundo.
	 param  self		Objeto invocador.
	 param  dono		CPF/CNPJ do dono do celular.
	 param  numero		Número do celular.
	 param  tipo		SmathPhone/RegularPhone
	 param  tipo_plano	Cartão/Assinatura
	 param  plano		Plano escolhido pelo dono do celular
	 param	vencimento  Caso seja do tipo Assinante dia do vencimento da fatura.
	''' 
	def __init__(self, dono, numero, tipo, tipo_plano, plano, vencimento):
		Celular.__init__(self, dono, numero, tipo, tipo_plano, plano)
		self.__vencimento = vencimento
		self.__lista_de_promocoes_internet = []
		self.__lista_de_validade_internet = []
		self.__lista_de_ligacoes_internet = []
	def getVencimento(self):
		return(self.__vencimento)
	def getListaDePromocoesInternet(self):
		return(self.__lista_de_promocoes_internet)
	def getListaDeValidadeInternet(self):
		return(self.__lista_de_validade_internet)
	def getLigacoesInternet(self):
		return(self.__lista_de_ligacoes_internet)
	def setVencimento(self, data):
		self.__vencimento = data			
	def adicionarPromocaoInternet(self, promocao):
		self.__lista_de_promocoes_internet.append(promocao)
	def adicionarValidadeInternet(self, data):
		self.__lista_de_validade_internet.append(data)
	def adicionarLigacaoInternet(self, ligacao):
		self.__lista_de_ligacoes_internet.append(ligacao)

