print("P(n�mero positivo),N(n�mero negativo)\n")
def informa(n):
	if n <= 0:
		print('N')
	else:
		print('P')
n = eval(input("digite um n�mero:"))
informa(n)