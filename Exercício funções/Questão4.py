print("P(número positivo),N(número negativo)\n")
def informa(n):
	if n <= 0:
		print('N')
	else:
		print('P')
n = eval(input("digite um número:"))
informa(n)