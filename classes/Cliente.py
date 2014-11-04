# -*- encoding: utf-8 -*-

class Cliente:
        '''
	 Método "construtor" da classe Cliente.
	 author	Alexandre Baixo/Matheus Franco/Carlos Segundo.
	 param  self		Objeto invocador.
	 param  nome		nome do cliente.
	 param  cpf_cnpj	numero do cpf/cnpj do cliente.
	 param  endereco	SmathPhone/RegularPhone
	 param  tipo_plano	Cartão/Assinatura
	 param  plano		Plano escolhido pelo dono do celular
	''' 
	def __init__(self, nome, cpf_cnpj, endereco):
		self.__nome = nome
		self.__cpf_cnpj = cpf_cnpj
		self.__endereco = endereco
	def getNome(self):
		return(self.__nome)
	def getCpfCnpj(self):
		return(self.__cpf_cnpj)
	def getEndereco(self):
		return(self.__endereco)

