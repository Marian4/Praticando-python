número = eval(input("escreva um número até 99:"))
nString = str(número)
dezena = ''
unidade = ''
if número == 0:
	print("\nZero.")
elif número > 0 and número < 10:
	if número == 1:
		print("\nUm.")
	elif número == 2:
		print("\nDois.")
	elif número == 3:
		print("\nTrês.")
	elif número == 4:
		print("\nQuatro.")
	elif número == 5:
		print("\nCinco.")
	elif número == 6:
		print("\nSeis.")
	elif número == 7:
		print("\nSete.")
	elif número == 8:
		print("\nOito.")
	elif número == 9:
		print("\nNove.")
elif número > 9:
	if número == 11:
		print('\nOnze.')
	elif número == 12:
		print('\nDoze.')
	elif número == 13:
		print('\nTreze.')
	elif número == 14:
		print('\nQuatorze.')
	elif número == 15:
		print('\nQuinze.')
	else:
		if nString[0] == '1':
			dezena = 'Dez'
			if nString[1] == '0':
				unidade = '.'
			elif nString[1] == '6':
				unidade = 'esseis.'
			elif nString[1] == '7':
				unidade = 'essete.'
			elif nString[1] == '8':
				unidade = 'oito.'
			elif nString[1] == '9':
				unidade = 'enove.'
			print("\n%s%s"%(dezena,unidade))
		if número > 19:
			if nString[0] == '2':
				dezena = 'Vinte'
			elif nString[0] == '3':
				dezena = 'Trinta'
			elif nString[0] == '4':
				dezena = 'Quarenta'
			elif nString[0] == '5':
				dezena = 'Cinquenta'
			elif nString[0] == '6':
				dezena = 'Sessenta'
			elif nString[0] == '7':
				dezena = 'Setenta'
			elif nString[0] == '8':
				dezena = 'Oitenta'
			elif nString[0] == '9':
				dezena = 'Noventa'
			if nString[1] == '0':
				unidade = '.'
			elif nString[1] == '1':
				unidade = ' e um.'
			elif nString[1] == '2':
				unidade = ' e dois.'
			elif nString[1] == '3':
				unidade = ' e três.'
			elif nString[1] == '4':
				unidade = ' e quatro.'
			elif nString[1] == '5':
				unidade = ' e cinco.'
			elif nString[1] == '6':
				unidade = ' e seis.'
			elif nString[1] == '7':
				unidade = ' e sete.'
			elif nString[1] == '8':
				unidade = ' e oito.'
			elif nString[1] == '9':
				unidade = ' e nove.'
			print("\n%s%s"%(dezena,unidade))
