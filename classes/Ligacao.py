# -*- encoding: utf-8 -*-

class Ligacao:
        '''
         Método "construtor" da classe Liga��o.
	 author	Alexandre Baixo/Matheus Franco/Carlos Segundo.
	 param  self		    Objeto invocador.
	 param  numero_do_celular   numero do celular que esta fazendo a liga��o.
	 param  data                data da liga��o.
	 param  hora                hora da liga��o
	 param  valor   	    valor da liga��o
	 param  status	  	    status da liga��o
	''' 
	def __init__(self, numero_do_celular, data, hora, valor, status):
		self.__numero_do_celular = numero_do_celular
		self.__data = data
		self.__hora = hora
		self.__valor = valor
		self.__status = status
	def getNumero(self):
		return(self.__numero)
	def getData(self):
		return(self.__data)
	def getHora(self):
		return(self.__hora)
	def getValor(self):
		return(self.__valor)
	def getStatus(self):
		return(self.__status)

class LigacaoInternet(Ligacao):
        '''
         Método que retorna a dura��o da chamada feita pela internet.
	 author	Alexandre Baixo/Matheus Franco/Carlos Segundo.
	 param  self		    Objeto invocador.
	 param  numero_do_celular   numero do celular que esta fazendo a liga��o.
	 param  data                data da liga��o.
	 param  hora                hora da liga��o
	 param  valor   	    valor da liga��o
	 param  status	  	    status da liga��o
         return duracao             dura��o da chamada
	''' 

	def __init__(self, numero_do_celular, data, hora, duracao, valor, status):
		Ligacao.__init__(self, numero_do_celular, data, hora, valor, status)
		self.__duracao = duracao * 60
	def getDuracao(self):
		return(self.__duracao / 60)

class LigacaoSimples(Ligacao):
        '''
         Método que retorna a dura��o da chamada.
	 author	Alexandre Baixo/Matheus Franco/Carlos Segundo.
	 param  self		    Objeto invocador.
	 param  numero_do_celular   numero do celular que esta fazendo a liga��o.
	 param  data                data da liga��o.
	 param  hora                hora da liga��o
	 param  valor   	    valor da liga��o
	 param  status	  	    status da liga��o
         return duracao             dura��o da chamada
	'''
	def __init__(self, numero_do_celular, data, hora, duracao, valor, status):
		Ligacao.__init__(self, numero_do_celular, data, hora, valor, status)
		self.__duracao = duracao
	def getDuracao(self):
		return(self.__duracao)

