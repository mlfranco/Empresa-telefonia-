# -*- encoding: utf-8 -*-
from datetime import *
from time import *
from classes.Cliente import *
from classes.Celular import *
from classes.Plano import *
from classes.Promocao import *
from classes.Ligacao import *
from classes.Operadora import *
from classes.Excecao import *
import pickle

class Interface:
	def __init__(self):
		try:
			the_file = open('operadora_celular.dat', 'rb')
			self.__operadora = pickle.load(the_file)
		except:
			self.__operadora = Operadora()
	
	def menu(self):
		while(True):
			print('\n\n\t#MENU#')
			print('\n1)  Habilitar celular\n2)  Adicionar novo plano\n3)  Adicionar nova promoção')
			print('4)  Adicionar promoção à um celular\n5)  Adicionar créditos')
			print('6)  Registrar ligação simples\n7)  Registrar ligação internet')
			print('8)  Listar dados de internet\n9)  Valor da conta\n10) Listar créditos e validade')
			print('11) Listar extrato de ligações\n12) Listar clientes\n13) Listar planos')
			print('14) Listar promoções\n15) Listar celulares\n16) Checar vencimentos')
			print('17) Checar validade de promoções\n18) Sair')
			while(True):
				try:
					escolha_menu = int(input('\nEscolha uma opção: \n>> '))
					break
				except:
					print('\nOpção inválida')
				
			if escolha_menu == 1:
				self.opcao_1()
				
			elif(escolha_menu == 2):
				self.opcao_2()
				
			elif(escolha_menu == 3):
				self.opcao_3()
		
			elif(escolha_menu == 4):
				self.opcao_4()

			elif(escolha_menu == 5):
				self.opcao_5()
		
			elif(escolha_menu == 6):
				self.opcao_6()

			elif(escolha_menu == 7):
				self.opcao_7()

			elif(escolha_menu == 8):
				self.opcao_8()

			elif(escolha_menu == 9):
				self.opcao_9()

			elif(escolha_menu == 10):
				self.opcao_10()

			elif(escolha_menu == 11):
				self.opcao_11()
		
			elif(escolha_menu == 12):
				self.opcao_12()

			elif(escolha_menu == 13):
				self.opcao_13()

			elif(escolha_menu == 14):
				self.opcao_14()

			elif(escolha_menu == 15):
				self.opcao_15()

			elif(escolha_menu == 16):
				self.opcao_16()

			elif(escolha_menu == 17):
				self.opcao_17()

			elif(escolha_menu == 18):
				self.opcao_18()
				break
		
			else:
				print('\nOpção inválida')
				continue	

	def opcao_1(self):
		try:
			escolha = int(input('Cliente já cadastrado?\n1) Sim\n2) Não\n>> '))
			if(escolha == 1):
				lista_de_clientes = self.__operadora.getListaDeClientes()
				if(len(lista_de_clientes) == 0):
					print('\nNão há clientes cadastrados')
					return
				i = 1
				print('\nLista de clientes:')
				for c in lista_de_clientes:
					print('\t%d) %s' % (i, c.getNome()))
					i += 1		
				try:
					escolha = int(input('\nCliente para o qual será habilitado o celular\n>> '))
					if(escolha >= 1) and (escolha <= len(lista_de_clientes)):
						cliente = lista_de_clientes[escolha - 1]
					else:
						print('\nOpção inválida')
						return
				except:
					print('\nOpção inválida')
					return
			elif(escolha == 2):
				cliente = self.criarCliente(self.__operadora)
			else:
				print('\nOpção inválida')
				return
		except:
			print('\nOpção inválida')
			return
		tipo_de_celular = self.escolhaTipoCelular()
		if(tipo_de_celular == -1):
			return
		tipo_de_plano = self.escolhaTipoPlano()
		if(tipo_de_plano == -1):
			return
		hoje = date.today()
		if(tipo_de_celular == 1) and (tipo_de_plano == 1):
			plano = self.escolhaPlanoCartao(self.__operadora)
			if(plano != -1):
				cpf_cnpj = cliente.getCpfCnpj()
				numero = self.__operadora.getProximoNumero()
				celular = RegularPhone(cpf_cnpj, numero, 'RegularPhone', 'Cartão', plano, hoje)
				self.escolhaPromocaoRegularPhoneCartao(self.__operadora, celular)
		elif(tipo_de_celular == 1) and (tipo_de_plano == 2):
			plano = self.escolhaPlanoAssinatura(self.__operadora)
			if(plano != -1):
				dia = self.vencimentoFatura()
				cpf_cnpj = cliente.getCpfCnpj()
				numero = self.__operadora.getProximoNumero()
				celular = RegularPhone(cpf_cnpj, numero, 'RegularPhone', 'Assinatura', plano, dia)
				self.escolhaPromocaoRegularPhoneAssinatura(self.__operadora, celular)
		elif(tipo_de_celular == 2) and (tipo_de_plano == 1):
			plano = self.escolhaPlanoCartao(self.__operadora)
			if(plano != -1):
				cpf_cnpj = cliente.getCpfCnpj()
				numero = self.__operadora.getProximoNumero()
				celular = SmartPhone(cpf_cnpj, numero, 'SmartPhone', 'Cartão', plano, hoje)
				self.escolhaPromocaoSmartPhoneCartao(self.__operadora, celular)
		elif(tipo_de_celular == 2) and (tipo_de_plano == 2):
			plano = self.escolhaPlanoAssinatura(self.__operadora)
			if(plano != -1):
				dia = self.vencimentoFatura()
				cpf_cnpj = cliente.getCpfCnpj()
				numero = self.__operadora.getProximoNumero()
				celular = SmartPhone(cpf_cnpj, numero, 'SmartPhone', 'Assinatura', plano, dia)
				self.escolhaPromocaoSmartPhoneAssinatura(self.__operadora, celular)		
		if(plano != -1) and (escolha == 1):
			self.__operadora.adicionarListaCelular(celular)
		elif(plano != -1) and (escolha == 2):
			self.__operadora.adicionarListaCelular(celular)
			self.__operadora.adicionarListaCliente(cliente)

	def opcao_2(self):
		try:
			tipo_do_plano = int(input('\nEscolha o tipo do plano:\n1) Cartão\n2) Assinatura\n>> '))
			if(tipo_do_plano != 1) and (tipo_do_plano != 2):
				print('\nOpção inválida')
				return
		except:
			print('\nOpção inválida')
			return
		print('\nDigite os dados do plano')
		nome = raw_input('Nome: ')
		while(True):
			try:
				valor = float(input('Valor do minuto: '))
				break
			except:
				print('Valor inválido')
		if(tipo_do_plano == 1):
			plano = PlanoCartao(nome, valor)
			self.__operadora.adicionarListaPlanoCartao(plano)
		else:
			plano = PlanoAssinatura(nome, valor)
			self.__operadora.adicionarListaPlanoAssinatura(plano)

	def opcao_3(self):
		try:
			print('\nEscolha o tipo da promoção:\n1) Internet\n2) Minutos\n3) Bônus')
			tipo_da_promocao = int(input('>> '))
			if (tipo_da_promocao < 1) and (tipo_da_promocao > 3):
				print('\nOpção inválida')
				return
		except:
			print('\nOpção inválida')
			return
		print('\nDigite os dados da promoção')
		nome = raw_input('Nome: ')
		if(tipo_da_promocao == 1):
			while(True):
				try:
					validade = int(input('Validade (dias): '))
					velocidade = float(input('Velocidade (somente o valor)(Mbps): '))
					franquia = int(input('Franquia (somente o valor)(Mb): '))
					alem = float(input('Velocidade além da franquia (somente o valor)(Mbps): '))
					break
				except:
					print('\nDado inválido')
			promocao = PromocaoInternet(nome, velocidade, franquia, alem, validade)
			self.__operadora.adicionarListaPromocoesInternet(promocao)
		elif(tipo_da_promocao == 2):
			while(True):
				try:
					validade = int(input('Validade (dias): '))
					quantidade = int(input('Quantia de minutos: '))
					break
				except:
					print('\nDado inválido')
			promocao = PromocaoMinutos(nome, validade, quantidade)
			self.__operadora.adicionarListaPromocoesMinutos(promocao)
		else:
			while(True):
				try:
					validade = int(input('Validade (dias): '))
					quantidade = int(input('Quantia de bônus: '))
					limite_diario = int(input('Limite diário: '))
					break
				except:
					print('\nDado inválido')
			promocao = PromocaoBonus(nome, validade, quantidade, limite_diario)
			self.__operadora.adicionarListaPromocoesBonus(promocao)
			
	def opcao_4(self):
		lista_de_celulares = self.__operadora.getListaDeCelulares()
		if(self.mostrarNumerosCelulares(self.__operadora, lista_de_celulares) == -1):
			return
		try:
			numero = int(input('\nInforme o número do celular\n>> '))
		except:
			print('Número inválido')
			return
		for c in lista_de_celulares:
			if(numero == c.getNumero()):
				if('RegularPhone' in c.getTipo()):
					self.adicionarPromocaoSimplesCelular(self.__operadora, c)
				elif('SmartPhone' in c.getTipo()):
					self.adicionarPromocaoInternetCelular(self.__operadora, c)
					self.adicionarPromocaoSimplesCelular(self.__operadora, c)
	
	def opcao_5(self):
		lista_de_celulares = self.__operadora.getListaDeCelulares()
		if(self.mostrarNumerosCelulares(self.__operadora, lista_de_celulares) == -1):
			return
		try:
			numero = int(input('\nInforme o número do celular\n>> '))
			valor = float(input('\nInforme o valor de crédito\n>> '))
		except:
			print('Dado inválido')
			return
		for c in lista_de_celulares:
			if(numero == c.getNumero()):
				if('Cartão' in c.getTipoPlano()):
					c.addCredito(valor)
					hoje = date.today()
					dias = timedelta(days = 180)
					c.setVencimento(hoje + dias)
				else:
					print('\nCelular não possui plano do tipo cartão')

	def opcao_6(self):	
		lista = self.__operadora.getListaDeCelulares()
		if(self.mostrarNumerosCelulares(self.__operadora, lista) == -1):
			return
		try:
			numero = int(input('\nNúmero do celular: '))
			print('Insira o dia, mês e ano da ligação')
			dia = int(input('Dia (dd): '))
			if(dia < 1) or (dia > 30):
				print('\nDia inválido')
				return
			mes = int(input('Mês (mm): '))
			if(mes < 1) or (mes > 12):
				print('\nMês inválido')
				return
			ano = int(input('Ano (aaaa): '))
			hora = raw_input('Hora da ligação (hh:mm): ')
			duracao = int(input('Duração (minutos): '))
		except:
			print('Dado inválido')
			return
		data = datetime(ano, mes, dia)
		end = False
		for c in lista:
			if(c.getNumero() == numero):
				lista_prom = c.getListaDePromocoes()
				custo = c.getPlano().getValorMinuto() * duracao
				if('Cartão' in c.getTipoPlano()):
					if(len(lista_prom) != 0):
						for p in lista_prom:
							if(p.getQuantidade() > duracao) and (p.getLimiteDiario() > duracao):
								p.removerQuantidade(duracao)
								l = LigacaoSimples(numero, data, hora, duracao, custo, 0)
								c.registrarLigacao(l)
								end = True
								break
					if(end == False):
						if(c.getCredito() < custo):
							try:
								raise ErroCredito(custo)
							except ErroCredito as e:
								e.mensagem(c.getCredito())
						else:
							c.retirarCredito(custo)
							l = LigacaoSimples(numero, data, hora, duracao, custo, 1)
							c.registrarLigacao(l)
				if('Assinatura' in c.getTipoPlano()):
					if(len(lista_prom) != 0):
						for p in lista_prom:
							if(p.getQuantidade() > duracao):
								p.removerQuantidade(duracao)
								l = LigacaoSimples(numero, data, hora, duracao, custo, 0)
								c.registrarLigacao(l)
								end = True
								break
					if(end == False):
						c.addFatura(custo)
						l = LigacaoSimples(numero, data, hora, duracao, custo, 1)
						c.registrarLigacao(l)

	def opcao_7(self):
		lista = self.__operadora.getListaDeCelulares()
		if(self.mostrarNumerosCelulares(self.__operadora, lista) == -1):
			return
		try:
			numero = int(input('\nNúmero do celular: '))
			print('Insira o dia, mês e ano da ligação')
			dia = int(input('Dia (dd): '))
			if(dia < 1) or (dia > 30):
				print('\nDia inválido')
				return
			mes = int(input('Mês (mm): '))
			if(mes < 1) or (mes > 12):
				print('\nMês inválido')
				return
			ano = int(input('Ano (aaaa): '))
			hora = raw_input('Hora da ligação (hh:mm): ')
			duracao = int(input('Duração (minutos): '))
		except:
			print('\nDado inválido')
			return
		data = datetime(ano, mes, dia)
		for c in lista:
			if(c.getNumero() == numero):
				if('SmartPhone' not in c.getTipo()):
					try:
						raise ErroTipoCelular()
					except ErroTipoCelular as e:
						e.mensagem()
				else:
					if(len(c.getListaDePromocoesInternet()) == 0):
						try:
							raise ErroPromocaoInternet()
						except ErroPromocaoInternet	as e:
							e.mensagem()
					else:
						custo = duracao * 60 * c.getListaDePromocoesInternet()[0].getVelocidade()
						l = LigacaoInternet(numero, data, hora, duracao, custo)
						c.getListaDePromocoesInternet()[0].removerFranquia(custo)
						c.adicionarLigacaoInternet(l)

	def opcao_8(self):
		lista = self.__operadora.getListaDeCelulares()
		if(self.mostrarNumerosCelulares(self.__operadora, lista) == -1):
			return
		try:
			numero = int(input('\nNúmero do celular: '))
		except:
			print('\nNúmero inválido')
			return
		end = False
		for c in lista:
			if(c.getNumero() == numero):
				if('SmartPhone' not in c.getTipo()):
					print('\nCelular não possui promoção do tipo internet')
					end = True
				if(len(c.getListaDePromocoesInternet()) == 0):
					print('\nCelular não possui promoção do tipo internet')
					end = True
				if(end == False):
					promocao = c.getListaDePromocoesInternet()[0]
					if(promocao.getFranquia() <= 0):
						print('\n\tFranquia atual: 0 Megabytes')
						print('\tVelocidade atual: %d Mbps' % promocao.getVelocidadeAlem())
					else:
						print('\n\tFranquia atual: %d Megabytes' % promocao.getFranquia())
						print('\tVelocidade atual %d Mbps' % promocao.getVelocidade())

	def opcao_9(self):
		hoje = date.today()
		lista = self.__operadora.getListaDeCelulares()
		if(self.mostrarNumerosCelulares(self.__operadora, lista) == -1):
			return
		try:
			numero = int(input('\nNúmero do celular: '))
		except:
			print('\nNúmero inválido')
			return
		for c in lista:
			if(c.getNumero() == numero):
				if('Assinatura' in c.getTipoPlano()):
					valor = 0
					dia = c.getVencimento()
					if(hoje.month == 1):
						data_inicial = datetime(hoje.year - 1, 12, dia)
					else:
						data_inicial = datetime(hoje.year, hoje.month - 1, dia)
					data_final = datetime(hoje.year, hoje.month, dia)
					lista_ligacoes = c.getLigacoes()
					for l in lista_ligacoes:
						if(l.getData() > data_inicial) and (l.getData() <= data_final):
							if(l.getStatus() == 0):
								valor += l.getValor()
					print('\nValor da conta: %2.f' % valor)
				else:
					print('\nCelular não possui plano do tipo assinatura')
					return

	def opcao_10(self):
		lista_de_celulares = self.__operadora.getListaDeCelulares()
		if(self.mostrarNumerosCelulares(self.__operadora, lista_de_celulares) == -1):
			return
		try:
			numero = int(input('\nInforme o número do celular\n>> '))
		except:
			print('\nDado inválido')
			return
		for c in lista_de_celulares:
			if(c.getNumero() == numero) and ('Cartão' in c.getTipoPlano()):
				print('\n\tCpf do proprietário: %s' % c.getNomeDono())
				print('\tNúmero do aparelho: %d' % c.getNumero())
				print('\tTipo do celular: %s' % c.getTipo())
				print('\tTipo do plano adquirido: %s' % c.getTipoPlano())
				if(c.getCredito() == -1):
					print('\tSaldo de crédito: R$0.00')
				else:
					print('\tSaldo de crédito: %.2f' % c.getCredito())
					print('\tVencimento dos créditos: %s' % c.getVencimento().strftime('%d/%m/%Y'))

	def opcao_11(self):
		lista = self.__operadora.getListaDeCelulares()
		if(self.mostrarNumerosCelulares(self.__operadora, lista) == -1):
			return
		try:
			numero = int(input('\nNúmero do celular: '))
			print('Insira o dia, mês e ano inicial do extrato')
			dia = int(input('Dia (dd): '))
			if(dia < 1) or (dia > 30):
				print('\nDia inválido')
				return
			mes = int(input('Mês (mm): '))
			if(mes < 1) or (mes > 12):
				print('\nMês inválido')
				return
			ano = int(input('Ano (aaaa): '))
		except:
			print('\nDado inválido')
			return
		data = datetime(ano, mes, dia)
		for c in lista:
			if(c.getNumero() == numero):
					lista_simples = c.getLigacoes()
					i = 1
					if(len(lista_simples) != 0):
						for l in lista_simples:
							if(l.getData() >= data):
								print('\nLigação %d:' % i)
								print('\tValor cobrado: R$%.2f' % l.getValor())
								print('\tData da ligação: %s' % l.getData().strftime('%d/%m/%Y'))
								print('\tDuração da ligação: %d minutos\n' % l.getDuracao())
								i += 1
					if('SmartPhone' in c.getTipo()):
						lista_internet = c.getLigacoesInternet()
						if(len(lista_internet) != 0):
							for l in lista_internet:
								if(l.getData() >= data):
									print('\nLigação %d:' % i)
									print('\tValor cobrado: %d Megabytes' % l.getValor())
									print('\tData da ligação: %s' % l.getData().strftime('%d/%m/%Y'))
									print('\tDuração da ligação: %d minutos\n' % l.getDuracao())
									i += 1

	def opcao_12(self):
		lista = self.__operadora.getListaDeClientes()
		i = 1
		if(len(lista) != 0):
			for c in lista:
				print('Cliente %d)' % i)
				print('\tNome: %s' % c.getNome())
				print('\tCPF/CNPJ: %s' % c.getCpfCnpj())
				print('\tEndereço: %s' % c.getEndereco())
				i += 1
				
	def opcao_13(self):
		lista_cartao = self.__operadora.getListaPlanosCartao()
		lista_assinatura = self.__operadora.getListaPlanosAssinatura()
		i = 1
		if(len(lista_cartao) != 0):
			print('\nPlanos do tipo cartão:\n')
			for p in lista_cartao:
				print('Plano %d)' % i)
				print('\tNome: %s' % p.getNome())
				print('\tValor por minuto: R$%.2f' % p.getValorMinuto())
				i += 1
		i = 1
		if(len(lista_assinatura) != 0):
			print('\nPlanos do tipo assinatura:\n')
			for p in lista_assinatura:
				print('Plano %d)' % i)
				print('\tNome: %s' % p.getNome())
				print('\tValor por minuto: R$%.2f' % p.getValorMinuto())
				i += 1

	def opcao_14(self):
		lista = self.__operadora.getListaPromocoesInternet()
		i = 1
		if(len(lista) != 0):
			print('\nPromoções do tipo internet:\n')
			for p in lista:
				print('Promoção %d)' % i)
				print('\tNome: %s' % p.getNome())
				print('\tVelocidade: %d' % p.getVelocidade())
				print('\tFranquia: %d' % p.getFranquia())
				print('\tVelocidade além da franquia: %d' % p.getVelocidadeAlem())
				print('\tValidade: %d\n' % p.getValidade())
				i += 1
		lista = self.__operadora.getListaPromocoesMinutos()
		i = 1
		if(len(lista) != 0):
			print('\nPromoções do tipo minutos:\n')
			for p in lista:
				print('Promoção %d)' % i)
				print('\tNome: %s' % p.getNome())
				print('\tValidade: %d' % p.getValidade())
				print('\tQuantidade: %d\n' % p.getQuantidade())
				i += 1
		lista = self.__operadora.getListaPromocoesBonus()
		i = 1
		if(len(lista) != 0):
			print('\nPromoções do tipo bônus:\n')
			for p in lista:
				print('Promoção %d)' % i)
				print('\tNome: %s' % p.getNome())
				print('\tValidade: %d' % p.getValidade())
				print('\tQuantidade: %d' % p.getQuantidade())
				print('\tLimiteDiário: %d' % p.getLimiteDiario())
				i += 1

	def opcao_15(self):
		lista = self.__operadora.getListaDeCelulares()
		i = 1
		for c in lista:
			if('Cartão' in c.getTipoPlano()):
				print('\nCelular %d)' % i)
				print('\tCpf do proprietário: %s' % c.getNomeDono())
				print('\tNúmero do aparelho: %d' % c.getNumero())
				print('\tTipo do celular: %s' % c.getTipo())
				print('\tTipo do plano adquirido: %s' % c.getTipoPlano())
				if(c.getCredito() == -1):
					print('\tSaldo de crédito: R$0.00')
				else:
					print('\tSaldo de crédito: R$%.2f' % c.getCredito())
					print('\tVencimento dos créditos: %s' % c.getVencimento().strftime('%d/%m/%Y'))
				i += 1
			else:
				print('\nCelular %d)' % i)
				print('\tCpf do proprietário: %s' % c.getNomeDono())
				print('\tNúmero do aparelho: %d' % c.getNumero())
				print('\tTipo do celular: %s' % c.getTipo())
				print('\tTipo do plano adquirido: %s' % c.getTipoPlano())
				print('\tValor da fatura até o momento: R$%.2f' % c.getFatura())
				print('\tDia do vencimento da fatura: %d' % c.getVencimento())
				i += 1

	def opcao_16(self):
		lista = self.__operadora.getListaDeCelulares()
		hoje = date.today()
		vencido = False
		for c in lista:
			lista_validade = c.getListaDeValidade()
			if('Cartão' in c.getTipoPlano()):
				if(hoje > c.getVencimento()):
					vencido = True
			elif('Assinatura' in c.getTipoPlano()):
				if(hoje.day > c.getVencimento()):
					vencido = True
			for v in lista_validade:
				if(hoje > v):
					vencido = True
			if('SmartPhone' in c.getTipo()):
				lista_validade = c.getListaDeValidadeInternet()
				for v in lista_validade:
					if(hoje > v):
						vencido = True
			if(vencido == True):
				cpf = c.getNomeDono()
				lista = self.__operadora.getListaDeClientes()
				for cl in lista:
					if(cpf == cl.getCpfCnpj()):
						print('\nCliente:')
						print('\tNome: %s' % cl.getNome())
						print('\tCPF/CNPJ: %s' % cl.getCpfCnpj())
						print('\tEndereço: %s' % cl.getEndereco())
				if('Cartão' in c.getTipoPlano()):
					print('\nCelular:')
					print('\tCpf do proprietário: %s' % c.getNomeDono())
					print('\tNúmero do aparelho: %d' % c.getNumero())
					print('\tTipo do celular: %s' % c.getTipo())
					print('\tTipo do plano adquirido: %s' % c.getTipoPlano())
					if(c.getCredito() == -1):
						print('\tSaldo de crédito: R$0.00')
					else:
						print('\tSaldo de crédito: R$%.2f' % c.getCredito())
						print('\tVencimento dos créditos: %s' % c.getVencimento().strftime('%d/%m/%Y'))
				else:
					print('\nCelular:')
					print('\tCpf do proprietário: %s' % c.getNomeDono())
					print('\tNúmero do aparelho: %d' % c.getNumero())
					print('\tTipo do celular: %s' % c.getTipo())
					print('\tTipo do plano adquirido: %s' % c.getTipoPlano())
					print('\tDia do vencimento da fatura: %d' % c.getVencimento())

	def opcao_17(self):
		lista_de_celulares = self.__operadora.getListaDeCelulares()
		if(self.mostrarNumerosCelulares(self.__operadora, lista_de_celulares) == -1):
			return
		try:
			numero = int(input('\nInforme o número do celular\n>> '))
		except:
			print('\nNúmero inválido')
			return
		for c in lista_de_celulares:
			if(numero == c.getNumero()):
				i = 0
				for p in c.getListaDePromocoes():
					print('\nPromoção:\n\tNome: %s' % p.getNome())
					print('\tValidade: ' + c.getListaDeValidade()[i].strftime('%d/%m/%Y'))
					i += 1
				if('SmartPhone' in c.getTipo()):
					i = 0
					for p in c.getListaDePromocoesInternet():
						print('\nPromoção:\n\tNome: %s' % p.getNome())
						print('\tValidade: ' + c.getListaDeValidadeInternet()[i].strftime('%d/%m/%Y'))
						i += 1

	def opcao_18(self):
		the_file = open('operadora_celular.dat', 'wb')
		pickle.dump(self.__operadora, the_file)
		the_file.close()
	
	def criarCliente(self, operadora):
		print ('\nDigite os dados do cliente')
		nome = raw_input('Nome: ')
		cpf_cnpj = raw_input('CPF/CNPJ: ')
		endereco = raw_input('Endereço: ')
		cliente = Cliente(nome, cpf_cnpj, endereco)
		return(cliente)

	def escolhaTipoCelular(self):
		try:
			print('\nTipos de celulares disponíveis:\n1) RegularPhone\n2) SmarthPhone')
			escolha = int(input('>> '))
			if(escolha == 1) or (escolha == 2):
				return(escolha)
			else:
				print('\nOpção inválida')
				return(-1)
		except:
			print('\nOpção inválida')
			return(-1)

	def escolhaTipoPlano(self):
		try:
			print('\nTipos de planos disponíveis:\n1) Cartão\n2) Assinatura')
			escolha = int(input('>> '))
			if(escolha == 1) or (escolha == 2):
				return(escolha)
			else:
				print('\nOpção inválida')
				return(-1)
		except:
			print('\nOpção inválida')
			return(-1)

	def escolhaPlanoCartao(self, operadora):
		lista_de_planos = operadora.getListaPlanosCartao()
		if(len(lista_de_planos) == 0):
			print('\nNão há planos do tipo cartão disponíveis')
			return(-1)
		i = 1
		print('\n\nPlanos:')
		for p in lista_de_planos:
			print('\t%d) %s' % (i, p.getNome()))
			i += 1
		try:
			escolha = int(input('\nEscolha a opção de plano desejado:\n>> '))
			if(escolha >= 1) and (escolha <= len(lista_de_planos)):
				plano = lista_de_planos[escolha - 1]
				return(plano)
			else:
				print('\nOpção inválida')
				return(-1)
		except:
				print('\nOpção inválida')
				return(-1)

	def escolhaPlanoAssinatura(self, operadora):
		lista_de_planos = operadora.getListaPlanosAssinatura()
		if(len(lista_de_planos) == 0):
			print('\nNão há planos do tipo assinatura disponíveis')
			return(-1)
		i = 1
		print('\n\nPlanos:')
		for p in lista_de_planos:
			print('\t%d) %s' % (i, p.getNome()))
			i += 1
		try:
			escolha = int(input('\nEscolha a opção de plano desejado:\n>> '))
			if(escolha >= 1) and (escolha <= len(lista_de_planos)):
				plano = lista_de_planos[escolha - 1]
				return(plano)
			else:
				print('\nOpção inválida')
				return(-1)
		except:
				print('\nOpção inválida')
				return(-1)

	def escolhaPromocaoRegularPhoneCartao(self, operadora, celular):
		lista_de_promocoes = operadora.getListaPromocoesBonus()[:]
		if(len(lista_de_promocoes) == 0):
			print('\nNão há promoções disponíveis para o plano escolhido')
			return
		i = 1
		print('\n\nPromoções:')
		while(True) and (len(lista_de_promocoes) > 0):
			for p in lista_de_promocoes:
				print('\t%d) %s' % (i, p.getNome()))
				i += 1
			print('\t0) Terminar')
			try:
				escolha = int(input('\nEscolha a opção de promoção desejada:\n>> '))
				if(escolha >= 1) and (escolha <= len(lista_de_promocoes)) and (escolha != 0):
					promocao = lista_de_promocoes[escolha - 1]
					hoje = date.today()
					dias = timedelta(days = promocao.getValidade())
					celular.adicionarPromocao(promocao)
					celular.adicionarValidade(hoje + dias)
					del lista_de_promocoes[escolha - 1]
					i = 1
				elif(escolha == 0):
					return
				else:
					print('Opção inválida')
					i = 1
			except:
				print('\nOpção inválida')
				i = 1

	def escolhaPromocaoRegularPhoneAssinatura(self, operadora, celular):
		lista_de_promocoes = operadora.getListaPromocoesMinutos()[:]
		if(len(lista_de_promocoes) == 0):
			print('\nNão há promoções disponíveis para o plano escolhido')
			return
		i = 1
		print('\n\nPromoções:')
		while(True) and (len(lista_de_promocoes) > 0):
			for p in lista_de_promocoes:
				print('\t%d) %s' % (i, p.getNome()))
				i += 1
			print('\t0) Terminar')
			try:
				escolha = int(input('\nEscolha a opção de promoção desejada:\n>> '))
				if(escolha >= 1) and (escolha <= len(lista_de_promocoes)) and (escolha != 0):
					promocao = lista_de_promocoes[escolha - 1]
					hoje = date.today()
					dias = timedelta(days = promocao.getValidade())
					celular.adicionarPromocao(promocao)
					celular.adicionarValidade(hoje + dias)
					del lista_de_promocoes[escolha - 1]
					i = 1
				elif(escolha == 0):
					break
			except:
				print('\nOpção inválida')
				i = 1			

	def escolhaPromocaoSmartPhoneCartao(self, operadora, celular):
		lista_de_promocoes_internet = operadora.getListaPromocoesInternet()[:]
		if(len(lista_de_promocoes_internet) != 0):
			i = 1
			print('\n\nPromoções de Internet:')
			while(True):
				for p in lista_de_promocoes_internet:
					print('\t%d) %s' % (i, p.getNome()))
					i += 1
				print('\t0) Terminar')
				try:
					escolha = int(input('\nEscolha a opção de promoção desejada:\n>> '))
					if(escolha >= 1) and (escolha <= len(lista_de_promocoes_internet)) and (escolha != 0):
						promocao = lista_de_promocoes_internet[escolha - 1]
						hoje = date.today()
						dias = timedelta(days = promocao.getValidade())
						celular.adicionarPromocaoInternet(promocao)
						celular.adicionarValidadeInternet(hoje + dias)
						break
					elif(escolha == 0):
						break
					else:
						print('Opção inválida')
						i = 1	
				except:
					print('Opção inválida')
					i = 1
		self.escolhaPromocaoRegularPhoneCartao(operadora, celular)

	def escolhaPromocaoSmartPhoneAssinatura(self, operadora, celular):
		lista_de_promocoes_internet = operadora.getListaPromocoesInternet()[:]
		if(len(lista_de_promocoes_internet) != 0):
			i = 1
			print('\nPromoções de Internet:')
			while(True):
				for p in lista_de_promocoes_internet:
					print('\t%d) %s' % (i, p.getNome()))
					i += 1
				print('\t0) Terminar')
				try:
					escolha = int(input('\nEscolha a opção de promoção desejada:\n>> '))
					if(escolha >= 1) and (escolha <= len(lista_de_promocoes_internet)) and (escolha != 0):
						celular.adicionarPromocaoInternet(lista_de_promocoes_internet[escolha - 1])
						hoje = date.today()
						dias = timedelta(days = lista_de_promocoes_internet[escolha - 1].getValidade())
						celular.adicionarValidadeInternet(hoje + dias)
						break
					elif(escolha == 0):
						break
					else:
						print('Opção inválida')
						i = 1
				except:
					print('Opção inválida')
					i = 1
		self.escolhaPromocaoRegularPhoneAssinatura(operadora, celular)

	def vencimentoFatura(self):
		while(True):
			try:
				dia = int(input('\nEscolha o dia de vencimento da fatura:\n>> '))
				if(dia >= 1) and (dia <= 30):
					return(dia)
				else:
					print('\nDia inválido')
			except:
				print('\nDia inválido')

	def adicionarPromocaoSimplesCelular(self, operadora, c):
		if('Cartão' in c.getTipoPlano()):
			lista_de_promocoes_disponiveis = operadora.getListaPromocoesBonus()[:]
		elif('Assinatura' in c.getTipoPlano()):	
			lista_de_promocoes_disponiveis = operadora.getListaPromocoesMinutos()[:]
		lista_de_promocoes = c.getListaDePromocoes()
		for pc in lista_de_promocoes:
			i = 0
			for po in lista_de_promocoes_disponiveis:
				if(pc.getNome() in po.getNome()):
					del lista_de_promocoes_disponiveis[i]
				else:
					i += 1
		i = 1
		while(True) and (len(lista_de_promocoes_disponiveis) > 0):
			print('Promocões disponíveis:')
			for p in lista_de_promocoes_disponiveis:
				print('\t%d) %s' % (i, p.getNome()))
			i += 1
			print('\t0) Terminar')
			try:
				e = int(input('\nEscolha a promoção desejada\n>> '))
				if(e >= 1) and (e <= len(lista_de_promocoes_disponiveis)) and (e != 0):
					promocao = lista_de_promocoes_disponiveis[e - 1]
					hoje = date.today()
					dias = timedelta(days = promocao.getValidade())
					c.adicionarPromocao(promocao)
					c.adicionarValidade(hoje + dias)
					del lista_de_promocoes_disponiveis[e - 1]
					i = 1
				elif(e == 0):
					break
				else:
					print('\nOpção inválida')
			except:
				print('\nOpção inválida')
				i = 1

	def adicionarPromocaoInternetCelular(self, operadora, c):
		lista_de_promocoes_internet = c.getListaDePromocoesInternet()
		if(len(lista_de_promocoes_internet) == 0):
			lista_de_promocoes_disponiveis = operadora.getListaPromocoesInternet()[:]
			for pc in lista_de_promocoes_internet:
				i = 0
				for po in lista_de_promocoes_disponiveis:
					if(pc.getNome() in po.getNome()):
						del lista_de_promocoes_disponiveis[i]
					else:
						i += 1
			i = 1
			while(True):
				print('Promocões de internet disponíveis:')
				for p in lista_de_promocoes_disponiveis:
					print('\t%d) %s' % (i, p.getNome()))
					i += 1
				print('\t0) Terminar')
				try:
					e = int(input('\nEscolha a promoção de internet desejada\n>> '))
					if(e >= 1) and (e <= len(lista_de_promocoes_disponiveis)) and(e != 0):
						promocao = lista_de_promocoes_disponiveis[e - 1]
						c.adicionarPromocaoInternet(promocao)
						hoje = date.today()
						dias = timedelta(days = promocao.getValidade())
						c.adicionarValidadeInternet(hoje + dias)
						break
					elif(e == 0):
						break
					else:
						print('\nOpção inválida')
				except:
					print('\nOpção inválida')
					i = 1					

	def mostrarNumerosCelulares(self, operadora, lista):
		if(len(lista) == 0):
			print('\nNão há celulares disponíveis')
			return(-1)
		print('\nNúmeros de celulares disponíveis:')
		for c in lista:
			print('\t* %d' % c.getNumero())

									
if __name__ == '__main__':
	interface = Interface()
	interface.menu()

