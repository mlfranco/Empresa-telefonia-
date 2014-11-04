# -*- encoding: utf-8 -*-

class Excecao(Exception):
	pass

class ErroCredito(Excecao):
	def __init__(self, valor):
		self.__valor = valor
	def mensagem(self, credito):
		print('\nCrédito insuficiente!')
		if(credito == -1):
			print('Seu crédito atual é: R$0.00' % credito)
		else:
			print('Seu crédito atual é: R$%.2f' % credito)
		print('O valor da ligação é: R$%.2f' % self.__valor)

class ErroTipoCelular(Excecao):
	def mensagem(self):
		print('\nO celular informado não é do tipo SmartPhone')

class ErroPromocaoInternet(Excecao):
	def mensagem(self):
		print('\nO celular informado não possui promoções do tipo internet')

