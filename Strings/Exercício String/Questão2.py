nome = str(input("Digite seu nome:"))
if not(nome.isupper()):
	print(nome.upper()[::-1])
else:
	print(nome[::-1])