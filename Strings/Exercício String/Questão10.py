n�mero = eval(input("escreva um n�mero at� 99:"))
nString = str(n�mero)
dezena = ''
unidade = ''
if n�mero == 0:
	print("\nZero.")
elif n�mero > 0 and n�mero < 10:
	if n�mero == 1:
		print("\nUm.")
	elif n�mero == 2:
		print("\nDois.")
	elif n�mero == 3:
		print("\nTr�s.")
	elif n�mero == 4:
		print("\nQuatro.")
	elif n�mero == 5:
		print("\nCinco.")
	elif n�mero == 6:
		print("\nSeis.")
	elif n�mero == 7:
		print("\nSete.")
	elif n�mero == 8:
		print("\nOito.")
	elif n�mero == 9:
		print("\nNove.")
elif n�mero > 9:
	if n�mero == 11:
		print('\nOnze.')
	elif n�mero == 12:
		print('\nDoze.')
	elif n�mero == 13:
		print('\nTreze.')
	elif n�mero == 14:
		print('\nQuatorze.')
	elif n�mero == 15:
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
		if n�mero > 19:
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
				unidade = ' e tr�s.'
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
